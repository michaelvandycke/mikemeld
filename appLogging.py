import logging
import os

def resetLog():
    logging.basicConfig(filename=os.path.dirname(__file__)+'/mikemeld.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logging.info("New log file")

def logData(level, data):
    logging.basicConfig(filename=os.path.dirname(__file__)+'/mikemeld.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    
    match level:
        case 1:
            logging.critical(data)
        case 2:
            logging.error(data)
        case 3:
            logging.warning(data)
        case 4:
            logging.info(data)
        case 5:
            logging.debug(data)
