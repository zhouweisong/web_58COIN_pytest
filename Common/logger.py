import logging
from Common import config
from logging.handlers import RotatingFileHandler
import time

fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'
logpath = config.log_dir + "web_autoTest_"+str(time.time())+".log"

handler_1 = logging.StreamHandler()
handler_1.setLevel(logging.INFO)

handler_2 = RotatingFileHandler(logpath, maxBytes=1024*1024*100,backupCount=10)
handler_2.setLevel(logging.INFO)

logging.basicConfig(format=fmt,datefmt=datefmt,level=logging.INFO,handlers=[handler_1,handler_2])
