# AI College Resource Chat Bot

This project is an AI-powered chatbot system designed to assist with academic and personal queries using **OpenAI's GPT-3.5** model and embeddings for search and retrieval. The project allows users to interact with a chatbot for academic queries, currently only implemented for semester 3 of IIIT Bangalore, as well as a personal bot providing personalized information about **Dedeepya Avancha**.

## Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Clone the Repository](#clone-the-repository)
  - [Install Poetry](#install-poetry)
  - [Install Dependencies](#install-dependencies)
  - [Set Up Environment Variables](#set-up-environment-variables)
  - [Create Vector Stores](#create-vector-stores)
  - [Run the Flask Backend](#run-the-flask-backend)
  - [Run the Streamlit Frontend](#run-the-streamlit-frontend)
- [Future Plans](#future-plans)
- [License](https://github.com/Dd1235/AI-College-Resource-Assistant/blob/main/LICENSE)

## Overview

The **AI College Resource Chat Bot** uses **OpenAI's GPT-3.5** to generate answers to questions based on user queries. It utilizes vector embeddings for efficient search and retrieval of academic and personal information. This project is designed to be flexible, allowing users to extend the bot with more personalized information or academic data.

## Tech Stack

- **Backend**: Flask
- **Frontend**: Streamlit
- **OpenAI API**: GPT-3.5 and OpenAI's embedding models
- **Database**: Vector stores using `Chroma`
- **Python Libraries**: `openai`, `langchain`, `Pillow`, `requests`, `streamlit`, `flask`
- **Dependency Management**: Poetry

## Features

- **Academic Chat Bot**: Handles questions related to Semester 3 academics at IIIT Bangalore, including course descriptions and schedules.
- **Personal Chat Bot**: Provides personalized information about **Dedeepya Avancha**, such as academic background, projects, and ongoing work.
- **Vector Store for Search**: The project uses OpenAI's embeddings to convert text into vectors, which allows for efficient searching and answering of queries.


## Setup

Follow these steps to set up the **AI College Resource Chat Bot** project on your local machine.

### 1. Clone the Repository

First, clone the repository from GitHub:

```bash
git clone https://github.com/Dd1235/AI-College-Resource-Assistant.git
cd AI-College-Resource-Assistant
```

### 2. Install Poetry

The project uses **Poetry** for dependency management. Follow these steps to install Poetry:

#### For Unix/macOS:

Run the following command to install Poetry:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

#### For Windows:

Follow the [official installation guide](https://python-poetry.org/docs/#installation) on the Poetry website.

#### Verify Installation

To confirm Poetry is installed correctly, run:

```bash
poetry --version
```

#### Verify Installation

To confirm Poetry is installed correctly, run:

```bash
poetry --version
```

### 3. Install Dependencies

Next, install the project dependencies using Poetry:

```bash
poetry install
```

### 4. Set Up Environment Variables

Create a `.env` file with the following environment variables:

```bash
OPENAI_API_KEY=<your-openai-api-key>
```

### 5. Create Vector Stores

To create vector stores for academic and personal data, run:

```bash
poetry run python scripts/create_vector_store.py
```

This script will generate vector stores for academic and personal data, which are used for efficient search and retrieval of information.

We are using the `Chroma` library to create vector stores. The script reads the academic and personal data from the `db/information` directory and creates vector stores in the `db/vector_stores` directory.

For embedding we are using the `langchain` library which is a wrapper around OpenAI's embedding models.
The OpenAI embedding model is text-embedding-3-small as it is the smallest model available and is sufficient for our use case.
The llm used is gpt-3.5-turbo.

### 6. Run the Flask Backend

To start the Flask backend, run:

```bash
poetry run python backend/app.py
```

### 7. Run the Streamlit Frontend

To start the Streamlit frontend, run:

```bash
poetry run streamlit run frontend/streamlit_app.py
```

## Future Plans

### 1. **Extend Academic Chat Bot**
   - Expand the academic chatbot to support queries for **all semesters**, not just semester 3.
   - Include **syllabi, grading formats, schedules**, and other academic resources for each course.
   - Add **professor-specific information**, such as contact details and office hours.

### 2. **Add Personalization**
   - Allow users to input their own personal data, such as **grades** or **projects**, and have the chatbot remember it for future interactions.
   - Enable the chatbot to store personalized academic progress (e.g., GPA calculations across semesters) and answer questions like "What is my overall GPA?"
   - Add support for storing **course preferences** and **extra-curricular interests** to help the bot provide personalized suggestions.

### 3. **Session Memory**
   - Implement **session memory** so the chatbot can maintain the context of a conversation during a session. This would allow users to ask follow-up questions without repeating information (e.g., "What is my GPA?" followed by "What is the grading scale for Signals and Systems?").
   - Add the capability to store and retrieve information across multiple sessions, so returning users can resume where they left off.

### 4. **Add Support for Recruiters**
   - Develop a separate mode for recruiters, which provides detailed student profiles for review during interviews or recruitment.
   - Allow recruiters to ask questions related to students’ academic performance, skills, projects, and internship experience.
   - Integrate LinkedIn and GitHub profiles for a more comprehensive view of students’ technical skills and professional background.

### 5. **Performance Enhancements**
   - Optimize the vector store and embedding retrieval for faster response times, especially as more data is added.
   - Explore integrating more efficient, smaller models like **text-embedding-3-small** for specific use cases to balance between accuracy and performance.

### 6. **Deploy a Fully Scalable Production System**
   - Deploy the project in a fully scalable production environment using **containerization (Docker)** for easy deployment and management.
   - Implement monitoring and logging tools to track performance and usage.
   - Add support for **horizontal scaling** to handle increased traffic, especially if this solution is rolled out to a larger number of students or institutions.

### 7. **Expand to More Institutions**
   - Make the system adaptable to other institutions by providing a template where users can input their institution’s academic information.
   - Allow admins or academic staff from other colleges to upload their own course data, creating a scalable resource assistant for any academic institution.


