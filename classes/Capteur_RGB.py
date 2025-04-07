from Capteur import Capteur

class Capteur_RGB(Capteur):
    """
        Classe implémentant le fonctionnement des capteurs RGB.

        Attributs :

        nom : Nom du capteur

        pins : pins utilisées par le capteur
        """
    def __init__(self, nom, pins):
        super().__init__(nom, pins)


    def lire_valeur(self):
        pass
