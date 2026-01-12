import json
from fyers_apiv3 import fyersModel

CLIENT_ID = "3SMH0PH30V-100"

with open("token.json", "r") as f:
    data = json.load(f)

# Handle both FYERS response formats safely
if "access_token" in data:
    access_token = data["access_token"]
elif "data" in data and "access_token" in data["data"]:
    access_token = data["data"]["access_token"]
else:
    raise Exception(f"No access token found in token.json: {data}")

fyers = fyersModel.FyersModel(
    client_id=CLIENT_ID,
    token=access_token,
    log_path=""
)

response = fyers.get_profile()
print(response)
