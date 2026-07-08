import streamlit as st
from UI import qa_app, suggest_app, summary_app

# Streamlit page config
st.set_page_config(page_title="🎛️ Transcript Intelligence Suite", layout="wide")

# Custom page style
st.markdown("""
    <style>
    .app-title {
        font-size: 36px;
        font-weight: bold;
        color: #4CAF50;
    }
    .sub-title {
        font-size: 20px;
        margin-bottom: 20px;
    }
    .option-button {
        font-size: 18px !important;
        padding: 0.75em 1.5em !important;
        margin: 0.5em;
        border-radius: 12px !important;
        background-color: #f0f2f6;
        border: 1px solid #ddd;
    }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown("<div class='app-title'>🧠 Transcript Intelligence Suite</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Select a tool to begin analyzing your transcript:</div>", unsafe_allow_html=True)

# Tool Selection
tool = st.selectbox("🔧 Choose a Transcript Tool", [
    "Q&A Extractor",
    "Suggested Answer Generator",
    "Executive Interview Summary"
], index=0)

# Spacer
st.markdown("---")

# Conditional UI Load
if tool == "Q&A Extractor":
    qa_app.render()
elif tool == "Suggested Answer Generator":
    suggest_app.render()
elif tool == "Executive Interview Summary":
    summary_app.render()
