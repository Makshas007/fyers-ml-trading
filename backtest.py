import pandas as pd
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv("ircon.csv")


df["Returns"] = df["close"].pct_change()
df["Target"] = (df["close"].shift(-1) > df["close"]).astype(int)

features = ["open", "high", "low", "close", "volume"]


df = df.iloc[:-1]


split = int(0.7 * len(df))

train_df = df.iloc[:split]
test_df = df.iloc[split:]

X_train = train_df[features]
y_train = train_df["Target"]

X_test = test_df[features]


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


test_df = test_df.copy()
test_df["Signal"] = model.predict(X_test)


test_df["Position"] = test_df["Signal"].apply(lambda x: 1 if x == 1 else -1)


test_df["StrategyReturn"] = test_df["Position"].shift(1) * test_df["Returns"]
test_df["EquityCurve"] = (1 + test_df["StrategyReturn"].fillna(0)).cumprod()

print("Final equity:", test_df["EquityCurve"].iloc[-1])
