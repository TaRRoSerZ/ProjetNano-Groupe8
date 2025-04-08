

class Servo_Moteur():
    """
    Classe représentant un servo moteur.

    Attributs:

    - nom (str): Le nom du moteur.
    - pins (dict): Dictionnaire des numéros de pins associés au moteur.

    Méthodes:

    - actionner(donnees): Actionne le moteur servo avec les données fournies.
    """
    def __init__(self,nom,pins,angle):
        self._nom = nom
        self._pins = pins
        self._angle = angle

    def regler_angle(self,angle):
        """
        Actionne le moteur servo avec les données fournies.
        """
        # Code pour actionner le moteur servo
        pass

