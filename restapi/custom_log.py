import logging
import datetime

currentdate = datetime.datetime.now().strftime("%d%m%Y")

def setup_logger(logger_name,log_file,level=logging.INFO):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(message)s')
    fileHandler = logging.FileHandler('log/'+log_file+'_'+currentdate,mode='a')
    fileHandler.setFormatter(formatter)
    l.setLevel(level)
    l.addHandler(fileHandler)