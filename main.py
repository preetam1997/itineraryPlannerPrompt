import streamlit as st
import json


from Model import get_model
from Prompt import get_prompt

st.title("Simple Chat")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("What is up?"):

    with st.chat_message("user"):
        st.markdown(prompt)


    st.session_state.messages.append({"role": "user", "content": prompt})


    def response_generator(user_prompt, api_key):

        model = get_model(0.2, 1, 1024, api_key)
        chat = model.start_chat()

        if len(st.session_state.messages) == 1:
            response = chat.send_message([get_prompt(), user_prompt, json.dumps(st.session_state.messages)])

        else:
            response = chat.send_message([user_prompt, json.dumps(st.session_state.messages)])


        return response.text


    full_response = response_generator(prompt, api_key=st.secrets['api_key'])


    with st.chat_message("assistant"):
        st.markdown(full_response)


    st.session_state.messages.append({"role": "assistant", "content": full_response})
