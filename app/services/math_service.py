import math

def calculate_expression(expression: str) -> str:
    """
    Avalia expressões matemáticas básicas de forma segura.
    Exemplo: "2 + 2", "sqrt(144)", "10 * (5 + 3)".
    """

    try:
        # Dicionário seguro com apenas funções matemáticas
        safe_dict = {
            "sqrt": math.sqrt,
            "log": math.log,
            "pow": math.pow,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "pi": math.pi,
            "e": math.e,
        }

        # Usa eval apenas com o dicionário seguro
        result = eval(expression, {"__builtins__": None}, safe_dict)

        return str(result)

    except Exception as e:
        return f"Erro ao calcular: {str(e)}"
