from Capteur import Capteur
from gpiozero import DigitalInputDevice


class Capteur_IR(Capteur):
    """
    Classe implémentant le fonctionnement des capteurs infrarouges.

    Attributs :

    nom : Nom du capteur

    pin_signal : pin servant à se connecter au Raspberry

    Methodes :

    lire_donnee() :
        Renvoie la veleur de detection du capteur.
    """
    def __init__(self, nom, pin_signal: int):
        super().__init__(nom)
        self._pin_signal = pin_signal
        self._capteur = DigitalInputDevice(pin_signal)


    def lire_donnee(self):
        return not self._capteur.value



