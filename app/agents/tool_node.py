from app.tools.calculator_tool import calculator_tool

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