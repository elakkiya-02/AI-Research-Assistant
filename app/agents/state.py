from typing import TypedDict

class AgentState(TypedDict):
    question: str
    context: str
    answer: str
    action: str
    observation: str
    iterations: int
    tool_history: list
