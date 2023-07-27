import streamlit as st
from io import StringIO
import pandas as pd
st.title("HYPE AI HAckathon") # Title
import time
import random

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
btn = False
if uploaded_file:
    st.header("Summarization")
    summary = "This text explains... demo text needs to be fixed" # Write Summarization here
    summary_placeholder = st.empty() 
    full_response = ""
    for chunk in summary.split():
        full_response += chunk + " "
        time.sleep(0.1)
        # Add a blinking cursor to simulate typing
        summary_placeholder.markdown(full_response + "▌")
    summary_placeholder.markdown(summary)
    btn = st.button("Click to Access the Chatbot")


if btn:
# Load messages from session storage
    if "messages" not in st.session_state:
        st.session_state.messages = []

    with st.chat_message("assistant"):
        st.write("Hello 👋 Ask the bot any question you want about the document!")
        # Render each message in the chat container
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Render new msg each time a new message is entered
    if prompt := st.chat_input("Say something..."): 
    # We used the := operator to assign the user's input to the prompt variable and checked if it's not None in the same line. If the user has sent a message, we display the message in the chat message container and append it to the chat history.
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Assistant response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            assistant_response = random.choice(
                [
                    "Hello there! How can I assist you today?",
                    "Hi, human! Is there anything I can help you with?",
                    "Do you need help?",
                ]
            )
            # Simulate stream of response with milliseconds delay
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})



# if uploaded_file is not None:
#     # To read file as bytes:
#     print("OK")
#     bytes_data = uploaded_file.getvalue()
#     st.write(bytes_data)

#     # To convert to a string based IO:
#     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#     st.write(stringio)

#     # To read file as string:
#     string_data = stringio.read()
#     st.write(string_data)


