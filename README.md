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
  - [Run the Flask Backend](#run-the-flask-backend)
  - [Run the Streamlit Frontend](#run-the-streamlit-frontend)
  - [Create Vector Stores](#create-vector-stores)
- [Future Plans](#future-plans)
- [Contributing](#contributing)
- [License](#license)

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

## Project Structure

````bash
.
├── backend/
│   └── app.py                    # Flask backend to handle chat requests
├── db/information/
│   ├── academic/
│   │   ├── iiit_bangalore_general_info.txt   # Academic info for IIIT Bangalore
│   │   └── semester_3_academics.txt          # Academic info for Semester 3
│   ├── personal/
│   │   └── dedeepya_avancha_profile.txt      # Personal profile information
├── frontend/
│   ├── chatbot_academic.py        # Streamlit page for academic chatbot
│   ├── chatbot_personal.py        # Streamlit page for personal chatbot
│   ├── home.py                    # Streamlit page for the home (guide and future plans)
│   └── streamlit_app.py           # Main Streamlit app to handle navigation and UI
├── scripts/
│   └── create_vector_store.py     # Script to create vector stores for academic/personal data
├── .gitignore                     # Gitignore file
├── LICENSE                        # License for the project
├── README.md                      # Readme file (this file)
├── poetry.lock                    # Poetry lock file for dependency management
└── pyproject.toml                 # Poetry project configuration


## Setup

Follow these steps to set up the **AI College Resource Chat Bot** project on your local machine.

### 1. Clone the Repository

First, clone the repository from GitHub:

```bash
git clone https://github.com/Dd1235/AI-College-Resource-Assistant.git
cd AI-College-Resource-Assistant
````

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

###5. Create Vector Stores

To create vector stores for academic and personal data, run:

```bash
poetry run python scripts/create_vector_store.py
```

This script will generate vector stores for academic and personal data, which are used for efficient search and retrieval of information.

We are using the `Chroma` library to create vector stores. The script reads the academic and personal data from the `db/information` directory and creates vector stores in the `db/vector_stores` directory.

For embedding we are using the `langchain` library which is a wrapper around OpenAI's embedding models.
The OpenAI embedding model is text-embedding-3-small as it is the smallest model available and is sufficient for our use case.
The llm used is gpt-3.5-turbo.

### 5. Run the Flask Backend

To start the Flask backend, run:

```bash
poetry run python backend/app.py
```

### 6. Run the Streamlit Frontend

To start the Streamlit frontend, run:

```bash
poetry run streamlit run frontend/streamlit_app.py
```
