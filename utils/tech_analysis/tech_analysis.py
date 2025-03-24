import os
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import pandas_ta as ta
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from utils.lexi import lexi_chat

import plotly.tools as tls
import plotly.io as pio

from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA

from bokeh.embed import file_html
from bokeh.resources import CDN

matplotlib.use("Agg")

TICKER_SYMBOL = 'GOOG'

# Define the folder where the files will be stored
output_folder = "utils/tech_analysis/outputs"

def tech_analysis(symbol):
        # Define the stock timeframe
        end_date = datetime.today()
        start_date = end_date - timedelta(days=120)  # 4 months before today
        # Fetch stock data using yfinance
        ### TO BE COMMENTED START
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        pd.to_pickle(stock_data, os.path.join(output_folder, "stock_data.pkl"))
        ### TO BE COMMENTED END

        stock_data = pd.read_pickle(os.path.join(output_folder, "stock_data.pkl"))

        # Format DataFrame
        stock_data = stock_data.droplevel(1, axis=1).reset_index()

        # Calculate technical indicators using pandas-ta
        stock_data.ta.macd(append=True)
        stock_data.ta.rsi(append=True)
        stock_data.ta.bbands(append=True)
        stock_data.ta.obv(append=True)

        # Calculate additional technical indicators
        stock_data.ta.sma(length=20, append=True)
        stock_data.ta.ema(length=50, append=True)
        stock_data.ta.stoch(append=True)
        stock_data.ta.adx(append=True)

        # Calculate other indicators
        stock_data.ta.willr(append=True)
        stock_data.ta.cmf(append=True)
        stock_data.ta.psar(append=True)

        # Convert OBV to million
        stock_data['OBV_in_million'] = stock_data['OBV']/1e7
        stock_data['MACD_histogram_12_26_9'] = stock_data['MACDh_12_26_9']

        class SmaCross(Strategy):
          def init(self):
            price = self.data.Close
            self.ma1 = self.I(SMA, price, 10)
            self.ma2 = self.I(SMA, price, 20)

          def next(self):
            if crossover(self.ma1, self.ma2):
                  self.buy()
            elif crossover(self.ma2, self.ma1):
                  self.sell()

        # Generate summarized financial analysis with the help of Lexi
        generated_text = """In Progress"""

        ##############################################################################################################################
        # Plot the technical indicators

        html_charts = {}

        # Price Trend Chart
        price_rend_chart = plt.figure()
        plt.plot(stock_data.index, stock_data['Close'], label='Close', color='blue')
        plt.plot(stock_data.index, stock_data['EMA_50'], label='EMA 50', color='green')
        plt.plot(stock_data.index, stock_data['SMA_20'], label='SMA_20', color='orange')
        plt.title("Price Trend")
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))
        plt.xticks(rotation=45, fontsize=8)
        plotly_fig = tls.mpl_to_plotly(price_rend_chart, resize=True, strip_style=True, verbose=True)
        plotly_fig.update_layout(showlegend=True)
        html_charts["price_trend"] = pio.to_html(plotly_fig, full_html=False)


        # On-Balance Volume Chart
        onbalance_volume_chart = plt.figure()
        plt.plot(stock_data['OBV'], label='On-Balance Volume')
        plt.title('On-Balance Volume (OBV) Indicator')
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))
        plt.xticks(rotation=45, fontsize=8)
        plt.legend()
        plotly_fig = tls.mpl_to_plotly(onbalance_volume_chart, resize=True, strip_style=True, verbose=True)
        plotly_fig.update_layout(showlegend=True)
        html_charts["on_balance_volume_chart"] = pio.to_html(plotly_fig, full_html=False)

        # MACD Plot
        macd_plot = plt.figure()
        plt.plot(stock_data['MACD_12_26_9'], label='MACD')
        plt.plot(stock_data['MACDh_12_26_9'], label='MACD Histogram')
        plt.title('MACD Indicator')
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))
        plt.xticks(rotation=45, fontsize=8)
        plt.title("MACD")
        plt.legend()
        plotly_fig = tls.mpl_to_plotly(macd_plot, resize=True, strip_style=True, verbose=True)
        plotly_fig.update_layout(showlegend=True)
        html_charts["macd"] = pio.to_html(plotly_fig, full_html=False)

        # RSI Plot
        rsi_plot = plt.figure()
        plt.plot(stock_data['RSI_14'], label='RSI')
        plt.axhline(y=70, color='r', linestyle='--', label='Overbought (70)')
        plt.axhline(y=30, color='g', linestyle='--', label='Oversold (30)')
        plt.legend()
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))
        plt.xticks(rotation=45, fontsize=8)
        plotly_fig = tls.mpl_to_plotly(rsi_plot, resize=True, strip_style=True, verbose=True)
        plotly_fig.update_layout(showlegend=True)
        html_charts["rsi"] = pio.to_html(plotly_fig, full_html=False)

        # Bollinger Bands Plot
        bollinger_bands_plot = plt.figure()
        plt.plot(stock_data.index, stock_data['BBU_5_2.0'], label='Upper BB')
        plt.plot(stock_data.index, stock_data['BBM_5_2.0'], label='Middle BB')
        plt.plot(stock_data.index, stock_data['BBL_5_2.0'], label='Lower BB')
        plt.plot(stock_data.index, stock_data['Close'], label='Close', color='brown')
        plt.title("Bollinger Bands")
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))
        plt.xticks(rotation=45, fontsize=8)
        plt.legend()
        plotly_fig = tls.mpl_to_plotly(bollinger_bands_plot, resize=True, strip_style=True, verbose=True)
        plotly_fig.update_layout(showlegend=True)
        html_charts["bollinger_bands_plot"] = pio.to_html(plotly_fig, full_html=False)

        # Stochastic Oscillator Plot
        stochastic_oscillator_plot = plt.figure()
        plt.plot(stock_data.index, stock_data['STOCHk_14_3_3'], label='Stoch %K')
        plt.plot(stock_data.index, stock_data['STOCHd_14_3_3'], label='Stoch %D')
        plt.title("Stochastic Oscillator")
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))
        plt.xticks(rotation=45, fontsize=8)
        plt.legend()
        plotly_fig = tls.mpl_to_plotly(stochastic_oscillator_plot, resize=True, strip_style=True, verbose=True)
        plotly_fig.update_layout(showlegend=True)
        html_charts["stochastic_oscillator_plot"] = pio.to_html(plotly_fig, full_html=False)

        # Williams %R Plot
        williams_r_plot = plt.figure()
        plt.plot(stock_data.index, stock_data['WILLR_14'])
        plt.title("Williams %R")
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))
        plt.xticks(rotation=45, fontsize=8)
        plotly_fig = tls.mpl_to_plotly(williams_r_plot, resize=True, strip_style=True, verbose=True)
        plotly_fig.update_layout(showlegend=True)
        html_charts["williams_r_plot"] = pio.to_html(plotly_fig, full_html=False)

        # ADX Plot
        adx_plot = plt.figure()
        plt.plot(stock_data.index, stock_data['ADX_14'])
        plt.title("Average Directional Index (ADX)")
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))
        plt.xticks(rotation=45, fontsize=8)
        plotly_fig = tls.mpl_to_plotly(adx_plot, resize=True, strip_style=True, verbose=True)
        plotly_fig.update_layout(showlegend=True)
        html_charts["adx_plot"] = pio.to_html(plotly_fig, full_html=False)

        # CMF Plot
        cmf_plot = plt.figure()
        plt.plot(stock_data.index, stock_data['CMF_20'])
        plt.title("Chaikin Money Flow (CMF)")
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))
        plt.xticks(rotation=45, fontsize=8)
        plotly_fig = tls.mpl_to_plotly(cmf_plot, resize=True, strip_style=True, verbose=True)
        plotly_fig.update_layout(showlegend=True)
        html_charts["cmf"] = pio.to_html(plotly_fig, full_html=False)

        bt = Backtest(stock_data.set_index('Date'), SmaCross, commission=.002,
              exclusive_orders=True)
        bt.run()
        fig = bt.plot(open_browser=False, resample=False)
        html_charts["backtesting"] = file_html(fig, CDN)
        html_file = "SmaCross.html"
        if os.path.exists(html_file):
            os.remove(html_file)

        # Show the plots (if necessary, plt.show() can be disabled)
        plt.tight_layout()
        # plt.show()

        return html_charts, generated_text