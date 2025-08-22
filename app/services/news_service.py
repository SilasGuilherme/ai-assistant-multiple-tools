import os
import requests

def get_latest_news(query: str = "tecnologia") -> str:
    # Lê a chave em runtime para funcionar com monkeypatch.setenv nos testes
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        return "⚠️ API key do NewsAPI não configurada."

    url = "https://newsapi.org/v2/everything"
    params = {"q": query, "apiKey": api_key, "language": "pt"}

    resp = requests.get(url, params=params).json()

    # Não depende de 'status'; usa 'articles' diretamente (compatível com o mock dos testes)
    articles = resp.get("articles", [])
    if not articles:
        return "Nenhuma notícia encontrada."

    headlines = [a.get("title", "").strip() for a in articles[:3] if a.get("title")]
    if not headlines:
        return "Nenhuma notícia encontrada."

    return " | ".join(headlines)
