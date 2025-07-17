import pandas as pd
import kagglehub

# Download latest version
path = kagglehub.dataset_download("nelgiriyewithana/world-stock-prices-daily-updating")

df = pd.read_csv("World-Stock-Prices-Dataset.csv")
df.head()
tickers = ['AAPL','AMZN','MSFT','NVDA']
df = df[df['Ticker'].isin(tickers)]
df.head()
