from unittest.mock import patch, MagicMock
from utils.lexi import lexi_chat

@patch("utils.lexi.client.chat.completions.create")
def test_lexi_chat_success(mock_create):
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="Hello from Lexi"))]
    mock_create.return_value = mock_response

    result = lexi_chat("Hello?")
    assert result == "Hello from Lexi"

@patch("utils.lexi.client.chat.completions.create")
def test_lexi_chat_failure(mock_create):
    mock_create.side_effect = Exception("API Error")

    result = lexi_chat("Hi")
    assert result == "API Error"