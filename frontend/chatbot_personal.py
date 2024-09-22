import os

import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env in development mode
load_dotenv()
# Backend API URL for the Personal Chatbot
backend_url_personal = os.getenv(
    "BACKEND_URL_PERSONAL", "http://localhost:5000/chatbot/personal"
)


# Function to send query to the backend
def send_query_to_backend(api_url, user_input):
    try:
        response = requests.post(api_url, json={"message": user_input})
        if response.status_code == 200:
            return response.json().get("response", "No response received")
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Error: {e}"


def show_personal_chatbot():
    st.title("Meet the team")

    with st.form(key="personal_bot_form"):
        personal_input = st.text_input("Ask Personal Chat Bot:", "")
        submit_button = st.form_submit_button("Send to Personal Bot")

    # If the form is submitted
    if submit_button:
        if personal_input:
            personal_response = send_query_to_backend(
                backend_url_personal, personal_input
            )
            st.write(f"Personal Bot Response: {personal_response}")
        else:
            st.write("Please enter a question.")
