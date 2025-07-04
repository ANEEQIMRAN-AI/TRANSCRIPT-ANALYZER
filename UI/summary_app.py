import streamlit as st
import os
import sys

# 🔧 Add root directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from WORKFLOW.nodes_summary_workflows import get_summary_workflow

# Initialize workflow
graph = get_summary_workflow()

# App UI setup
st.set_page_config(page_title="🧠 Interview Transcript Analyzer", layout="centered")
st.title("🧠 Interview Transcript Analyzer")
st.markdown("Upload a `.txt` or `.pdf` file containing a **verbatim interview transcription**. The AI will analyze and provide a summary with key points.")

# Upload section
uploaded_file = st.file_uploader("📄 Upload Transcript File", type=["txt", "pdf"])

if uploaded_file:
    # Save uploaded file to a temporary location
    os.makedirs("temp", exist_ok=True)
    temp_path = os.path.join("temp", uploaded_file.name)

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ File uploaded successfully!")

    if st.button("🔍 Analyze Transcript"):
        with st.spinner("Analyzing using Gemini..."):
            result = graph.invoke({"file_path": temp_path})
            summary = result.get("summary_result", "⚠️ No summary returned.")

        # Output
        st.subheader("📋 Summary & Key Points")
        st.write(summary)
