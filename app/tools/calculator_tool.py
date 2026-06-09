def calculator_tool(expression: str):
    try:
        print("Im here")
        return eval(expression)
    except Exception:
        return "Invalid Expression"