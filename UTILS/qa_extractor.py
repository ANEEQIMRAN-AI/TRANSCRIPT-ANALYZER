# File: UTILS/qa_extractor.py

from PROMPTS.qa_prompt import qa_prompt
from LLM import llm

def extract_qa_from_transcript(input_dict: dict) -> dict:
    transcript_text = input_dict.get("transcript_text")
    if not transcript_text:
        raise ValueError("Transcript text is missing.")

    chain = qa_prompt | llm
    response = chain.invoke({"transcript_text": transcript_text})

    return {"qa_output": response.content}
