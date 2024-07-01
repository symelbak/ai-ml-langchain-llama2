import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.schema import(
    AIMessage,
    HumanMessage,
    SystemMessage
)

st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("Hey I am your chatbot")

if "sessionMessages" not in st.session_state:
    st.session_state.sessionMessages = [
        SystemMessage(content="you are a helpful assistant.")
    ]

def load_answer(question):
    st.session_state.sessionMessages.append(HumanMessage(content=question))
    response = llm(st.session_state.sessionMessages)
    st.session_state.sessionMessages.append(AIMessage(content=response.content))
    return response.content

def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest")

user_input = get_text()
submit = st.button('Generate')

if submit:
    response = load_answer(user_input)
    st.subheader("Answer:")
    st.write(response,key = 1)
