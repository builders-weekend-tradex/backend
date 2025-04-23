from unittest.mock import patch
from utils.tech_analysis.tech_analysis import tech_analysis

@patch("utils.tech_analysis.tech_analysis.yf.download")
@patch("utils.tech_analysis.tech_analysis.pd.read_pickle")
def test_tech_analysis_returns_expected_keys(mock_read_pickle, mock_download, mock_yfinance_dataframe):
    mock_download.return_value = mock_yfinance_dataframe
    mock_read_pickle.return_value = mock_yfinance_dataframe

    charts, text = tech_analysis("GOOG")

    expected_keys = [
        "price_trend", "on_balance_volume_chart", "macd", "rsi",
        "bollinger_bands_plot", "stochastic_oscillator_plot",
        "williams_r_plot", "adx_plot", "cmf", "backtesting"
    ]

    for key in expected_keys:
        assert key in charts, f"Missing chart: {key}"
    assert isinstance(text, str)
