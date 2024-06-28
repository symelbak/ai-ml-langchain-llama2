import streamlit as st
from dotenv import load_dotenv
from pages.admin_utils import *


def main():
    load_dotenv()
    st.set_page_config(page_title="Dump PDF to Pinecone - Vector Store")
    st.title("Please upload your files...📁 ")

    pdf = st.file_uploader("Only PDF files allowed", type=["pdf"])

    if pdf is not None:
        with st.spinner('Wait for it...'):
            text=read_pdf_data(pdf)
            st.write("👉Reading PDF done")

            docs_chunks=split_data(text)

            st.write("👉Splitting data into chunks done")

            embeddings=create_embeddings_load_data()
            st.write("👉Creating embeddings instance done")

            import os
            push_to_pinecone(os.getenv("PINECONE_API_KEY"),"gcp-starter","tickets",embeddings,docs_chunks)

        st.success("Successfully pushed the embeddings to Pinecone")


if __name__ == '__main__':
    main()
