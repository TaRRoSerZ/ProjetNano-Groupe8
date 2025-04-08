

class Moteur_DC():
    """
        Classe représentant un moteur servo.

        Attributs:

        - nom (str): Le nom du moteur.
        - pins (dict): Dictionnaire des numéros de pins associés au moteur.
        - vitesse (int): La vitesse du moteur.
        - direction (str): La direction du moteur.

        Méthodes:

        - regler_vitesse :Actionne le moteur DC avec les données fournies.
        :param vitesse:

        -changer_direction :Change la direction du moteur DC.
        :param direction:
        """
    def __init__(self,nom,pins,vitesse,direction):
        self._noms = nom
        self._pins = pins
        self._vitesse = vitesse
        self._direction = direction

    def regler_vitesse(self,vitesse):


        pass

    def changer_direction(self,direction):

        pass