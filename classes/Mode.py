from abc import ABC,abstractmethod
from Voiture import Voiture

class Mode(ABC):
    def __init__(self):
        self._voiture = Voiture("Vroum-Mobile")
    """
    Classe abstraite représentant un mode de fonctionnement de la voiture.

    Cette interface définit la méthode `executer()` que chaque mode (test, course, grand 8, etc.)
    doit implémenter pour décrire son comportement spécifique.
    """


    @abstractmethod
    def executer(self):
        pass