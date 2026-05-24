import streamlit as st
import google.generativeai as ai

# 1. API Key Setup (Secure Way)
API_KEY = st.secrets["GEMINI_API_KEY"]
ai.configure(api_key=API_KEY)
# 2. Page Configuration
st.set_page_config(page_title="Al Ramzan Academy Bot", page_icon="🤖", layout="centered")

# 3. Chatbot Header
st.title("🤖 Al Ramzan Academy Bot")
st.caption("Welcome! I am your AI assistant for programming and learning. Powered by Gemini.")

# 4. Chat History Initialize karna
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 5. Purani chat ko screen par dikhana
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

# 6. User ka input
user_query = st.chat_input("Ask me anything about Python, programming, or AI...")

if user_query:
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.chat_history.append({"role": "user", "text": user_query})
    
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
        
        with st.chat_message("assistant"):
            st.markdown(bot_response)
        st.session_state.chat_history.append({"role": "assistant", "text": bot_response})
        
    except Exception as e:
        st.error(f"Oho! Kuch masala hua hai: {e}")