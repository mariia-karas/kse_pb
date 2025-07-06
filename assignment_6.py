import yfinance as yf
import pandas as pd

apple = yf.Ticker("AAPL")
df = apple.history(period="5y", interval="1d").drop(columns=["Dividends", "Stock Splits"]).reset_index()

df["SMA_50"] = df["Close"].rolling(window=50).mean()
df["SMA_200"] = df["Close"].rolling(window=200).mean()
df = df.iloc[199:]

shares = 0
cash = 10000

for day in range(1, len(df)-1):
  SMA_50_yesterday = df["SMA_50"].iloc[day-1]
  SMA_50_today = df["SMA_50"].iloc[day]
  SMA_200_yesterday = df["SMA_200"].iloc[day-1]
  SMA_200_today = df["SMA_200"].iloc[day]
  price = df["Close"].iloc[day+1]
  date = df["Date"].iloc[day+1]

  if SMA_50_yesterday > SMA_200_yesterday and SMA_50_today < SMA_200_today:
    if shares > 0:
      cash += shares*price
      print(f"{shares} sold on {date}")
      shares = 0

  elif SMA_50_yesterday < SMA_200_yesterday and SMA_50_today > SMA_200_today:
    if cash >= price:
      shares_to_buy = cash // price
      cash -= shares_to_buy*price
      print(f"{shares_to_buy} bought on {date}")
      shares += shares_to_buy 
      
  
profit_lose = cash + shares * df["Close"].iloc[-1] - 10000

if profit_lose>0:
  print(f"Tot al profit: {profit_lose}")
if profit_lose<=0:
  print(f"Total lose: {profit_lose}")