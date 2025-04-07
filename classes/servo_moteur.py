from moteur import Moteur

class Moteur_Servo(Moteur):
    """
    Classe représentant un moteur servo.

    Attributs:

    - nom (str): Le nom du moteur.
    - pins (dict): Dictionnaire des numéros de pins associés au moteur.

    Méthodes:

    - actionner(donnees): Actionne le moteur servo avec les données fournies.
    """
    def __init__(self,nom,pins):
        super().__init__(nom,pins)

    def actionner(self,donnees):
        """
        Actionne le moteur servo avec les données fournies.
        """
        # Code pour actionner le moteur servo
        pass