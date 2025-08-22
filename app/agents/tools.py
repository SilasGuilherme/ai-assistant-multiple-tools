from langchain.agents import Tool
from app.services.math_service import calculate_expression
from app.services.weather_service import get_weather
from app.services.news_service import get_latest_news


def calculadora_wrapper(expr: str) -> str:
    """Wrapper para garantir retorno em string."""
    result = calculate_expression(expr)
    return str(result)


def clima_wrapper(city: str) -> str:
    """Wrapper para garantir retorno em string."""
    result = get_weather(city)
    return str(result)


def noticias_wrapper(query: str = "") -> str:
    """Wrapper para garantir retorno em string."""
    result = get_latest_news(query)
    return str(result)


tools = [
    Tool(
        name="Calculadora",
        func=calculadora_wrapper,
        description=(
            "Resolve cálculos matemáticos. "
            "Aceita apenas expressões no formato Python, como '2 + 2', 'sqrt(144)', '10 * (5 + 3)'. "
            "Use sqrt(x) para raízes quadradas."
        ),
    ),
    Tool(
        name="Clima",
        func=clima_wrapper,
        description="Obtém informações do clima para uma cidade informada.",
    ),
    Tool(
        name="Notícias",
        func=noticias_wrapper,
        description="Obtém as últimas notícias com base em uma busca.",
    ),
]
