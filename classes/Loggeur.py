import logging

def setupLoggeur():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime) s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('../Logs/logs.txt'),
        ]
    )

def lireLogs(limite):
    if type(limite) != int:
        limite = 20

    with open('../Logs/logs.txt', 'r') as f:
        lines = f.readlines()[-limite:]
        for line in lines:
            print(line, end=" ")

        f.close()
