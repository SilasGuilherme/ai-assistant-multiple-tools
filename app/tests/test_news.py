import pytest
from app.services.news_service import get_latest_news

def test_news_without_api_key(monkeypatch):
    monkeypatch.setenv("NEWS_API_KEY", "")
    response = get_latest_news("technology")
    assert "não configurada" in response.lower()

def test_news_with_mock(monkeypatch):
    def mock_requests_get(url, params):
        class MockResponse:
            def json(self):
                return {
                    "articles": [
                        {"title": "Notícia 1"},
                        {"title": "Notícia 2"}
                    ]
                }
        return MockResponse()

    import app.services.news_service as news_service
    monkeypatch.setattr(news_service.requests, "get", mock_requests_get)

    monkeypatch.setenv("NEWS_API_KEY", "fake_key")
    response = get_latest_news("technology")

    assert "Notícia 1" in response
    assert "Notícia 2" in response
