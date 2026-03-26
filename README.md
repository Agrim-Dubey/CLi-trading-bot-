# CLI Trading Bot — Binance Futures Testnet

A command-line Python application to place Market and Limit orders on Binance Futures Testnet (USDT-M).

---

## Project Structure

```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance API client wrapper
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   └── logging_config.py  # Logging setup
├── cli.py                 # CLI entry point
├── .env                   # API keys (never commit this)
├── requirements.txt
├── README.md
└── logs/
    └── trading_bot.log    # Auto-generated
```

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Agrim-Dubey/CLI-trading-bot.git
cd CLI-trading-bot
```

### 2. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Get Binance Testnet API Keys

1. Go to [https://testnet.binancefuture.com](https://testnet.binancefuture.com)
2. Log in and generate API credentials
3. Copy your API Key and Secret

### 5. Create your `.env` file

Create a file called `.env` in the root of the project:

```
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
```

---

## How to Run

### Place a MARKET order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Place a LIMIT order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 80000
```

### See all available options

```bash
python cli.py --help
```

---

## Example Output

```
Order Request Summary
  Symbol   : BTCUSDT
  Side     : BUY
  Type     : MARKET
  Quantity : 0.01

Order Placed Successfully!
┌─────────────┬──────────────┐
│ Field       │ Value        │
├─────────────┼──────────────┤
│ orderId     │ 123456789    │
│ symbol      │ BTCUSDT      │
│ side        │ BUY          │
│ type        │ MARKET       │
│ status      │ FILLED       │
│ executedQty │ 0.01         │
│ avgPrice    │ 84321.50     │
└─────────────┴──────────────┘
```

---

## Logging

All API requests, responses, and errors are logged to `logs/trading_bot.log` automatically.

Log format:
```
2025-03-26 20:15:00 | INFO | orders | Order placed successfully: {...}
2025-03-26 20:15:00 | ERROR | client | API keys missing. Check your .env file.
```

---

## Assumptions

- All orders are placed on Binance Futures Testnet (USDT-M), not real Binance
- LIMIT orders require a `--price` argument, MARKET orders do not
- Quantity must be greater than 0
- Side must be `BUY` or `SELL`
- Order type must be `MARKET` or `LIMIT`
- API keys must be set in `.env` before running

---

## Requirements

- Python 3.x
- Binance Futures Testnet account and API credentials

```
python-binance
python-dotenv
typer
rich
```