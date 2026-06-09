from app.tools.calculator_tool import calculator_tool

def calculator_node(state):
    print("Calling Calculator tool from calculator node...")
    result = calculator_tool(state['question'])
    print("RESULT: ", result)
    return {'context':f"calculator result: {result}"}