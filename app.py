import streamlit as st
import base64

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="MindBalance AI", layout="wide")

# ---------- LOAD VIDEO ----------
def get_base64_video(video_file):
    with open(video_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

video_base64 = get_base64_video("earth.mp4")

# ---------- GLOBAL STYLES ----------
st.markdown(
    f"""
    <style>

    /* Background video */
    .video-bg {{
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        z-index: -1;
        opacity: 0.6;
        filter: blur(2px);
    }}

    /* Glass container */
    .glass {{
        background: rgba(255, 255, 255, 0.12);
        padding: 40px;
        border-radius: 25px;
        backdrop-filter: blur(20px);
        box-shadow: 0 0 60px rgba(0,0,0,0.6);
        max-width: 750px;
        margin: auto;
        margin-top: 80px;
    }}

    /* Neon title */
    .title {{
        font-size: 3.2rem;
        font-weight: 800;
        text-align: center;
        color: #ffffff;
        text-shadow:
            0 0 5px #00ffe1,
            0 0 10px #00ffe1,
            0 0 20px #ff00c8,
            0 0 40px #ff00c8;
        margin-bottom: 30px;
        animation: floatText 4s ease-in-out infinite;
    }}

    @keyframes floatText {{
        0% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-10px); }}
        100% {{ transform: translateY(0px); }}
    }}

    /* Subtitle */
    .subtitle {{
        text-align: center;
        color: #e0e0e0;
        margin-bottom: 25px;
        font-size: 1.1rem;
    }}

    /* Input box */
    .stTextInput>div>div>input {{
        background: rgba(255,255,255,0.18);
        color: white;
        border-radius: 14px;
        border: none;
        padding: 14px;
        font-size: 16px;
    }}

    /* Button */
    .stButton button {{
        background: linear-gradient(90deg, #00ffe1, #ff00c8);
        color: white;
        border-radius: 14px;
        padding: 12px 30px;
        border: none;
        font-size: 17px;
        font-weight: 600;
        transition: 0.3s;
        display: block;
        margin: auto;
    }}

    .stButton button:hover {{
        transform: scale(1.08);
        box-shadow: 0 0 25px #00ffe1;
    }}

    /* Result text */
    .result {{
        margin-top: 25px;
        font-size: 1.2rem;
        text-align: center;
        color: #ffffff;
        text-shadow: 0 0 10px #00ffe1;
    }}

    </style>

    <video autoplay loop muted class="video-bg">
        <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
    </video>
    """,
    unsafe_allow_html=True
)

# ---------- GLASS UI ----------
st.markdown('<div class="glass">', unsafe_allow_html=True)

st.markdown('<div class="title">🧠 MindBalance AI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Your AI-powered mental wellness companion</div>',
    unsafe_allow_html=True
)

user_input = st.text_input("How are you feeling today?")

if st.button("Analyze Mood"):
    if user_input:
        # Dummy AI response (replace with your API later)
        response = "✨ You are stronger than you think. Keep going 💙"
        st.markdown(f'<div class="result">{response}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter your feelings first.")

st.markdown('</div>', unsafe_allow_html=True)
