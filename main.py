import streamlit as st


# Function to generate a simple response (replace with your AI model call)
def generate_response(user_input):
    # Simulate a basic response
    # Replace this with a call to an AI model such as Google Gemini, OpenAI, or any other model
    if "hello" in user_input.lower():
        return "Hi there! How can I assist you with your trip planning today?"
    elif "help" in user_input.lower():
        return "Sure, I can help you with travel itinerary planning, recommendations, and more. What would you like to know?"
    else:
        return "Sorry, I didn't understand that. Can you please clarify?"


# Streamlit interface
def chatbot_interface():
    st.title("Travel Planning Chatbot")

    # Initialize the chat history (session state)
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # User input field
    user_input = st.text_input("You: ", "")

    # Handle chat when the user submits input
    if st.button("Send") and user_input.strip() != "":
        # Store user input in the chat history
        st.session_state['chat_history'].append(f"You: {user_input}")

        # Generate a response (this is where you'd plug in an AI model like Google Gemini)
        bot_response = generate_response(user_input)

        # Store bot response in the chat history
        st.session_state['chat_history'].append(f"Bot: {bot_response}")

        # Clear the user input field after sending the message
        st.text_input("You: ", "", key="input_text")

    # Display the chat history
    for message in st.session_state['chat_history']:
        st.write(message)


if __name__ == "__main__":
    ch