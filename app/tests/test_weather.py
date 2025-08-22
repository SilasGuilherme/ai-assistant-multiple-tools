import pytest
from app.services.weather_service import get_weather

def test_weather_without_api_key(monkeypatch):
    monkeypatch.setenv("OPENWEATHER_API_KEY", "")
    response = get_weather("São Paulo")
    assert "não configurada" in response.lower()

def test_weather_with_mock(monkeypatch):
    def mock_requests_get(url, params):
        class MockResponse:
            def json(self):
                return {
                    "main": {"temp": 25},
                    "weather": [{"description": "céu limpo"}]
                }
        return MockResponse()

    import app.services.weather_service as weather_service
    monkeypatch.setattr(weather_service.requests, "get", mock_requests_get)

    monkeypatch.setenv("OPENWEATHER_API_KEY", "fake_key")
    response = get_weather("São Paulo")

    assert "25" in response
    assert "céu limpo" in response
