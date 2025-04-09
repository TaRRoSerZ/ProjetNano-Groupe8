

class Voiture :
    def __init__(self, nom:str) :
        self._nom = nom
        self._vitesse = 0
        self._direction = 0
        self._etat_batterie = 0.0
        self._capteurs = []
        self._pont_h = None
        self._servo_moteur = None
        self._batterie = None
        self._etat_voiture = "arret"

        @property
        def nom(self) :
            return self._nom

        @property
        def vitesse(self) :
            return self._vitesse

        @property
        def direction(self) :
            return self._direction

        @property
        def etat_batterie(self) :
            return self._etat_batterie

        @property
        def capteurs(self) :
            return self._capteurs

        @property
        def pont_h(self) :
            return self._pont_h

        @property
        def servo_moteur(self) :
            return self._servo_moteur

        @property
        def batterie(self) :
            return self._batterie

        @property
        def etat_voiture(self) :
            return self._etat_voiture

    def __str__(self) :
        return f"Voiture : {self.nom} \n Etat : {self.etat_voiture}"

    def demarrer(self):
        pass

    def arreter(self):
        pass

    def se_deplacer(self):
        pass

    def mettre_a_jour_position(self):
        pass

    def eviter_obstacle(self):
        pass

    def verifier_batterie(self):
        pass

    def affichage_vitesse(self):
        return print(f"Vitesse : {self._vitesse}")

