from servo import Servo_Moteur
from Moteur_DC import Moteur_DC
from Capteur_Ultrasons import Capteur_Ultrasons
from Capteur_IR import Capteur_IR
import time
from threading import Thread, Lock



class Voiture:
    def __init__(self, nom):
        self._nom = nom
        self._moteur = Moteur_DC("Moteur DC")
        self._servo = Servo_Moteur()
        self._capteur_avant = Capteur_Ultrasons("Capteur Avant", 5, 6)
        self._capteur_gauche = Capteur_Ultrasons("Capteur gauche", 9, 11)
        self._capteur_droit = Capteur_Ultrasons("Capteur droit", 19, 26)
        self._capteur_ligne = Capteur_IR("Capteur IR", 20)

        # État partagé pour contrôler la voiture
        self._etat_voiture = "AVANCER"  # L'état peut être "AVANCER", "EVITER_OBSTACLE", etc.
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


    def faire_demi_tour(self):
        self._servo.centrer()
        self._moteur.avancer(60)
        time.sleep(2)
        self._servo.tourner_droite()
        time.sleep(2)
        self._servo.centrer()
        time.sleep(2)
        self._moteur.stop()
        self._servo.desactiver_pwm()

    def aller_tout_droit(self):
        self._servo.centrer()
        self._moteur.avancer(100)
        time.sleep(5)
        self._moteur.stop()
        self._servo.desactiver_pwm()

    def detecter_collision_avant(self):

        while True:
            distance = self._capteur_avant.lire_donnee() * 100  # Conversion de la distance en cm
            print(f"Distance détectée : {distance} cm")
            if distance <= 10:
                self.moteur.avancer(10)
                return False
            time.sleep(0.3)

    def detecter_collision_gauche(self):

        while True:
            distance = self.capteur_gauche.lire_donnee() * 100
            if self.detecter_collision_avant() == False:
                return
            elif distance <= 10:
                self._servo.tourner_droite()
                return None
            time.sleep(0.3)

    def detecter_collision_droite(self):

        while True:
            distance = self.capteur_droit.lire_donnee() * 100
            if distance <= 10:
                self._servo.tourner_gauche()
                return None
            time.sleep(0.3)

    def demi_tour_en_T(self):
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
        self._moteur.stop()

    def detecter_ligne_arrivee(self):
        time.sleep(5)
        while True:
            if self._capteur_ligne.lire_donnee():
                ligne_noire = self._capteur_avant.lire_donnee()

                if ligne_noire:
                    print("Ligne noire détectée")
                    self.arreter_voiture()
                    break
        time.sleep(0.1)

    def demarrer(self):
        thread_mouvement = Thread(target=self.aller_tout_droit)
        thread_capteur_ultrasons_avant = Thread(target=self.detecter_collision_avant)
        thread_capteur_ultrasons_gauche = Thread(target=self.detecter_collision_gauche)
        thread_capteur_ultrasons_droite = Thread(target=self.detecter_collision_droite)
        thread_ligne = Thread(target=self.detecter_ligne_arrivee)


        thread_mouvement.start()
        thread_capteur_ultrasons_avant.start()
        thread_capteur_ultrasons_gauche.start()
        thread_capteur_ultrasons_droite.start()
        thread_ligne.start()

        thread_mouvement.join()
        thread_capteur_ultrasons_avant.join()
        thread_capteur_ultrasons_gauche.join()
        thread_capteur_ultrasons_droite.join()
        thread_ligne.join()


voiture = Voiture("Vroum-Mobile")
voiture.demarrer()

