import os
import requests

def get_weather(city: str) -> str:
    # Lê a chave em runtime para os testes com monkeypatch funcionarem
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "⚠️ API key do OpenWeather não configurada."

    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "lang": "pt", "units": "metric"}

    resp = requests.get(url, params=params).json()

    if "main" not in resp or "weather" not in resp:
        return "Erro ao buscar clima."

    temp = resp["main"].get("temp")
    description = resp["weather"][0].get("description", "")

    return f"O clima em {city} é {description}, temperatura {temp}°C."
