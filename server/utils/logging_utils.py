import logging
from logging.handlers import TimedRotatingFileHandler
from constants import LOGS_DIR

debug_handler = TimedRotatingFileHandler(f"{LOGS_DIR}/debug.log", when="midnight", interval=1, backupCount=10)
debug_handler.setLevel(logging.DEBUG)
info_handler = TimedRotatingFileHandler(f"{LOGS_DIR}/info.log", when="midnight", interval=1, backupCount=10)
info_handler.setLevel(logging.INFO)
warning_handler = TimedRotatingFileHandler(f"{LOGS_DIR}/warning.log", when="W0", interval=1, backupCount=4)
warning_handler.setLevel(logging.WARNING)
error_handler = TimedRotatingFileHandler(f"{LOGS_DIR}/error.log", when="W0", interval=1, backupCount=4)
error_handler.setLevel(logging.ERROR)
critical_handler = TimedRotatingFileHandler(f"{LOGS_DIR}/critical.log", when="W0", interval=4, backupCount=10)
critical_handler.setLevel(logging.CRITICAL)

access_handler = TimedRotatingFileHandler(f"{LOGS_DIR}/access.log", when="midnight", interval=1, backupCount=10)
access_handler.setLevel(logging.INFO)
error_spec_handler = TimedRotatingFileHandler(f"{LOGS_DIR}/error_specific.log", when="W0", interval=1, backupCount=4)
error_spec_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('[%(asctime)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
debug_handler.setFormatter(formatter)
info_handler.setFormatter(formatter)
warning_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)
critical_handler.setFormatter(formatter)
access_handler.setFormatter(formatter)
error_spec_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.addHandler(debug_handler)
logger.addHandler(info_handler)
logger.addHandler(warning_handler)
logger.addHandler(error_handler)
logger.addHandler(critical_handler)
logger.addHandler(console_handler)
