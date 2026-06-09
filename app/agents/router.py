def router(state):
    question=state['question']
    operators = ["+","-","*", "/"]
    if any(op in question for op in operators):
        print("-> calculator")
        return "calculator"
    
    print("-> retrieve")
    return "retrieve"