import logging
import os

from logging.handlers import RotatingFileHandler

from app.config import config

formatter = logging.Formatter('[%(asctime)s]\t %(name)s.%(funcName)s:%(lineno)d\t %(levelname)s : %(message)s',datefmt='%Y-%m-%d %H:%M:%S')



def setup_logger(name, log_file) -> logging.Logger:
    """To setup as many loggers as you want"""

    # handler = logging.FileHandler(log_file)
    __DEBUG_LEVEL__ = logging.INFO if config["development"].DEBUG else logging.ERROR


    if not os.path.exists('logs'):
        os.mkdir('logs')

    handler = RotatingFileHandler('logs/'+log_file, mode='a', encoding=None, delay=False)
    if 'info' in log_file:
        handler.maxBytes = 5*1024*1024
        handler.backupCount = 2

    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(__DEBUG_LEVEL__)
    logger.addHandler(handler)

    return logger