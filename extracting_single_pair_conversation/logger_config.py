import logging

logging.basicConfig(filename='logging_file.log',level=logging.DEBUG,format="%(asctime)s%(message)s",filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# def get_logger_instace(name):
#     logger = logging.getLogger(name)    
#     logger.setLevel(logging.DEBUG)
#     return logger

# logging_config.py

# import logging

# # Create or get the logger
# logger = logging.getLogger('shared_logger')
# logger.setLevel(logging.DEBUG)  # Log everything (DEBUG level or higher)

# # Prevent multiple handlers if the logger is configured multiple times
# if not logger.handlers:
#     # Create a file handler to log to a file
#     file_handler = logging.FileHandler('shared_log_file.log')
#     file_handler.setLevel(logging.DEBUG)

#     # Define log format
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     file_handler.setFormatter(formatter)

#     # Add file handler to logger
#     logger.addHandler(file_handler)