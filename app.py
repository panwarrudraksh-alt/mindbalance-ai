import streamlit as st
import base64
import os
from openai import OpenAI

st.set_page_config(page_title="MindBalance AI", layout="centered")

# ---------- LOAD API ----------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ---------- SAFE VIDEO BACKGROUND ----------
def get_base64_video(video_file):
    if os.path.exists(video_file):
        with open(video_file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

video_base64 = get_base64_video("earth.mp4")

if video_base64:
    st.markdown(f"""
    <style>
    .stApp {{ background: transparent; }}
    video {{
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        z-index: -10;
        object-fit: cover;
        filter: brightness(0.45) saturate(1.2);
    }}
    </style>

    <video autoplay muted loop>
        <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
    </video>
    """, unsafe_allow_html=True)

# ---------- CSS ----------
st.markdown("""
<style>

/* REMOVE ALL DEFAULT BACKGROUNDS */
.main, .block-container, header, footer {
    background: transparent !important;
}

/* KILL GRAY BAR FOREVER */
[data-testid="stDecoration"], .st-emotion-cache-18ni7ap {
    display: none !important;
}

/* GLASS CARD */
.glass-card {
    background: rgba(255, 255, 255, 0.08);
    padding: 35px;
    border-radius: 22px;
    backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.18);
    box-shadow: 0 0 35px rgba(0,255,255,0.25);
    margin-top: 40px;
}

/* TITLE */
.title {
    text-align: center;
    font-size: 46px;
    font-weight: 800;
    background: linear-gradient(90deg, #00f5ff, #ff00e6, #00ff88);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* CHAT BUBBLES */
.user-bubble {
    background: linear-gradient(90deg, #00f5ff, #0099ff);
    padding: 12px;
    border-radius: 14px;
    margin: 8px 0;
    color: white;
    text-align: right;
}

.bot-bubble {
    background: rgba(255,255,255,0.12);
    padding: 12px;
    border-radius: 14px;
    margin: 8px 0;
    color: #ffffff;
    text-align: left;
}

/* BUTTON */
.stButton > button {
    width: 100%;
    border-radius: 14px;
    background: linear-gradient(90deg, #00f5ff, #ff00e6);
    color: white;
    font-weight: bold;
    border: none;
    padding: 12px;
}

textarea {
    background: rgba(0,0,0,0.35) !important;
    color: white !important;
    border-radius: 12px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------- SESSION MEMORY ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- UI ----------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<div class="title">🧠 MindBalance AI</div>', unsafe_allow_html=True)

# DISPLAY CHAT HISTORY
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-bubble">🧑 {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-bubble">🤖 {msg["content"]}</div>', unsafe_allow_html=True)

# INPUT
user_input = st.text_area("💭 Share your thoughts...", height=100)

if st.button("✨ Send"):
    if user_input.strip() != "":
        # SAVE USER MESSAGE
        st.session_state.messages.append({"role": "user", "content": user_input})

        # GET AI RESPONSE
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages
        )

        bot_reply = response.choices[0].message.content

        # SAVE BOT MESSAGE
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})

        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
