from app.rag.prompt_template import RAG_PROMPT
from app.agents.reason_prompt import REASON_PROMPT

allowed_actions = {'calculator', 'text_stats',
                   'retrieve','generate'}

def reason_node(state,llm):
        print("At reason node...")
        print("This Iteration : ", state['iterations'])
        """#RULE BASED REASONING
        if state['iterations']>=1:
            action='generate'
        else:
            question = state['question']
            operators = ["+", "-","*","/"]
            if question.lower().startswith('count words'):
                action='text_stats'
            elif any (op in question for op in operators):
                action = "calculator"
            else:
                action ='retrieve'"""
        prompt = REASON_PROMPT.format(question=state['question'])
        action = llm.generate_response(prompt).strip().lower()
        if action not in allowed_actions:
            action='retrieve'
        print("Action = ", action)
        return{"action" :  action}
    
def retrieve_node(state, retriever):
    print("At retrieve node...")
    docs = retriever.retrieve(state["question"])
    context = "\n\n".join(doc.page_content for doc in docs)
    return {"context": context}

def observe_node(state):
    print("At Observation node...")
    #converts the observation from the calculator tool to context
    return {'context': state['observation'],
            'iterations': state['iterations'] + 1}

def generate_node(state,llm):
    print("At generate node...")
    prompt = RAG_PROMPT.format(context=state["context"],
                                question=state["question"])
    answer = llm.generate_response(prompt)
    return{"answer":answer}