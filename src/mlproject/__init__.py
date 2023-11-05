#Creating custom login
import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"#Initialize logging string
#Basically that will give us information about (time, name, which module is used, and message what it will print)

log_dir = "logs"#Creating a log folder
log_filepath = os.path.join(log_dir, "running_logs.log")#Inside this folder creating a log file
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(#And called the basic method that will provide all command inside log file
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),#Will create inside this log folder inside that it will save all the loging
        logging.StreamHandler(sys.stdout)# Will print all the logs inside terminal whenever you will execute your Template.py file
    ]
)

logger = logging.getLogger("MLOpsprojectLogger")#initialize your logging