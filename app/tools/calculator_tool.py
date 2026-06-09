def calculator_tool(expression: str):
    try:
        print("In calculator tool")
        return eval(expression)
    except Exception:
        return "Invalid Expression"