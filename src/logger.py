import logging
import os 
from datetime import datetime

# FIX 1: Fixed the datetime formatting string
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# FIX 2: Set logs_path to JUST the directory, then create it
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Create the final file path by joining the directory and the file name
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    # FIX 3: Removed the quotes around the variable name
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  
    level=logging.INFO,
)
