# File: WORKFLOW/nodes_qa_workflow.py

from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_core.runnables import RunnableLambda
from UTILS.qa_extractor import extract_qa_from_transcript
from UTILS.file_reader import extract_text_from_file

# Define the graph

def get_qa_workflow():
    # Define the state schema
    class State(dict):
        file_path: str
        transcript_text: str
        qa_output: str

    # Node: Read transcript from file
    def load_transcript(state: State):
        result = extract_text_from_file({"file_path": state["file_path"]})
        state["transcript_text"] = result["transcript_text"]
        return state

    # Node: Extract Q&A using LLM
    def qa_node(state: State):
        result = extract_qa_from_transcript({"transcript_text": state["transcript_text"]})
        state["qa_output"] = result["qa_output"]
        return state

    # Build the graph
    builder = StateGraph(State)
    builder.add_node("load_transcript", RunnableLambda(load_transcript))
    builder.add_node("extract_qa", RunnableLambda(qa_node))

    builder.set_entry_point("load_transcript")
    builder.add_edge("load_transcript", "extract_qa")
    builder.add_edge("extract_qa", END)

    return builder.compile()
