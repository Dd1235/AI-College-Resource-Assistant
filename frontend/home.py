import streamlit as st


def show_home_page():
    st.title("Welcome to AI Resource Chat Bot")
    st.write(
        """
    This is the main homepage for the AI Resource Chat Bot.  
    Use the navigation in the sidebar to interact with the academic and personal chatbots.
    """
    )
    st.image("./assets/images/myself.jpeg", caption="AI Chatbot Platform")
