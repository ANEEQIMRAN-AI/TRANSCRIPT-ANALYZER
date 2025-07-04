import re

def clean_transcript(text: str) -> str:
    """
    Cleans the raw transcript by removing timestamps and common filler words.
    """
    # Remove timestamps like [00:03:12]
    text = re.sub(r"\[\d{2}:\d{2}:\d{2}\]", "", text)

    # Remove common filler words (optional, expand as needed)
    fillers = r"\b(um|uh|you know|like|I mean|so|well|hmm)\b"
    text = re.sub(fillers, "", text, flags=re.IGNORECASE)

    # Remove extra spaces or blank lines
    text = re.sub(r"\s{2,}", " ", text)
    text = re.sub(r"\n{2,}", "\n", text)

    return text.strip()
