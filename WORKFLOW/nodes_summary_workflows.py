from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from typing import TypedDict, Optional

from UTILS.file_reader import extract_text_from_file
from UTILS.summarizer import summarize_transcript

# 🧠 Define the state that flows between nodes
class SummaryState(TypedDict):
    file_path: str
    transcript_text: Optional[str]
    summary_result: Optional[str]

def get_summary_workflow():
    graph = StateGraph(SummaryState)  # define the graph with this state

    # 🧩 Add nodes
    graph.add_node("read_file", RunnableLambda(extract_text_from_file))
    graph.add_node("summarize", RunnableLambda(summarize_transcript))

    # 🔁 Define flow between nodes
    graph.set_entry_point("read_file")
    graph.add_edge("read_file", "summarize")
    graph.add_edge("summarize", END)

    # ✅ Compile and return the runnable graph
    return graph.compile()
