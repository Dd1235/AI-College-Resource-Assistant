import os

import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env in development mode
load_dotenv()
# Backend API URL for the Academic Chatbot
backend_url_academic = os.getenv(
    "BACKEND_URL_ACADEMIC", "http://localhost:5000/chatbot/academic"
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


def show_academic_chatbot():
    st.title("AI Resource Chat Bot - Academic")

    # Create a form to handle the input submission
    with st.form(key="academic_bot_form"):
        academic_input = st.text_input("Ask Academic Chat Bot:", "")

        # Form submit button
        submit_button = st.form_submit_button("Send to Academic Bot")

    # If the form is submitted
    if submit_button:
        if academic_input:
            academic_response = send_query_to_backend(
                backend_url_academic, academic_input
            )
            st.write(f"Academic Bot Response: {academic_response}")
        else:
            st.write("Please enter a question.")
