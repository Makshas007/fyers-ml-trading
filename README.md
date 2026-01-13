# FYERS ML Trading Strategy (IRCON)

## Overview

This project implements an end-to-end **algorithmic trading pipeline** using the **FYERS API** and a **machine learning model** to generate trading signals for Indian equities.
The strategy is demonstrated on **IRCON International Ltd (NSE: IRCON-EQ)** using historical daily price data.

The system covers the complete workflow:

* Broker API authentication
* Historical data retrieval
* Feature preparation
* Machine learning–based signal generation
* Chronological backtesting
* Paper-traded execution
* Risk management considerations

This project was developed as part of **Finstreet Round 2 evaluation**.


## Project Structure

```
fyers_app/
│
├── app.py              # FYERS OAuth authentication & token generation
├── fetch_data.py       # Historical OHLCV data fetch via FYERS API
├── model.py            # Machine learning model training
├── backtest.py         # Chronological backtesting logic
├── trade.py            # Paper trading (simulated execution)
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignore secrets, logs, and generated files
```

Generated files such as CSVs and tokens are intentionally excluded from version control.


## Data Source

* **Broker API**: FYERS API
* **Instrument**: IRCON International Ltd (NSE: IRCON-EQ)
* **Frequency**: Daily candles (OHLCV)
* **Period**: November–December 2025

Historical data is fetched programmatically using authenticated API calls.


## Machine Learning Model

* **Model**: Random Forest Classifier
* **Features**: Open, High, Low, Close, Volume (OHLCV)
* **Target**: Next-day price direction (up/down)
* **Train/Test Split**:

  * First 70% → training
  * Remaining 30% → testing
* **Methodology**: Chronological split to avoid look-ahead bias

The model serves as a baseline predictive component rather than a fully optimized trading system.


## Backtesting Methodology

* Backtesting is performed **sequentially** to simulate real-world execution.
* Trades are assumed to execute on the **next trading day** after signal generation.
* Strategy returns are computed using **position-shifted daily returns**.
* Performance metrics are derived from the resulting equity curve.

### Key Results

* **Final equity**: ~0.94
* **Maximum drawdown**: ~6%

The results highlight the limitations of using basic price features without regime awareness or technical indicators.


## Paper Trading

Live order placement via the FYERS API requires available trading capital.
Since this project was executed without live margin, **paper trading** was used to simulate order execution.

Each model-generated signal is logged with:

* Date
* Execution price
* Trade direction (BUY / SELL)
* Quantity

This approach aligns with standard quantitative research practices before deploying live capital.


## Risk Management

Risk management rules applied conceptually in this project:

* Risk per trade limited to **≤ 2%**
* Fixed position size (1 share)
* Mandatory stop-loss assumption
* No overtrading (one decision per day)
* Single-symbol exposure

These constraints are documented and enforced at the strategy design level.


## Limitations

* Limited historical data window
* No transaction costs or slippage modeled
* Basic feature set (no technical indicators)
* Evaluated via paper trading due to capital constraints

These limitations are intentional to maintain transparency and avoid overfitting.


## Future Improvements

* Incorporate technical indicators (RSI, moving averages)
* Expand to multi-day prediction horizons
* Model confidence–based trade filtering
* Transaction cost and slippage modeling
* Multi-symbol portfolio extension


## Disclaimer

This project is for **educational and research purposes only**.
It does not constitute financial advice or a recommendation to trade securities.


## Author

**Saksham**
GitHub: [https://github.com/Makshas007/fyers-ml-trading](https://github.com/Makshas007/fyers-ml-trading)

