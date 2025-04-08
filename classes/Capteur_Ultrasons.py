from Capteur import Capteur

class Capteur_Ultrasons(Capteur):
    """
    Classe implémentant le fonctionnement des capteurs à ultrasons.

    Attributs :

    nom : Nom du capteur

    pin_echo : pin servant à la réception

    pin_trig : pin servant à l'envoie du signal
    """
    def __init__(self, nom, pin_echo, pin_trig):
        super().__init__(nom)
        self._pin_echo = pin_echo
        self._pin_trig = pin_trig


    def lire_valeur(self):
        pass



