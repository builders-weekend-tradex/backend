import pytest
from unittest.mock import MagicMock
import pandas as pd
from datetime import datetime

# ---------- Lexi Fixture ----------
@pytest.fixture
def mock_lexi_response():
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="Hello from Lexi"))]
    return mock_response

# ---------- Social Analysis Fixtures ----------
@pytest.fixture
def mock_news_articles_tech():
    return {
        "articles": [
            {
                "title": "Big Tech News",
                "publishedAt": "2024-04-10T12:00:00Z",
                "url": "https://example.com/article1"
            }
        ]
    }

@pytest.fixture
def mock_news_articles_ai():
    return {
        "articles": [
            {
                "title": "AI Expansion",
                "publishedAt": "2024-04-09T09:00:00Z",
                "url": "https://example.com/article2"
            }
        ]
    }

# ---------- Technical Analysis Fixture ----------
@pytest.fixture
def mock_yfinance_dataframe():
    columns = pd.MultiIndex.from_tuples([
        ("Open", ""), ("High", ""), ("Low", ""), ("Close", ""), ("Volume", "")
    ])
    data = [[100, 105, 98, 102, 1000000]] * 120
    index = pd.date_range(end=datetime.today(), periods=120)
    df = pd.DataFrame(data, columns=columns, index=index)
    df.index.name = "Date"
    return df
