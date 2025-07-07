# File: PROMPTS/qa_prompt.py

from langchain_core.prompts import ChatPromptTemplate

qa_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are provided with a verbatim transcript of a conversation, interview, or meeting.

Your task is to extract every question and its directly corresponding answer, strictly as they appear in the text, without introducing any modifications, rephrasings, interpretations, or additional punctuation — not even a full stop, comma, or formatting change.

🔒 Rules you must strictly follow:
- Do not paraphrase or alter the language in any way
- Do not complete or infer incomplete sentences
- Do not add or remove punctuation, even if it appears to be missing
- Do not include any explanations or commentary
- Do not skip or merge any question-answer pairs

✅ Format your output precisely as follows:
Q: [Exact question from transcript]
A: [Exact corresponding answer from transcript]

Repeat this format for every valid question-and-answer pair found in the transcript.

Your output must be purely extractive and 100% faithful to the original wording in the transcript. Treat this as a legal or compliance-level task."""
    ),
    (
        "human",
        """Transcript:
{transcript_text}

Extract all question-answer pairs."""
    )
])
