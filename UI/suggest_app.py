def render():
    import os
    import streamlit as st
    import sys

    # 🔧 Add root directory to Python path
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    from WORKFLOW.nodes_suggest_workflow import get_suggest_workflow

    # Configure Streamlit page
    st.set_page_config(page_title="💡 Suggested Interview Answers Generator", layout="wide")
    st.title("💬 AI-Suggested Answers from Transcript")

    # Upload Section
    uploaded_file = st.file_uploader("📤 Upload Interview Transcript (.pdf or .txt)", type=["pdf", "txt"])

    if uploaded_file:
        # Save uploaded file temporarily
        os.makedirs("temp_uploads", exist_ok=True)
        file_path = os.path.join("temp_uploads", uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        # Run Workflow
        with st.spinner("🧠 Analyzing transcript and generating suggested answers..."):
            app = get_suggest_workflow()
            output = app.invoke({"file_path": file_path})

        # Output
        st.subheader("📋 Suggested Answers")
        st.code(output["suggested_answers"], language="markdown")
