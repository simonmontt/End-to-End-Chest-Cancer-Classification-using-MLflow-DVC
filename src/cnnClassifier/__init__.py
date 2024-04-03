import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" #Ascii time, level, module name and the message of the log

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # To create the logs folder and save the logs inside of it
        logging.StreamHandler(sys.stdout)  # To print the log in the terminal itself
    ]
)

logger = logging.getLogger("cnnClassifierLogger")