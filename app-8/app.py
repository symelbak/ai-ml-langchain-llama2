import streamlit as st 
from utils import generate_script

# Styling
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#FFFFFF;
    }
</style>""", unsafe_allow_html=True)


# Session State Variable
if 'API_Key' not in st.session_state:
    st.session_state['API_Key'] =''


st.title('YouTube Script Writing Tool') 

st.sidebar.title("🗝️")
st.session_state['API_Key']= st.sidebar.text_input("What's your API key?",type="password")
st.sidebar.image('./Youtube.jpg',width=300, use_column_width=True)


prompt = st.text_input('Please provide the topic of the video',key="prompt") 
video_length = st.text_input('Expected Video Length 🕒 (in minutes)',key="video_length") 
creativity = st.slider('Creativity limit ✨ - (0 LOW || 1 HIGH)', 0.0, 1.0, 0.2,step=0.1)

submit = st.button("Generate Script for me")


if submit:
    
    if st.session_state['API_Key']:
        search_result,title,script = generate_script(prompt,video_length,creativity,st.session_state['API_Key'])
        # generate the script
        st.success('Script:')

        #Display Title
        st.subheader("Title:")
        st.write(title["text"])

        #Display Video Script
        st.subheader("Your Video Script:")
        st.write(script)

        #Display Search Engine Result
        st.subheader("DuckDuckGo Search:")
        with st.expander('Expand'): 
            st.info(search_result)
    else:
        st.error("Please provide API key.....")