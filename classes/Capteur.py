from abc import ABC, abstractmethod

class Capteur(ABC):
    """
    Classe abstraite représentant les caractéristiques communes des capteurs.

    Attributs :

    nom : Nom du capteur
    """
    def __init__(self, nom: str):
        self._nom = nom


    @abstractmethod
    def lire_donnee(self):
        """Méthode abstraite permettant à tout les capteurs d'avoir la même méthode"""
        pass

    @property
    def nom(self):
        """getter de nom"""
        return self._nom

