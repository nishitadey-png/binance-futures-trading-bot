# Trading Bot Application (Mock Trading Environment)

## Project Overview

This project is a **Python-based trading bot application** developed as part of the **Primetrade.ai – Python Developer Application Task**.

The objective of this project is to demonstrate:

* Clean and reusable backend architecture
* Robust input validation and error handling
* Well-structured CLI and UI layers
* Logging of requests, responses, and failures
* Readiness for real-world trading API integration

⚠️ **Important Note:**

This implementation intentionally does **not** connect to the Binance Futures Testnet or any live exchange API.

Recent changes in Binance policies require **mandatory identity verification (KYC)** to generate Futures API keys for new accounts. Since the assignment evaluation focuses on **code quality, structure, validation, logging, and correctness of order flow**, a **mock trading environment** is used instead.

The application architecture is designed such that **real exchange APIs can be plugged in later with minimal changes**.

---

## Technical Stack Used

* **Language:** Python 3.8+
* **CLI Framework:** Typer
* **CLI Output Styling:** Rich
* **Web UI:** Streamlit (lightweight UI)
* **Logging:** Python `logging` module
* **Environment Management:** `venv`
* **Version Control:** Git

---

## Features

* BUY / SELL order simulation
* MARKET and LIMIT order types
* Enhanced interactive CLI (menu-driven)
* Lightweight Streamlit-based web UI
* Strong input validation with clear error messages
* Structured logging to files
* Modular and extendable codebase

---

## Project Structure

```
trading_bot/
│
├── app.py              
│
├── bot/
│   ├── __init__.py
│   ├── cli.py          
│   ├── client.py       
│   ├── orders.py       
│   ├── validators.py  
│   └── logging_config.py
│
├── logs/
│   ├── trading.log
│   ├── market_order.log
│   └── limit_order.log
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Setup Instructions

### 1. Prerequisites

* Python **3.8 or higher**
* Git
* VS Code (recommended)

---

### 2. Clone the Repository

```bash
git clone <https://github.com/nishitadey-png/binance-futures-trading-bot.git>
cd trading_bot
```

---

### 3. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

If required, dependencies include:

* typer
* rich
* streamlit

---

## How to Run the Application

The project supports **two execution modes**:

1. **Enhanced Interactive CLI**
2. **Lightweight Web UI (Streamlit)**

All commands must be executed from the **project root directory (`trading_bot`)**.

---

## Enhanced Interactive CLI

Run the CLI using:

```bash
python -m bot.cli
```

### CLI Flow

The CLI guides the user through:

* Selecting trading symbol
* Choosing BUY or SELL
* Selecting MARKET or LIMIT order
* Entering quantity
* Entering price (required for LIMIT orders)

All inputs are validated and clear error messages are displayed for invalid entries.

---

### Example CLI Output

```
Order Request Summary:
{'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.01}

Order Successful 
Order ID: MOCK12345
Status: FILLED
Executed Qty: 0.01
Avg Price: MARKET_PRICE
```

---

## Lightweight Web UI (Streamlit)

A minimal Streamlit UI is provided for easy interaction and demonstration.

### Run the Web UI

```bash
streamlit run app.py
```

### UI Features

* Form-based order placement
* MARKET and LIMIT order support
* Input validation
* Clear success and error messages
* Order summary display

---

## Logging

The application logs all order activity and errors.

### Log Files

* `logs/trading.log` – general application logs
* `logs/market_order.log` – MARKET order logs
* `logs/limit_order.log` – LIMIT order logs

Each log includes:

* Timestamp
* Order request details
* Simulated response
* Success or failure status

---

## Assumptions

* Orders are simulated (mock execution)
* No real funds or live APIs are used
* USDT-M Futures style contract logic assumed
* One order placed per execution
* No leverage, margin, or position management

---

## Design Decisions

* **Mock client** used to bypass external API restrictions
* **Separation of concerns** between CLI/UI, business logic, and client layer
* **Extensible architecture** for future integration with real exchanges

---

## Future Enhancements

* Integration with real trading APIs
* Strategy-based trading logic
* Persistent order history
* UI dashboard with charts

---

## Author

**Nishita Dey**
Python Developer 

---

## Conclusion

This project demonstrates strong Python fundamentals, clean architecture, validation, logging, and user experience design.

The mock trading approach ensures reliable evaluation while maintaining readiness for real-world trading system integration.
