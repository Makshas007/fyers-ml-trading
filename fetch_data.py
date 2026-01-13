import json
import pandas as pd
from fyers_apiv3 import fyersModel

CLIENT_ID = "3SMH0PH30V-100"

with open("token.json", "r") as f:
    data = json.load(f)


if "access_token" in data:
    access_token = data["access_token"]
else:
    access_token = data["data"]["access_token"]

fyers = fyersModel.FyersModel(
    client_id=CLIENT_ID,
    token=access_token,
    log_path=""
)

params = {
    "symbol": "NSE:IRCON-EQ",
    "resolution": "D",
    "date_format": "1",
    "range_from": "2025-11-01",
    "range_to": "2025-12-31",
    "cont_flag": "0"
}

resp = fyers.history(data=params)

df = pd.DataFrame(
    resp["candles"],
    columns=["timestamp", "open", "high", "low", "close", "volume"]
)

df["date"] = pd.to_datetime(df["timestamp"], unit="s")
df.drop(columns=["timestamp"], inplace=True)

df.to_csv("ircon.csv", index=False)
print(df.head())
