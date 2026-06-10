from app.services.llm_service import LLMService
from langgraph.graph import StateGraph, START, END
#from app.agents.tool_node import calculator_node
#from app.agents.tool_node import text_stats_node
from app.agents.tool_node import tool_node
#from app.agents.router import router
from app.agents.state import AgentState
from app.agents.nodes import reason_node, generate_node, retrieve_node, observe_node
from app.logger import logger
#STATE

#RETRIEVAL NODE
class ResearchAgent:
    def __init__(self, retriever):
        self.retriever = retriever
        self.llm = LLMService()
        graph = StateGraph(AgentState)

        graph.add_node("reason", lambda state:reason_node(state, self.llm))
        graph.add_node("retrieve", lambda state:retrieve_node(state, self.retriever))
        graph.add_node('tool',tool_node)
        graph.add_node('observe', observe_node)
        graph.add_node('generate', lambda state:generate_node(state, self.llm))

        graph.add_edge(START, 'reason')
        graph.add_conditional_edges('reason',
                                    lambda state: state['action'],
                                    {'calculator':'tool',
                                     'text_stats':'tool',
                                     'retrieve':'retrieve',
                                     'generate':'generate'
                                     })
        graph.add_edge('tool', 'observe')
        graph.add_edge('observe', 'reason')
        graph.add_edge('retrieve', 'generate')
        graph.add_edge('generate', END)
        self.agent = graph.compile()
    
    def invoke(self,question:str):
        #print("Invoking response...")
        logger.info("Invoking Agent")
        #response = self.agent.invoke({"question":question})
        response = self.agent.invoke({'question': question,
                                      'iterations':0,
                                      'tool_history': []})
        return response["answer"]