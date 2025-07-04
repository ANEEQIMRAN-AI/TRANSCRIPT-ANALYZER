from LLM import llm  # Import LLM from shared file
from PROMPTS.summary_prompts import summary_prompt
from TOOLS.summary_tools import clean_transcript

def summarize_transcript(inputs: dict) -> dict:
    """
    Runs transcript cleaning and then passes the cleaned transcript to Gemini via LangChain.
    """
    # Step 1: Extract transcript text
    raw_text = inputs.get("transcript_text", "")

    # Step 2: Clean the transcript
    cleaned_text = clean_transcript(raw_text)

    # Step 3: Use the prompt + LLM pipeline
    chain = summary_prompt | llm
    result = chain.invoke({"transcript_text": cleaned_text})

    # Step 4: Return result
    return {"summary_result": result.content}
