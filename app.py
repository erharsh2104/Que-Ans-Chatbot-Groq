import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_messages([('system','You are an Helpful AI Assistant'),
                                           ('human','Question : {Question}')])

def generate_response(query,llm,temperature,max_tokens,api_key):
    model=ChatGroq(model=llm,temperature=temperature,api_key=api_key,max_tokens=max_tokens)
    parser = StrOutputParser()
    chain=prompt | model | parser
    result=chain.invoke({'Question':query})
    return result

st.title("Q and A Chatbot with Groq")

st.sidebar.title('Settings')

api=st.sidebar.text_input('Provide the Groq API Key',type='password')

llm=st.sidebar.selectbox('Select the LLM :',['openai/gpt-oss-20b','openai/gpt-oss-120b','openai/gpt-oss-safeguard-20b'])

temperature=st.sidebar.slider('Temperature',min_value=0.0,max_value=1.0,value=0.7)

max_tokens=st.sidebar.slider('Max Tokens',min_value=50,max_value=2048,value=300)

query=st.text_input('What is your Query')

if st.button('Answer'):
    if query:
        if not api:
            st.warning('Please enter your Groq API key in the sidebar.')
        else:
            try:
                st.write(generate_response(query,llm,temperature,max_tokens,api))
            except Exception as e:
                st.error(f'Error: {e}')
    else:
        st.write('Please provide your query')