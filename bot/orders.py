from bot.validators import validate_input
from binance.exceptions import BinanceAPIException
from bot.client import get_client
from bot.logging_config import setup_logger

logger = setup_logger("orders")

def place_order(symbol,side,order_type,quantity,price=None):
    try:
        symbol, side, order_type = validate_input(symbol, side, order_type, quantity, price)
        client = get_client()
        order_params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }
        if order_type == "LIMIT":
            order_params["price"] = price
            order_params["timeInForce"] = "GTC"
        order_response = client.futures_create_order(**order_params)
        logger.info(f"Order placed successfully: {order_response}")
        return order_response
    except BinanceAPIException as e:
        logger.error(f"Binance API error: {e.message}")
        raise
    except Exception as e:
        logger.error(f"Error placing order: {str(e)}")
        raise

