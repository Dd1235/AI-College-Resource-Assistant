import logging
import os

from config import DevelopmentConfig, ProductionConfig
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Initialize Flask App
app = Flask(__name__)

if os.getenv("FLASK_ENV") == "production":
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

# Load environment variables from .env in development mode
# load_dotenv()


limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["20 per minute, 40 per day"],  # Set default limit
)


# Enable logging
logging.basicConfig(level=logging.INFO)


from flask_cors import CORS

CORS(app)

current_dir = os.path.dirname(os.path.abspath(__file__))
academic_vector_store_path = os.path.join(current_dir, "./db/vector_stores/academic")
personal_vector_store_path = os.path.join(current_dir, "./db/vector_stores/personal")

# Initialize the embedding model
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Load Academic and Personal Vector Stores with error handling
try:
    academic_vector_store = Chroma(
        persist_directory=academic_vector_store_path, embedding_function=embeddings
    )
except Exception as e:
    print(f"Error loading academic vector store: {e}")
    academic_vector_store = None

try:
    personal_vector_store = Chroma(
        persist_directory=personal_vector_store_path, embedding_function=embeddings
    )
except Exception as e:
    print(f"Error loading personal vector store: {e}")
    personal_vector_store = None

# Initialize the LLM using ChatOpenAI
llm = ChatOpenAI(model="gpt-3.5-turbo")


academic_prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template=(
        "You are an academic assistant. Use the following context to answer "
        "only questions related to IIITB's semester 3 academics or campus:\n\n"
        "{context}\n\nQuestion: {question}\nAnswer:"
    ),
)

personal_prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template=(
        "You are an assistant specialized in answering questions only related to Dedeepya Avancha, to potential recruiters. Keep the answers professional and concise. "
        "she made this platform and so currently the team behind this app consists of only her,"
        "a second-year IMTech Computer Science student at IIIT Bangalore. ... "
        "{context}\n\nQuestion: {question}\nAnswer:"
    ),
)

# Create RetrievalQA chains for both academic and personal chatbots
academic_qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=academic_vector_store.as_retriever() if academic_vector_store else None,
    chain_type_kwargs={"prompt": academic_prompt_template},
)

personal_qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=personal_vector_store.as_retriever() if personal_vector_store else None,
    chain_type_kwargs={"prompt": personal_prompt_template},
)


# Helper function to query vector store and LLM
def query_vector_store(qa_chain, user_input):
    response = qa_chain.run(user_input)
    return response


@app.route("/")
def index():
    return jsonify({"message": "Hello from Flask backend!"})


# Academic Information Chatbot
@app.route("/chatbot/academic", methods=["POST"])
@limiter.limit("10 per minute, 20 per day")
def chatbot_academic():
    data = request.get_json()
    if not data or "message" not in data or not isinstance(data.get("message"), str):
        return jsonify({"error": "Invalid input or missing 'message' key."}), 400
    user_input = data.get("message", "")
    logging.info("Received academic query: %s", user_input)

    response = query_vector_store(academic_qa_chain, user_input)
    logging.info("Academic response: %s", response)

    return (
        jsonify({"response": response})
        if response
        else jsonify({"response": "No relevant information found."})
    )


# Personal Information Chatbot
@app.route("/chatbot/personal", methods=["POST"])
@limiter.limit("5 per minute, 20 per day")
def chatbot_personal():
    data = request.get_json()
    if not data or "message" not in data or not isinstance(data.get("message"), str):
        return jsonify({"error": "Invalid input or missing 'message' key."}), 400
    user_input = data.get("message", "")
    logging.info("Received personal query: %s", user_input)

    response = query_vector_store(personal_qa_chain, user_input)
    logging.info("Personal response: %s", response)

    return (
        jsonify({"response": response})
        if response
        else jsonify({"response": "No relevant information found."})
    )


if __name__ == "__main__":
    # Cast the port to an integer (5000 is the default if PORT is not set)
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
