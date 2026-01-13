import pandas as pd

# Load historical data
df = pd.read_csv("ircon.csv")

# Assume this column was created in backtest
# 1 = Buy, -1 = Sell
df["Signal"] = df["close"].pct_change().apply(lambda x: 1 if x > 0 else -1)

paper_trades = []

for i in range(1, len(df)):
    trade = {
        "date": df.loc[i, "date"],
        "price": df.loc[i, "close"],
        "action": "BUY" if df.loc[i-1, "Signal"] == 1 else "SELL",
        "qty": 1
    }
    paper_trades.append(trade)

trades_df = pd.DataFrame(paper_trades)
trades_df.to_csv("paper_trades.csv", index=False)

print("Paper trading completed.")
print(trades_df.head())
