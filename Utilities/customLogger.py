import logging.handlers
import logging

class LogGen:
    @staticmethod
    def logger():
        logging.basicConfig(filename="Logs/C2taAutomationLog.log", format = '%(asctime)s-%(message)s', 
        datefmt='%d-%b-%y %H:%M:%S', filemode='w'
        )
        rotate_file = logging.handlers.RotatingFileHandler(
            "Logs/C2taAutomationLog.log", maxBytes=1024 * 1024 * 28, backupCount=3
        )

        logger = logging.getLogger()
        logger.addHandler(rotate_file)
        logger.setLevel(logging.INFO)
        return logger