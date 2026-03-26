import os 
import logging



def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    os.makedirs("logs", exist_ok=True)  

    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    filehandler = logging.FileHandler("logs/trading_bot.log")
    filehandler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(filehandler)
    logger.addHandler(console_handler)

    
    return logger 