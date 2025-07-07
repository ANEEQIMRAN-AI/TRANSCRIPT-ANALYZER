# File: UI/qa_app.py

import streamlit as st
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from WORKFLOW.nodes_qa_workflow import get_qa_workflow




# 🔧 Add root directory to Python path


st.set_page_config(page_title="Interview Q&A Extractor", layout="wide")
st.title("📄 Interview Q&A Extractor")

uploaded_file = st.file_uploader("Upload Transcript (.pdf or .txt)", type=["pdf", "txt"])

if uploaded_file is not None:
    with st.spinner("Processing transcript..."):
        # Save the file temporarily
        temp_file_path = os.path.join("temp_transcript." + uploaded_file.name.split(".")[-1])
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.read())

        # Prepare state
        workflow = get_qa_workflow()
        result = workflow.invoke({"file_path": temp_file_path})

        if "qa_output" in result:
            st.subheader("🧠 Extracted Q&A Pairs")
            st.text_area("Output", result["qa_output"], height=600)
        else:
            st.error("❌ Failed to extract Q&A pairs from transcript.")
