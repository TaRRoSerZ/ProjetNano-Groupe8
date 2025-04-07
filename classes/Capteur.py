from abc import ABC, abstractmethod

class Capteur(ABC):
    """
    Classe abstraite représentant les caractéristiques communes des capteurs.

    Attributs :

    nom : Nom du capteur

    pins : pins utilisées par le capteur
    """
    def __init__(self, nom: str, pins: dict):
        self._nom = nom
        self._pins = pins

    @abstractmethod
    def lire_valeur(self):
        pass

    @property
    def nom(self):
        """getter de nom"""
        return self._nom

    @property
    def pins(self):
        """getter de pins"""
        return self._pins
