import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("ircon.csv")

# label: next-day direction
df["Target"] = (df["close"].shift(-1) > df["close"]).astype(int)

features = ["open", "high", "low", "close", "volume"]
X = df[features].iloc[:-1]
y = df["Target"].iloc[:-1]

split = int(0.7 * len(X))

X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print("Test accuracy:", accuracy)
