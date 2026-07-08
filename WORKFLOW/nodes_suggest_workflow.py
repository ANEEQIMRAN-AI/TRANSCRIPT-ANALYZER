from typing import TypedDict
from langgraph.graph import StateGraph, END

from UTILS.file_reader import extract_text_from_file
from UTILS.answer_suggester import suggest_answers_from_transcript


# Define the structure of data passed between nodes
class SuggestGraphState(TypedDict):
    file_path: str
    transcript_text: str
    suggested_answers: str


def get_suggest_workflow():
    workflow = StateGraph(SuggestGraphState)

    # Node: extract text from .pdf or .txt
    def extract_node(state: SuggestGraphState) -> SuggestGraphState:
        extracted = extract_text_from_file({"file_path": state["file_path"]})
        return {**state, **extracted}

    # Node: suggest professional answers for each question
    def suggest_node(state: SuggestGraphState) -> SuggestGraphState:
        suggested = suggest_answers_from_transcript({"transcript_text": state["transcript_text"]})
        return {**state, **suggested}

    # Add nodes to the graph
    workflow.add_node("extract_transcript", extract_node)
    workflow.add_node("suggest_answers", suggest_node)

    # Define flow between nodes
    workflow.set_entry_point("extract_transcript")
    workflow.add_edge("extract_transcript", "suggest_answers")
    workflow.add_edge("suggest_answers", END)

    # Compile the workflow
    return workflow.compile()
