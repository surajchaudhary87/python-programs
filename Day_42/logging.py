# 1. What is Logging?
#   --Logging means recording messages about the execution of a program.

import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("This is a debug message")
logging.info("Application started")
logging.warning("Low storage space")
logging.error("Something went wrong")
logging.critical("Application cannot continue")