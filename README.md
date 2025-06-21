## Simple Gen AI App using Open AI 

# Langchain OpenAI Assistant with Langsmith Tracking 🤖

This repository hosts a simple Streamlit application that builds an AI assistant using LangChain and OpenAI, with integration for Langsmith tracing.

## ✨ Features

* **Interactive UI:** Built with Streamlit for easy interaction.
* **AI Assistant:** Uses OpenAI's `gpt-4o` model for responses.
* **LangChain Integration:** Connects prompt templates to the LLM and parses output.
* **Langsmith Tracking:** Configured for tracing and monitoring AI interactions.
* **Environment Variables:** Securely loads API keys and settings from a `.env` file.

## 🚀 Getting Started

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Abubakar0011/Simple_GenAI_App_Practice.git]
    cd your-repo-name
    ```
2.  **Set up Virtual Environment & Install Dependencies:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate # or .\.venv\Scripts\activate on Windows
    pip install streamlit langchain-core langchain-openai python-dotenv
    ```
3.  **Configure Environment Variables:**
    Create a `.env` file in your project root with your keys:
    ```dotenv
    OPENAI_API_KEY="your_openai_api_key_here"
    LANGCHAIN_API_KEY="your_langchain_api_key_here"
    LANGCHAIN_PROJECT="your-langsmith-project-name"
    ```
    **Remember to add `.env` to your `.gitignore`!**
4.  **Run the Application:**
    ```bash
    streamlit run app.py
    ```
