from unittest.mock import patch, MagicMock
from utils.social_analysis.news_feed import get_news

@patch("utils.social_analysis.news_feed.newsapi.get_everything")
def test_get_news_with_mapping(mock_get_everything):
    mock_get_everything.return_value = {
        "articles": [
            {
                "title": "Big Tech News",
                "publishedAt": "2024-04-10T12:00:00Z",
                "url": "https://example.com/article1"
            }
        ]
    }

    result = get_news("GOOG")  # Should map to "GOOGLE"
    
    assert isinstance(result, list)
    assert result[0]["title"] == "Big Tech News"
    assert result[0]["url"] == "https://example.com/article1"

@patch("utils.social_analysis.news_feed.newsapi.get_everything")
def test_get_news_without_mapping(mock_get_everything):
    mock_get_everything.return_value = {
        "articles": [
            {
                "title": "AI Expansion",
                "publishedAt": "2024-04-09T09:00:00Z",
                "url": "https://example.com/article2"
            }
        ]
    }

    result = get_news("OpenAI")

    assert len(result) == 1
    assert result[0]["title"] == "AI Expansion"
