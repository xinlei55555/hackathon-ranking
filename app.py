import streamlit as st
from io import StringIO
import pandas as pd
st.title("HYPE AI HAckathon") # Title


# '''
# Our app should be able to:
# - Accept PDF documents (CVs) as uploads 
# - Chatbots
# '''

# Upload button
# Transcript
# Summarizer
# Chat functionality
# Load messages from session storage
if "messages" not in st.session_state:
    st.session_state.messages = []
# Render each message in the chat container
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
uploaded_file = st.file_uploader("Upload a PDF")
with st.chat_message("assistant"):
    st.write("Hello 👋")
prompt = st.chat_input("Say something...")


if uploaded_file is not None:
    # To read file as bytes:
    print("OK")
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)


