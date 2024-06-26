
import streamlit as st
import os
from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv

load_dotenv()

#customize the appearance of then Streamlit application's web page
st.set_page_config(page_title="Educate Kids", page_icon=":robot:")
st.header("Hey, Ask me something & I will give out similar things")

#Initialize the OpenAIEmbeddings object
embeddings = OpenAIEmbeddings()

# import CSV file data
from langchain.document_loaders.csv_loader import CSVLoader
loader = CSVLoader(file_path='myData.csv', csv_args={
    'delimiter': ',',
    'quotechar': '"',
    'fieldnames': ['Words']
})

data = loader.load()

#Display the data
print(data)

db = FAISS.from_documents(data, embeddings)

#Function to receive input from user
def get_text():
    input_text = st.text_input("You: ", key= input)
    return input_text


user_input=get_text()
submit = st.button('Find similar Things')  

if submit:
    
    #fetch the similar text
    docs = db.similarity_search(user_input)
    print(docs)
    st.subheader("Top Matches:")
    st.text(docs[0].page_content)
    st.text(docs[1].page_content)

