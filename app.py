import streamlit as st
import base64
import os

st.set_page_config(page_title="MindBalance AI", layout="centered")

# ---------- SAFE VIDEO BACKGROUND ----------
def get_base64_video(video_file):
    if os.path.exists(video_file):
        with open(video_file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

video_base64 = get_base64_video("earth.mp4")

if video_base64:
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: transparent;
        }}

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
        """,
        unsafe_allow_html=True
    )

# ---------- GLOBAL CSS ----------
st.markdown("""
<style>

/* REMOVE STREAMLIT DEFAULT BACKGROUND */
.main, .block-container {
    background: transparent !important;
}

/* GLASS CARD */
.glass-card {
    background: rgba(255, 255, 255, 0.08);
    padding: 35px;
    border-radius: 22px;
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.18);
    box-shadow: 0 0 35px rgba(0,255,255,0.25);
    margin-top: 60px;
}

/* TITLE NEON */
.title {
    text-align: center;
    font-size: 46px;
    font-weight: 800;
    background: linear-gradient(90deg, #00f5ff, #ff00e6, #00ff88);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glow 3s ease-in-out infinite alternate;
}

/* SUBTITLE */
.subtitle {
    text-align: center;
    color: #e0e0e0;
    font-size: 18px;
    margin-bottom: 30px;
}

/* BUTTON STYLE */
.stButton > button {
    width: 100%;
    border-radius: 14px;
    background: linear-gradient(90deg, #00f5ff, #ff00e6);
    color: white;
    font-weight: bold;
    border: none;
    padding: 12px;
    box-shadow: 0 0 15px rgba(255, 0, 230, 0.6);
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 25px rgba(0, 255, 255, 0.9);
}

/* INPUT BOX */
textarea, .stTextInput input {
    background: rgba(0,0,0,0.35) !important;
    color: white !important;
    border-radius: 12px !important;
}

/* FLOATING NEON PARTICLES */
.particle {
    position: fixed;
    width: 6px;
    height: 6px;
    background: cyan;
    border-radius: 50%;
    box-top: 0;
    animation: floatUp 12s linear infinite;
    opacity: 0.7;
}

@keyframes floatUp {
    from {
        transform: translateY(100vh) scale(0.5);
        opacity: 0;
    }
    to {
        transform: translateY(-10vh) scale(1.2);
        opacity: 1;
    }
}

/* GLOW ANIMATION */
@keyframes glow {
    from { text-shadow: 0 0 12px #00f5ff; }
    to { text-shadow: 0 0 25px #ff00e6; }
}

/* REMOVE GRAY BAR */
.glass { display: none !important; }

</style>

<!-- PARTICLES -->
<div class="particle" style="left:10%; animation-delay:0s;"></div>
<div class="particle" style="left:25%; animation-delay:2s;"></div>
<div class="particle" style="left:40%; animation-delay:4s;"></div>
<div class="particle" style="left:60%; animation-delay:1s;"></div>
<div class="particle" style="left:75%; animation-delay:3s;"></div>
<div class="particle" style="left:90%; animation-delay:5s;"></div>
""", unsafe_allow_html=True)

# ---------- GLASS UI ----------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.markdown('<div class="title">🧠 MindBalance AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your AI Mental Wellness Companion 🌌💬</div>', unsafe_allow_html=True)

user_input = st.text_area("💭 How are you feeling today?", height=120)

if st.button("✨ Get Support"):
    if user_input.strip() == "":
        st.warning("Please share something so I can help 🤗")
    else:
        st.success("You're not alone 💙 I'm here for you.")
        st.write("🪷 Take a deep breath… Inhale… Exhale…")
        st.write("🌟 Remember: You are stronger than you think.")

st.markdown("</div>", unsafe_allow_html=True)
