import os
import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv
load_dotenv()


# Langsmith Tracking
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. Provide me answers based on the input."),
        ("human", "{input}"),
    ]
)

# Streamlit APP
st.title("Langchain with OpenAI and Langsmith Tracking")
input_text = st.text_input("Enter your question: ")

# LLM model
llm = ChatOpenAI(model="gpt-4o")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"input": input_text}))
