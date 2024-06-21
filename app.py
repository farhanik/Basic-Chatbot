from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv
from langchain import OpenAI 

load_dotenv()

prompt= ChatPromptTemplate.from_messages(

    [
          ("system","You are a helpful medical report assistant.Please response to the user queries"),
          ("user","Question:{question}")
    ]
)


st.title('Simple Chatbot')
input_text = st.text_input("Write what you want")

llm=ChatOpenAI(model="gpt-3.5-turbo")
llm = ChatOpenAI(temperature=0.7)

output_parser=StrOutputParser()

chain = prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({"question":input_text}))