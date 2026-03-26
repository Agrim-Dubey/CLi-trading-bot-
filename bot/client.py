from binance.client import Client
from dotenv import load_dotenv
from bot.logging_config import setup_logger
import os 

logger = setup_logger("client")
def get_client():
    load_dotenv()
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_SECRET_KEY")
    if not api_key or not api_secret:
        raise ValueError("API key or API secret was found missing")
    else:
        client = Client(api_key,api_secret,testnet=True)
        logger.info("Client initialized successfully")
        return client