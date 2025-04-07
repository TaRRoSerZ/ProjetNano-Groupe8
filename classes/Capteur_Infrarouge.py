from Capteur import Capteur

class Capteur_Infrarouge(Capteur):
    """
    Classe implémentant le fonctionnement des capteurs infrarouges.

    Attributs :

    nom : Nom du capteur

    pins : pins utilisées par le capteur
    """
    def __init__(self, nom, pins):
        super().__init__(nom, pins)


    def lire_valeur(self):
        pass

