from Capteur import Capteur

class Capteur_IR(Capteur):
    """
    Classe implémentant le fonctionnement des capteurs infrarouges.

    Attributs :

    nom : Nom du capteur

    pin_signal : pin servant à se connecter au Raspberry
    """
    def __init__(self, nom, pin_signal: int):
        super().__init__(nom)
        self._pin_signal = pin_signal


    def lire_valeur(self):
        pass

