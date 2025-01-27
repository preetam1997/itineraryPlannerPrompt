import streamlit as st
import time
import json

# Assuming you have a 'get_model' and 'get_prompt' function in your Model and Prompt modules
from Model import get_model
from Prompt import get_prompt

st.title("Simple Chat")

# Initialize chat history if not already initialized
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Define response generator to handle chat completion with history
    def response_generator(user_prompt, api_key):
        # Initialize the model (ensure to use your specific model settings)
        model = get_model(0.2, 1, 1024, api_key)
        chat = model.start_chat()

        if len(st.session_state.messages) == 1:
            response = chat.send_message([get_prompt(), user_prompt, json.dumps(st.session_state.messages)])
        # Send the conversation to the model
        else:
            response = chat.send_message([user_prompt, json.dumps(st.session_state.messages)])

        # Extract the text of the response (check the exact attribute based on the model's API)
        return response.text  # Make sure this matches the actual response structure

    # Get the assistant's reply
    full_response = response_generator(prompt, api_key=st.secrets['api_key'])

    # Display the assistant's full response
    with st.chat_message("assistant"):
        st.markdown(full_response)

    # Once the full response is generated, append it to the chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
