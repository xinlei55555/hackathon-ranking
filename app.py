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


uploaded_file = st.file_uploader("Upload a PDF")
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
