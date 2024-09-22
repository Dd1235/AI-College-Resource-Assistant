import os

import chatbot_academic
import chatbot_personal
import home
import streamlit as st

# from PIL import Image

# Set the page title and layout
st.set_page_config(page_title="AI Resource Chat Bot", layout="wide")

# Sidebar for page navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to", ["Home", "Chat Bot 1 - Academic", "Chat Bot 2 - Meet the team"]
)

# Render the selected page
if page == "Home":
    home.show_home_page()
elif page == "Chat Bot 1 - Academic":
    chatbot_academic.show_academic_chatbot()
elif page == "Chat Bot 2 - Meet the team":
    chatbot_personal.show_personal_chatbot()


# Caching the image to avoid reloading on every form submission
# @st.cache_resource
# def load_image(image_path):
#     return Image.open(image_path)


# Add a common footer or team section on all pages
st.sidebar.subheader("Team")

# Get the current directory and the image path
current_dir = os.path.dirname(os.path.abspath(__file__))
# image_path = os.path.join(current_dir, "assets/images/myself.jpeg")

# # Load the image (using cache)
# image = load_image(image_path)

# # Remove the option to expand the image by hiding the full-screen button using CSS
# st.sidebar.markdown(
#     """
#     <style>
#     [data-testid="stImage"] button {visibility: hidden;}
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Display the image in the sidebar with a smaller size and caption
# st.sidebar.image(image, caption="Dedeepya Avancha", width=150)

# # Inject CSS for rounded corners on the image
# st.sidebar.markdown(
#     """
#     <style>
#     [data-testid="stImage"] img {
#         border-radius: 15px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# Add additional team information
st.sidebar.markdown(
    """
**Dedeepya Avancha**  
IMTech 2nd year, IIIT Bangalore  
[LinkedIn](https://www.linkedin.com/in/dedeepya-avancha-507363217/)
"""
)
