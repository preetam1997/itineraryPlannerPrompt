import streamlit as st
import random
import time

from Model import get_model
from Prompt import get_prompt

st.title("Simple chat")

# Initialize chat history if not already initialized
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
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


    # Call the response generator to get the assistant's reply
    def response_generator(user_prompt, api_key):
        model = get_model(0.2, 1, 1024, api_key)  # Initialize the model with your settings
        chat = model.start_chat()  # Start the chat session

        # Get the response from the assistant by sending the user's prompt and system prompt
        response = chat.send_message([get_prompt(), user_prompt])

        # Return the full response after processing
        return response.text


    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        # Get the complete response from the assistant
        full_response = response_generator(prompt, api_key=st.secrets['api_key'])

        # Display the full response at once
        st.markdown(full_response)

        # Once the full response is generated, append it to the chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
