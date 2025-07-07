from PROMPTS.suggest_prompt import suggest_prompt
from LLM import llm

def suggest_answers_from_transcript(input_dict: dict) -> dict:
    transcript_text = input_dict.get("transcript_text")
    if not transcript_text:
        raise ValueError("Transcript text is missing.")

    chain = suggest_prompt | llm
    response = chain.invoke({"transcript_text": transcript_text})

    return {"suggested_answers": response.content}
