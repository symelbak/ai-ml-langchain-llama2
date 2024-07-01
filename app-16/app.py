
from langchain_openai import ChatOpenAI

from langchain.schema import HumanMessage, SystemMessage
from io import StringIO
import streamlit as st
from dotenv import load_dotenv
import time
import base64


load_dotenv()

st.title("Let's do code review for your python code")
st.header("Please upload your .py file here:")


def text_downloader(raw_text):

    timestr = time.strftime("%Y%m%d-%H%M%S")
    
    b64 = base64.b64encode(raw_text.encode()).decode()
 
    new_filename = "code_review_analysis_file_{}_.txt".format(timestr)
    
    st.markdown("#### Download File ✅###")
    
    
    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click Here!!</a>'

    st.markdown(href, unsafe_allow_html=True)

data = st.file_uploader("Upload python file",type=".py")

if data:

   
    stringio = StringIO(data.getvalue().decode('utf-8'))

    
    fetched_data = stringio.read()

    
    st.write(fetched_data)

   
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9)

   
    systemMessage = SystemMessage(content="You are a code review assistant. Provide detailed suggestions to improve the given Python code along by mentioning the existing code line by line with proper indent")

   
    humanMessage = HumanMessage(content=fetched_data)

    finalResponse = chat.invoke([systemMessage, humanMessage])

    st.markdown(finalResponse.content)

    text_downloader(finalResponse.content)

