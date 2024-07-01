from dotenv import load_dotenv
import streamlit as st
from user_utils import *

if 'HR_tickets' not in st.session_state:
    st.session_state['HR_tickets'] =[]
if 'IT_tickets' not in st.session_state:
    st.session_state['IT_tickets'] =[]
if 'Transport_tickets' not in st.session_state:
    st.session_state['Transport_tickets'] =[]


def main():
    load_dotenv()

    st.header("Automatic Ticket Classification Tool")
    st.write("We are here to help you, please ask your question:")
    user_input = st.text_input("🔍")

    if user_input:

        embeddings=create_embeddings()

        import os
    
        index=pull_from_pinecone(os.getenv("PINECONE_API_KEY"),"gcp-starter","tickets",embeddings)
        
       
        relavant_docs=get_similar_docs(index,user_input)

       
        response=get_answer(relavant_docs,user_input)
        st.write(response)

        button = st.button("Submit ticket?")

        if button:

            embeddings = create_embeddings()
            query_result = embeddings.embed_query(user_input)

            department_value = predict(query_result)
            st.write("your ticket has been sumbitted to : "+department_value)

            if department_value=="HR":
                st.session_state['HR_tickets'].append(user_input)
            elif department_value=="IT":
                st.session_state['IT_tickets'].append(user_input)
            else:
                st.session_state['Transport_tickets'].append(user_input)



if __name__ == '__main__':
    main()



