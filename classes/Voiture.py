from Affichage import VoitureInterface
from Servo_Moteur import Servo_Moteur
from Moteur_DC import Moteur_DC
from Capteur_Ultrasons import Capteur_Ultrasons
from Capteur_IR import Capteur_IR
import time
from threading import Thread, Lock


class Voiture:
    """
    Classe représentant une voiture autonome équipée de capteurs et de moteurs.
    Elle peut détecter des obstacles, suivre un mur, et effectuer une course avec plusieurs tours.
    """

    def __init__(self, nom):
        """
        Initialise une instance de la voiture.

        :param nom: Nom de la voiture.
        """
        self._nom = nom
        self._moteur = Moteur_DC("Moteur DC")
        self._servo = Servo_Moteur()
        self._capteur_avant = Capteur_Ultrasons("Capteur Avant", 5, 6)
        self._capteur_gauche = Capteur_Ultrasons("Capteur gauche", 9, 11)
        self._capteur_droit = Capteur_Ultrasons("Capteur droit", 19, 26)
        self._capteur_ligne = Capteur_IR("Capteur IR", 20)
        self._etat_voiture = True
        self._lock = Lock()

    @property
    def etat_voiture(self):
        return self._etat_voiture

    @property
    def lock(self):
        return self._lock

    @property
    def nom(self):
        return self._nom

    @property
    def moteur(self):
        return self._moteur

    @property
    def capteur_ligne(self):
        return self._capteur_ligne

    @property
    def servo(self):
        return self._servo

    @property
    def capteur_avant(self):
        return self._capteur_avant

    @property
    def capteur_gauche(self):
        return self._capteur_gauche

    @property
    def capteur_droit(self):
        return self._capteur_droit

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @lock.setter
    def lock(self, lock):
        self._lock = lock

    @etat_voiture.setter
    def etat_voiture(self, etat_voiture):
        self._etat_voiture = etat_voiture

    def suivre_mur(self, direction="droite"):
        """
        Fait suivre un mur à la voiture dans une direction donnée.

        :param direction: Direction du mur à suivre ("droite" ou "gauche").
        """
        if direction == "droite":
            capteur = self._capteur_droit
            while self._etat_voiture:
                distance = capteur.lire_donnee() * 100
                if distance <= 20 or distance >= 100:
                    self._servo.tourner_gauche()
                    time.sleep(0.3)
                elif distance >= 30:
                    self._servo.tourner_droite()
                    time.sleep(0.3)
                else:
                    self._servo.centrer()
                time.sleep(0.2)

    def detecter_collision(self):
        """
        Détecte les obstacles et ajuste la trajectoire de la voiture pour les éviter.
        """
        while self._etat_voiture:
            self._moteur.avancer(30)
            self._servo.centrer()
            distance_avant = self._capteur_avant.lire_donnee() * 100
            distance_gauche = self._capteur_gauche.lire_donnee() * 100
            distance_droite = self._capteur_droit.lire_donnee() * 100

            if distance_avant <= 20:
                self._moteur.stop()
                time.sleep(0.5)
                self._servo.tourner_gauche()
                self._moteur.reculer(-30)
                time.sleep(1)
                self._moteur.stop()
                time.sleep(0.5)
                self._servo.centrer()
                self._moteur.avancer(30)
                if distance_gauche > distance_droite:
                    self._servo.tourner_gauche()
                    self._moteur.avancer(30)
                    time.sleep(0.15)
                    self._servo.centrer()
                elif distance_droite > distance_gauche:
                    self._servo.tourner_droite()
                    self._moteur.avancer(30)
                    time.sleep(0.15)
                    self._servo.centrer()

    def aller_tout_droit(self):
        """
        Fait avancer la voiture en ligne droite.
        """
        self._servo.centrer()
        self._moteur.avancer(20)

    def demi_tour_en_T(self):
        """
        Effectue un demi-tour en forme de T.
        """
        self._servo.centrer()
        self._moteur.avancer(60)
        time.sleep(0.3)
        self._servo.tourner_gauche()
        time.sleep(1)
        self._moteur.stop()
        self._servo.centrer()
        time.sleep(0.1)
        self._servo.tourner_droite()
        time.sleep(1)
        self._moteur.reculer()
        time.sleep(1)
        self._moteur.stop()
        self._servo.centrer()
        self._moteur.avancer()
        time.sleep(1)
        self._moteur.stop()
        self._servo.desactiver_pwm()

    def grand_8(self):
        """
        Fait effectuer un mouvement en forme de 8 à la voiture.
        """
        self._servo.centrer()
        self._moteur.avancer(60)
        time.sleep(0.5)
        self._servo.tourner_droite()
        time.sleep(4.5)
        self._servo.centrer()
        time.sleep(0.3)
        self._servo.tourner_gauche()
        time.sleep(3.2)
        self._moteur.stop()
        self._servo.centrer()
        self._servo.desactiver_pwm()

    def arreter_voiture(self):
        """
        Arrête la voiture et désactive les moteurs.
        """
        self._moteur.stop()
        self._servo.desactiver_pwm()
        self._etat_voiture = False

    def compteur_tour(self, nb_tour):
        """
        Compte le nombre de tours effectués par la voiture.

        :param nb_tour: Nombre de tours à effectuer.
        """
        compte = nb_tour
        while compte > 0:
            if not self._capteur_ligne.lire_donnee():
                compte -= 1
                time.sleep(2)
        self.arreter_voiture()

    def course(self, nb_tour):
        """
        Lance une course avec détection des collisions, suivi de mur et comptage des tours.

        :param nb_tour: Nombre de tours à effectuer.
        """
        thread_collision = Thread(target=self.detecter_collision)
        thread_tours = Thread(target=self.compteur_tour, args=(nb_tour,))
        thread_mur = Thread(target=self.suivre_mur, args=("droite",))

        thread_collision.start()
        thread_tours.start()
        thread_mur.start()

        thread_collision.join()
        thread_tours.join()
        thread_mur.join()


voiture = Voiture("Vroum-Mobile")
interface = VoitureInterface(voiture)
