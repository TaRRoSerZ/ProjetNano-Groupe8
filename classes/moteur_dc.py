from moteur import Moteur

class Moteur_DC(Moteur):
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
        Actionne le moteur DC avec les données fournies.
        """
        # Code pour actionner le moteur DC
        pass