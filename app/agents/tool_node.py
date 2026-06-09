from app.tools.tool_registry import TOOLS

def tool_node(state):
    action = state['action']
    tool = TOOLS[action]
    question = state['question']
    if action =='text_stats':
        question = question.replace("count words", "")
    result = tool(question)
    history = state['tool_history']
    history.append(f'{action} -> {result}')
    return {'observation': str(result),
            'tool_history':history}

#COMMENTING AS WE HAVE TOOL REGISTRY NOW
"""from app.tools.calculator_tool import calculator_tool
from app.tools.text_stats_tool import text_stats_tool

def calculator_node(state):
    history = state['tool_history']
    print("Calling Calculator tool from calculator node...")
    result = calculator_tool(state['question'])
    print("RESULT: ", result)
    history.append(f'calculator -> {result}')
    #return {'context':f"calculator result: {result}"}
    #OBSERVATION
    return {'observation':f"calculator result: {result}",
            'tool_history':history}

def text_stats_node(state):
    history=state['history']
    print("Calling Text Stats tool from text_Stats_node...")
    result = text_stats_tool(state['question'])
    history.append(f'text_stats -> {result}')
    return {'observation':f'text stats result: {result}',
            'tool_history':history}"""

