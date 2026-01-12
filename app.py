import json
from flask import Flask, redirect, request
from fyers_apiv3 import fyersModel

app = Flask(__name__)

CLIENT_ID = "3SMH0PH30V-100"
SECRET_KEY = "GSFQXONA8X"
REDIRECT_URI = "http://127.0.0.1:5000/callback"

@app.route("/")
def home():
    return "Server is running"

@app.route("/test")
def test():
    return "Test route works"

@app.route("/login")
def login():
    session = fyersModel.SessionModel(
        client_id=CLIENT_ID,
        secret_key=SECRET_KEY,
        redirect_uri=REDIRECT_URI,
        response_type="code",
        grant_type="authorization_code"
    )
    auth_url = session.generate_authcode()
    return redirect(auth_url)

@app.route("/callback")
def callback():
    auth_code = request.args.get("auth_code")

    if not auth_code:
        return "Authorization failed: no auth code"

    session = fyersModel.SessionModel(
        client_id=CLIENT_ID,
        secret_key=SECRET_KEY,
        redirect_uri=REDIRECT_URI,
        response_type="code",
        grant_type="authorization_code"
    )

    session.set_token(auth_code)
    response = session.generate_token()

    
    if response.get("s") != "ok":
        return f"Token generation failed: {response}"

    with open("token.json", "w") as f:
        json.dump(response, f, indent=2)

    return "Login successful. Access token stored."



if __name__ == "__main__":
    app.run(debug=True)