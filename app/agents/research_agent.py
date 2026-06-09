from typing import TypedDict
from app.services.llm_service import LLMService
from langgraph.graph import StateGraph, START, END
from app.rag.prompt_template import RAG_PROMPT
from app.agents.tool_node import calculator_node
from app.agents.router import router

#STATE
class AgentState(TypedDict):
    question: str
    context: str
    answer: str
    action: str
#RETRIEVAL NODE
class ResearchAgent:
    def __init__(self, retriever):
        self.retriever = retriever
        self.llm = LLMService()
        graph = StateGraph(AgentState)

        graph.add_node("retrieve", self.retrieve_node)
        graph.add_node("generate", self.generate_node)
        graph.add_node("reason", self.reason_node)
        #graph.add_edge(START, "retrieve")
        graph.add_node("calculator", calculator_node)
        graph.add_edge(START, 'reason')
        graph.add_conditional_edges("reason",
                                    lambda state:state['action'],
                                    {'calculator':'calculator',
                                    'retrieve':'retrieve'})
        
        graph.add_edge('retrieve', 'generate') #edge for node 'retrieve'
        graph.add_edge('calculator', 'generate') #edge for node 'calculator'
        graph.add_edge("generate", END) #edge for node 'generate'. will END here
        self.agent = graph.compile()

    def retrieve_node(self, state:AgentState):
        print("At retrieve node...")
        docs = self.retriever.retrieve(state["question"])
        context = "\n\n".join(doc.page_content for doc in docs)
        return {"context": context}
    
    def generate_node(self, state:AgentState):
        print("At generate node...")
        prompt = RAG_PROMPT.format(context=state["context"],
                                   question=state["question"])
        answer = self.llm.generate_response(prompt)
        return{"answer":answer}
    
    def invoke(self,question:str):
        print("Invoking response...")
        response = self.agent.invoke({"question":question})
        return response["answer"]
    
    def reason_node(self, state):
        print("At reason node...")
        question = state['question']
        operators = ["+", "-","*","/"]
        if any (op in question for op in operators):
            action = "calculator"
        else:
            action ="retrieve"
        print("Action = ", action)
        return{"action" :  action}


