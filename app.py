import streamlit as st
from groq import Groq

# 🔑 Load API key
api_key = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=api_key)

st.set_page_config(page_title="MindBalance AI", layout="wide")

# ---------- 🌌 NEON GLASS UI ----------
st.markdown("""
<style>

/* 🌈 Animated gradient background */
body {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    background-size: 300% 300%;
    animation: gradientMove 16s ease infinite;
}

@keyframes gradientMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* 💎 Apply glass effect to main container */
section.main > div {
    background: rgba(255, 255, 255, 0.10);
    padding: 40px;
    border-radius: 28px;
    backdrop-filter: blur(25px);
    box-shadow: 0 0 60px rgba(0,0,0,0.6);
    max-width: 850px;
    margin: auto;
    margin-top: 60px;
    border: 1px solid rgba(255,255,255,0.2);
}

/* ✨ Neon floating title */
.title {
    font-size: 3rem;
    font-weight: 800;
    text-align: center;
    color: #ffffff;
    text-shadow:
        0 0 6px #00ffe1,
        0 0 14px #00ffe1,
        0 0 22px #ff00c8,
        0 0 40px #ff00c8;
    margin-bottom: 10px;
    animation: floatText 4s ease-in-out infinite;
}

@keyframes floatText {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

/* 💬 Chat bubbles */
.user-bubble {
    background: linear-gradient(135deg, #00f5a0, #00d9f5);
    padding: 14px 20px;
    border-radius: 22px 22px 5px 22px;
    color: #003333;
    margin: 12px 0;
    width: fit-content;
    font-weight: 500;
    box-shadow: 0 0 14px rgba(0,255,200,0.7);
}

.ai-bubble {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    padding: 14px 20px;
    border-radius: 22px 22px 22px 5px;
    color: #4a0033;
    margin: 12px 0;
    width: fit-content;
    font-weight: 500;
    box-shadow: 0 0 16px rgba(255,120,180,0.7);
}

/* 🧠 Chat input */
.stChatInput input {
    background: rgba(255,255,255,0.18) !important;
    color: white !important;
    border-radius: 14px !important;
    border: none !important;
    padding: 14px !important;
    font-size: 16px !important;
}

/* 📏 Spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

</style>
""", unsafe_allow_html=True)

# ---------- 🧠 UI ----------
st.markdown('<div class="title">🧠 MindBalance AI</div>', unsafe_allow_html=True)
st.markdown("### 💬 Your AI-powered mental wellness companion 🌱✨")

# 🧹 Reset button
if st.button("🧹 Reset Chat"):
    st.session_state.messages = []
    st.rerun()

# 🧠 Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# 💬 Display chat
for msg in st.session_state.messages:
    if not msg["content"].strip():
        continue

    if msg["role"] == "user":
        st.markdown(f'<div class="user-bubble">🧑‍💬 {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="ai-bubble">🤖 {msg["content"]}</div>', unsafe_allow_html=True)

# 💭 Chat input
user_input = st.chat_input("How are you feeling today? 💭")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("🤖 MindBalance is thinking... 🧠💫"):
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=st.session_state.messages
            )

            ai_reply = response.choices[0].message.content.strip()

            if ai_reply:
                st.session_state.messages.append({"role": "assistant", "content": ai_reply})

            st.rerun()

        except Exception as e:
            st.error(f"⚠️ Groq Error: {e}")
