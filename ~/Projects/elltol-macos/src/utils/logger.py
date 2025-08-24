
from loguru import logger
import os

log_path = os.path.expanduser("~/Library/Logs/EllTol/")
os.makedirs(log_path, exist_ok=True)

logger.add(f"{log_path}/app.log", rotation="10 MB", retention="30 days")

def get_logger():
    return logger
