import logging

def setupLoggeur():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime) s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('../logs.txt'),
        ]
    )