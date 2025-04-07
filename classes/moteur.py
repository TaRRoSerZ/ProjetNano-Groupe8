from abc import ABC, abstractmethod


class Moteur(ABC):
    """
    Classe abstraite représentant un moteur.

    Attributs:

    - nom (str): Le nom du moteur.
    - pins (dict): Dictionnaire des numéros de pins associés au moteur.

    Méthodes:

    - actionner(donnees): Méthode abstraite pour actionner le moteur avec les données fournies.
    """
    def __init__(self,nom,pins):
        self._nom = nom
        self._pins = pins

    @abstractmethod
    def actionner(self,donnees):
        """
        Méthode abstraite pour actionner le moteur avec les données fournies.
        """
        pass

