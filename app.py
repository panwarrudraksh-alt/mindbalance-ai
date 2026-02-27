import streamlit as st
from groq import Groq

# 🔑 Load API key from Streamlit Secrets
api_key = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=api_key)

st.set_page_config(page_title="MindBalance AI", layout="wide")

# 🌍 GLASS + EARTH BACKGROUND + GRAVITY PARTICLES
st.markdown("""
<style>

/* 🌍 Earth video background */
video#earth-bg {
    position: fixed;
    right: 0;
    bottom: 0;
    min-width: 100%;
    min-height: 100%;
    object-fit: cover;
    z-index: -2;
    filter: brightness(0.45) blur(2px);
}

/* 🌫 Glass overlay */
.glass-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(10, 15, 25, 0.45);
    backdrop-filter: blur(6px);
    z-index: -1;
}

/* 🪐 Gravity particles */
.particle {
    position: fixed;
    width: 8px;
    height: 8px;
    background: rgba(255,255,255,0.7);
    border-radius: 50%;
    animation: gravity 12s infinite linear;
}

@keyframes gravity {
    0% { transform: translateY(-10vh) translateX(0); opacity: 0; }
    10% { opacity: 0.8; }
    100% { transform: translateY(110vh) translateX(50px); opacity: 0; }
}

/* 💎 Glass chat container */
.chat-container {
    max-width: 850px;
    margin: auto;
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(25px);
    padding: 35px;
    border-radius: 30px;
    box-shadow: 0 0 40px rgba(0,0,0,0.6);
    border: 1px solid rgba(255,255,255,0.2);
}

/* 💬 User bubble */
.user-bubble {
    background: linear-gradient(135deg, #00f5a0, #00d9f5);
    padding: 14px 20px;
    border-radius: 25px 25px 5px 25px;
    color: #003333;
    margin: 12px 0;
    width: fit-content;
    font-weight: 500;
    box-shadow: 0 0 12px rgba(0,255,200,0.6);
}

/* 🤖 AI bubble */
.ai-bubble {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    padding: 14px 20px;
    border-radius: 25px 25px 25px 5px;
    color: #4a0033;
    margin: 12px 0;
    width: fit-content;
    font-weight: 500;
    box-shadow: 0 0 14px rgba(255,100,150,0.6);
}

/* 🧠 Title */
h1 {
    text-align: center;
    font-weight: 800;
    font-size: 2.6rem;
    color: white;
    margin-bottom: 25px;
}

/* ✨ Input bar */
.stChatInput input {
    border-radius: 25px !important;
    border: 1px solid rgba(255,255,255,0.3) !important;
    padding: 14px !important;
    background: rgba(255,255,255,0.15) !important;
    color: white !important;
}

/* 📏 Better spacing */
.block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
}

</style>

<!-- 🌍 Earth background video -->
<video autoplay muted loop id="earth-bg">
  <source src="https://cdn.coverr.co/videos/coverr-earth-rotation-5176/1080p.mp4" type="video/mp4">
</video>

<div class="glass-overlay"></div>

<!-- 🪐 Gravity particles -->
<div class="particle" style="left:10%; animation-duration:10s;"></div>
<div class="particle" style="left:25%; animation-duration:14s;"></div>
<div class="particle" style="left:40%; animation-duration:12s;"></div>
<div class="particle" style="left:60%; animation-duration:16s;"></div>
<div class="particle" style="left:75%; animation-duration:11s;"></div>
<div class="particle" style="left:90%; animation-duration:15s;"></div>

""", unsafe_allow_html=True)

st.title("🧠 MindBalance AI")

st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# 🧠 Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# 💬 Display chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-bubble">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="ai-bubble">{msg["content"]}</div>', unsafe_allow_html=True)

# ✅ Chat input (no loop)
user_input = st.chat_input("How are you feeling today?")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=st.session_state.messages
        )

        ai_reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": ai_reply})

        st.rerun()

    except Exception as e:
        st.error(f"Groq Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)
