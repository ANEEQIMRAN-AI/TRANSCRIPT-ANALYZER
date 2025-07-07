# 🧠 Transcript Intelligence Suite

An AI-powered suite of tools that transforms raw interview or meeting transcripts into actionable intelligence. Powered by [LangGraph](https://github.com/langchain-ai/langgraph), Google Gemini, and Streamlit, this modular platform enables question extraction, answer suggestion, and executive summary generation — all from verbatim `.txt` or `.pdf` transcripts.

---

## 🚀 Features

### 🔍 1. Q&A Extractor
Extracts every question and its exact corresponding answer from the transcript without **any modification** — punctuation, grammar, or wording remains 100% original.

### 💡 2. Suggested Answer Generator
For each extracted question, this tool suggests **two professional answers** based on typical interview expectations — useful for coaching, training, and model fine-tuning.

### 📋 3. Executive Summary Generator
Generates a nuanced, executive-level analysis of the candidate’s **technical skills, leadership potential, communication style,** and **hiring fit** — ideal for HR/talent intelligence workflows.

---

## 📁 Project Structure

TRANSCRIPT_SUITE/
├── main_app.py # Central dashboard for tool selection
├── LLM.py # Gemini model configuration
│
├── PROMPTS/ # All reusable prompt templates
│ ├── qa_prompt.py
│ ├── suggest_prompt.py
│ └── summary_prompt.py
│
├── UTILS/ # Logic for each agent
│ ├── file_reader.py
│ ├── qa_extractor.py
│ ├── answer_suggester.py
│ └── summary_generator.py
│
├── WORKFLOW/ # LangGraph state machines
│ ├── nodes_qa_workflow.py
│ ├── nodes_suggest_workflow.py
│ └── nodes_summary_workflow.py
│
├── UI/ # Streamlit UIs for each module
│ ├── qa_app.py
│ ├── suggest_app.py
│ └── summary_app.py
│
├── temp_uploads/ # Temporary upload storage
├── .env # Your GEMINI_API_KEY goes here
├── requirements.txt # Python dependencies
└── README.md



---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/transcript-intelligence-suite.git
cd transcript-intelligence-suite
```

## Create virtual environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

## Install dependencies

pip install -r requirements.txt

## Add your Gemini API Key

GEMINI_API_KEY=your_google_api_key_here

## 🧪 Running the App

streamlit run main_app.py

You’ll be greeted with a dashboard that allows you to:

📄 Upload a transcript (.txt or .pdf)

🛠 Select which AI tool to run

✅ Get extracted Q&A, suggested answers, or executive summary


## 🛠 Tech Stack

LangGraph (stateful AI flows)

LangChain

Streamlit (UI framework)

Google Gemini Pro

PyMuPDF (for parsing PDFs)


## 🤖 Use Cases

Technical hiring and talent evaluation

Interview coaching and preparation

Conversational data structuring

LLM tuning dataset generation

Automated meeting analysis

## 🧑‍💻 Author

📫 aneeqimran.ai@gmail.com
