from bot.logging_config import setup_logger



logger = setup_logger("validators")


VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_input(symbol,side,order_type,quantity,price=None):
    logger.debug(f"Validating input: symbol={symbol}, side={side}, order_type={order_type}, quantity={quantity}, price={price}")

    if side.upper() not in VALID_SIDES or order_type.upper() not in VALID_ORDER_TYPES:
        logger.error(f"Invalid side or order type: side={side}, order_type={order_type}") 
        raise ValueError("Inavlid input please input proper values")

    if quantity <=0:
        logger.error(f"Invalid quantity: quantity={quantity}")
        raise ValueError("Quantity must be greater than 0") 
    
    if order_type.upper() == "LIMIT" and (price is None or price <= 0):
        logger.error(f"Invalid price for LIMIT order: price={price}")
        raise ValueError("Price must be greater than 0 for LIMIT orders")   
    
    logger.info("Input validation successful")
    return symbol.upper(), side.upper(), order_type.upper()