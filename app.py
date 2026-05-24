import streamlit as str
import google.generativeai as ai

# 1. API Key Setup
API_KEY = "AIzaSyCKz8tS2x1BCjrVhpHW57_Gl2eg3gGP-oI"
ai.configure(api_key=API_KEY)

# 2. Page Configuration
str.set_page_config(page_title="Al Ramzan Academy Bot", page_icon="🤖", layout="centered")

# 3. Chatbot Header
str.title("🤖 Al Ramzan Academy Bot")
str.caption("Welcome! I am your AI assistant for programming and learning. Powered by Gemini.")

# 4. Chat History Initialize karna
if "chat_history" not in str.session_state:
    str.session_state.chat_history = []

# 5. Purani chat ko screen par dikhana
for message in str.session_state.chat_history:
    with str.chat_message(message["role"]):
        str.markdown(message["text"])

# 6. User ka input
user_query = str.chat_input("Ask me anything about Python, programming, or AI...")

if user_query:
    with str.chat_message("user"):
        str.markdown(user_query)
    str.session_state.chat_history.append({"role": "user", "text": user_query})
    
    try:
        # Automatic valid model select karna
        available_models = [m.name for m in ai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        if available_models:
            model_name = available_models[0]
            model = ai.GenerativeModel(model_name)
            
            prompt = f"You are Al Ramzan Academy Bot, a helpful AI tutor for students. Answer this clearly: {user_query}"
            response = model.generate_content(prompt)
            bot_response = response.text
        else:
            bot_response = "Oho! Mujhe aapke system me koi valid Gemini model nahi mila."
        
        with str.chat_message("assistant"):
            str.markdown(bot_response)
        str.session_state.chat_history.append({"role": "assistant", "text": bot_response})
        
    except Exception as e:
        str.error(f"Oho! Kuch masala hua hai: {e}")