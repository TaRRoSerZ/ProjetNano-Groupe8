import logging

def setupLoggeur():
    """
    Méthode qui permet de mettre en place le fichier logs.txt, écrire dedans si il existe et le créer s'il n'est pas encore dans l'arborescance.
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime) s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('../Logs/logs.txt'),
        ]
    )

def lireLogs(limite):
    """
    Méthode qui permet de lire les logs et de les afficher dans la console. 

    args :
        - limite : permet de définir le nombre de ligne qui va être affiché dans la console (en partant du log le plus récent)
    """
    if type(limite) != int:
        limite = 20

    with open('../Logs/logs.txt', 'r') as f:
        lines = f.readlines()[-limite:]
        for line in lines:
            print(line, end=" ")

        f.close()
