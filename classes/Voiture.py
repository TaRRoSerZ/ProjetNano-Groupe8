class Voiture:
    """
    La classe voiture représente la classe principale qui sera instanciée lors du lancement de la voiture
    elle permet de gérer toutes les actions réalisables par la voiture
    """

    def __init__(self, nom, nombre_tour):
        self._nom = nom
        self._nombre_tour = nombre_tour
        self._moteurs = {}
        self._capteurs = {}

    def __str__(self):
        return self.nom + " " + self.nombre_tour


    @property
    def nom(self):
        return self._nom

    @property
    def nombre_tour(self):
        return self._nombre_tour

    @nombre_tour.setter
    def nombre_tour(self, nombre_tour):
        self._nombre_tour = nombre_tour

    @property
    def moteurs(self):
        return self._moteurs


    @property
    def capteurs(self):
        return self._capteurs


    def lire_valeur(self):
        pass

    def avancer(self):
        pass

    def tourner(self, direction):
        pass

    def arret(self):
        pass

    def calculer_vitesse(self):
        pass

    def mode_test(self):
        pass


