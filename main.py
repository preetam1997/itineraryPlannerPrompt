import streamlit as st
import random
import time

from Model import get_model

st.title("Simple chat")

# Initialize chat history
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

def response_generator(user_prompt, api_key):
    model = get_model(0.2,1,1024, api_key)
    response = model.send_message(user_prompt)

    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# Display assistant response in chat message container
with st.chat_message("assistant"):
    response = st.write_stream(response_generator(prompt, api_key=st.secrets['api_key']))
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})