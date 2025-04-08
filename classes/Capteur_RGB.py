from Capteur import Capteur

class Capteur_RGB(Capteur):
    """
        Classe implémentant le fonctionnement des capteurs RGB.

        Attributs :

        nom : Nom du capteur

        pin_R : pin pour le rouge

        pin_G : pin pour le vert

        pin_B : pin pour le bleu

        pin_C : pin servant à régler l'instensité de la luminosité
        """
    def __init__(self, nom, pin_R, pin_G, pin_B, pin_C):
        super().__init__(nom)
        self._pin_R = pin_R
        self._pin_G = pin_G
        self._pin_B = pin_B
        self._pin_C = pin_C


    def lire_valeur(self):
        pass
