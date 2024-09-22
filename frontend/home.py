import streamlit as st


def show_home_page():
    st.title("Welcome to AI Resource Chat Bot")

    # Introduction
    st.write(
        """
    The **AI Resource Chat Bot** is designed to assist you with information related to academic resources, personal data, and much more. 
     Here’s what you can do with the current version:
    """
    )

    # Guide for the current version of the Chat Bot
    st.header("Guide")
    st.write(
        """
    - **Academic Chat Bot**: Ask the academic chatbot any questions related to academic subjects, schedules, and resources available for semester 3. It uses context from preloaded information and answers queries based on that.
    - **Personal Chat Bot (Meet the Team)**: This chatbot provides personalized information about **Dedeepya Avancha**, including academic achievements, skills, and current projects. Future plans for this chatbot include expanding it into a **recruiter bot** to provide tailored information to potential employers.
    """
    )

    # Future Plans Section
    st.header("Future Plans")
    st.write(
        """
    As the **AI Resource Chat Bot** continues to evolve, here are some exciting features that will be added in the future:
    
    1. **Remembering Context**: The chatbot will be enhanced to remember user context across multiple interactions. This means the bot will be able to maintain a conversation, track past queries, and dynamically adjust responses based on past inputs.
    
    2. **User Sessions**: We are planning to integrate user sessions, where users can log in and have personalized experiences. Each session will store the user's information, preferences, and past interactions. This will make the chatbot more effective in answering personal and context-specific queries.
    
    3. **More Data Integration**: The academic chatbot will be expanded to include more subjects and academic years. Additionally, the bot will integrate with more resources, including lecture notes, video tutorials, and references from past exams.
    
    4. **Personal Chatbot for Recruiters**: One of the major features in development is a personalized chatbot designed for recruiters. This chatbot will provide structured information about **Dedeepya Avancha's** skills, qualifications, and projects, tailored to potential employers. It will be capable of answering common recruiter questions like qualifications, experience, projects, and more.
    """
    )

    # st.image(
    #     "https://via.placeholder.com/600x300",
    #     caption="AI Resource Chat Bot Expansion Plans",
    # )

    # Footer
    st.write(
        """
    Stay tuned for these updates as we continue to improve the chatbot’s capabilities!
    """
    )
