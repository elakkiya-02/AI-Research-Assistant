def calculator_tool(expression: str):
    try:
        print("In calculator toll")
        return eval(expression)
    except Exception:
        return "Invalid Expression"