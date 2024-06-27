import streamlit as st
from dotenv import load_dotenv
from utils import query_agent

load_dotenv()


st.title("CSV analysis tool")
st.header("Please upload your CSV file here:")

data = st.file_uploader("Upload CSV file",type="csv")

query = st.text_area("Enter your query")
button = st.button("Generate Response")

if button:
    #Response
    answer =  query_agent(data,query)
    print(answer['output'])
    st.write(answer['output'])