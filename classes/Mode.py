from abc import ABC,abstractmethod
class Mode(ABC):
    """
    Classe abstraite représentant un mode de fonctionnement de la voiture.

    Cette interface définit la méthode `executer()` que chaque mode (test, course, grand 8, etc.)
    doit implémenter pour décrire son comportement spécifique.
    """
    @abstractmethod
    def executer(self):
        pass