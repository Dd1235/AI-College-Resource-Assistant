import os

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings

current_dir = os.path.dirname(os.path.abspath(__file__))

academic_dir = os.path.join(current_dir, "../db/information/academic")

personal_dir = os.path.join(current_dir, "../db/information/personal")


academic_persistent_directory = os.path.join(
    current_dir, "../db/vector_stores/academic"
)
personal_persistent_directory = os.path.join(
    current_dir, "../db/vector_stores/personal"
)

# Initialize embedding model
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


def create_vector_store(doc_dir, persist_dir, description):
    print(f"\n--- Processing {description} ---")
    if not os.path.exists(persist_dir):
        print(
            f"Persistent directory does not exist. Initializing vector store for {description}..."
        )

        if not os.path.exists(doc_dir):
            raise FileNotFoundError(
                f"The directory {doc_dir} does not exist. Please check the path."
            )

        documents = []
        text_files = [f for f in os.listdir(doc_dir) if f.endswith(".txt")]
        for text_file in text_files:
            print(f"taking care of text file {text_file}")
            file_path = os.path.join(doc_dir, text_file)
            loader = TextLoader(file_path)
            docs = loader.load()
            for doc in docs:
                doc.metadata = {"source": text_file}
                documents.append(doc)

        # Use RecursiveCharacterTextSplitter to split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=100
        )
        docs = text_splitter.split_documents(documents)

        # Create and persist the vector store
        print(f"Creating embeddings and vector store for {description}...")
        vector_store = Chroma.from_documents(
            docs, embeddings, persist_directory=persist_dir
        )
        vector_store.persist()
        print(f"Vector store for {description} created and saved at {persist_dir}.")
    else:
        print(f"Vector store for {description} already exists. No need to initialize.")


# Generate vector stores for academic and personal data
create_vector_store(academic_dir, academic_persistent_directory, "Academic Information")
create_vector_store(personal_dir, personal_persistent_directory, "Personal Information")
