# import streamlit as st
#
# from Model import get_model
#
# API_KEY = st.secrets["api_key"]
# # Function to generate a simple response (replace with your AI model call)
# def generate_response(user_input, api_key):
#     model = get_model(0.2,1,1024, api_key)
#     chat = model.start_chat()
#     response = chat.send_message(user_input)
#     return response.text
#
# # Streamlit interface
# def chatbot_interface():
#     st.title("Travel Planning Chatbot")
#
#     # Initialize the chat history (session state)
#     if 'chat_history' not in st.session_state:
#         st.session_state['chat_history'] = []
#
#     # User input field
#     user_input = st.text_input("You: ", "")
#
#     # Handle chat when the user submits input
#     if st.button("Send") and user_input.strip() != "":
#         # Store user input in the chat history
#         st.session_state['chat_history'].append(f"You: {user_input}")
#
#         # Generate a response (this is where you'd plug in an AI model like Google Gemini)
#         bot_response = generate_response(user_input, API_KEY)
#
#         # Store bot response in the chat history
#         st.session_state['chat_history'].append(f"Bot: {bot_response}")
#
#         # Clear the user input field after sending the message
#         st.text_input("You: ", "", key="input_text")
#
#     # Display the chat history
#     for message in st.session_state['chat_history']:
#         st.write(message)
#
#
# if __name__ == "__main__":
#     chatbot_interface()

import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
