from unittest.mock import patch
from utils.social_analysis.news_feed import get_news

@patch("utils.social_analysis.news_feed.newsapi.get_everything")
def test_get_news_with_mapping(mock_get_everything, mock_news_articles_tech):
    mock_get_everything.return_value = mock_news_articles_tech
    result = get_news("GOOG")
    assert result[0]["title"] == "Big Tech News"

@patch("utils.social_analysis.news_feed.newsapi.get_everything")
def test_get_news_without_mapping(mock_get_everything, mock_news_articles_ai):
    mock_get_everything.return_value = mock_news_articles_ai
    result = get_news("OpenAI")
    assert result[0]["title"] == "AI Expansion"
