import pandas as pd
import kagglehub

# Download latest version
path = kagglehub.dataset_download("nelgiriyewithana/world-stock-prices-daily-updating")

df = pd.read_csv("World-Stock-Prices-Dataset.csv")

# Convert 'Date' to datetime right after reading
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
print("After conversion:", df['Date'].dtype)

# Drop rows where 'Date' couldn't be parsed
df = df.dropna(subset=['Date'])

tickers = ['AAPL','AMZN','MSFT','NVDA','BABA','TCEHY','JD','BYDDY','NIO']
df = df[df['Ticker'].isin(tickers)]

df = df[['Date','Open','Close','Brand_Name','Ticker']]
df['Day'] = df['Date'].dt.day
print(df.dtypes)