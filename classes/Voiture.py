from Servo_Moteur import Servo_Moteur
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

        if direction == "droite":
            capteur = self._capteur_droit
            while self._etat_voiture:
                print("Suivre le mur...")
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
        else:
            pass

    def detecter_collision(self):
        while self._etat_voiture:
            self._moteur.avancer(30)  # Démarrer la voiture en ligne droite
            self._servo.centrer()  # Centrer le servo
            distance_avant = self._capteur_avant.lire_donnee() * 100
            distance_gauche = self._capteur_gauche.lire_donnee() * 100
            distance_droite = self._capteur_droit.lire_donnee() * 100

            if distance_avant <= 20:  # Si un obstacle est détecté à l'avant
                print("Obstacle détecté à l'avant, ralentissement...")
                self._moteur.stop()  # stop
                time.sleep(0.5)
                self._servo.tourner_gauche()
                self._moteur.reculer(-30)
                time.sleep(1)
                self._moteur.stop()
                time.sleep(0.5)
                self._servo.centrer()
                self._moteur.avancer(30)  # Avancer après avoir évité l'obstacle
                if distance_gauche > distance_droite:  # Plus d'espace à gauche
                    print("Esquive vers la gauche...")
                    self._servo.tourner_gauche()
                    self._moteur.avancer(30)
                    time.sleep(0.15)
                    self._servo.centrer()
                elif distance_droite > distance_gauche:  # Plus d'espace à droite
                    print("Esquive vers la droite...")
                    self._servo.tourner_droite()
                    self._moteur.avancer(30)
                    time.sleep(0.15)
                    self._servo.centrer()


            elif distance_gauche > distance_droite:  # Plus d'espace à gauche
                print("Esquive vers la gauche...")
                self._servo.tourner_gauche()
                time.sleep(0.15)
                self._servo.centrer()

            elif distance_droite > distance_gauche:  # Plus d'espace à droite
                print("Esquive vers la droite...")
                self._servo.tourner_droite()
                time.sleep(0.15)
                self._servo.centrer()

            elif distance_avant <= 20 and distance_gauche <= 11:
                self._moteur.stop()
                self._servo.centrer()
                self._moteur.reculer(-30)  # Reculer de 20 cm
                time.sleep(1)
                self._moteur.stop()
                time.sleep(1)
                self._servo.tourner_droite()
                self._moteur.avancer(30)
                time.sleep(0.3)
                self._moteur.stop()
                self._servo.tourner_gauche()
                time.sleep(0.1)
                self._servo.centrer()
                self._moteur.avancer(30)


            elif distance_avant <= 20 and distance_droite <= 11:
                self._moteur.stop()
                self._servo.centrer()
                self._moteur.reculer(-30)  # Reculer de 20 cm
                time.sleep(1)
                self._moteur.stop()
                time.sleep(1)
                self._servo.tourner_gauche()
                self._moteur.avancer(30)
                time.sleep(0.3)
                self._moteur.stop()
                self._servo.tourner_droite()
                time.sleep(0.1)
                self._servo.centrer()
                self._moteur.avancer(30)
        time.sleep(0.3)

        # else:
        #     print("Obstacle trop proche, arrêt...")
        #     self._moteur.stop()  # Arrêter si aucun espace disponible
        #     break
        # else:
        #     print("Aucun obstacle détecté, avancer...")
        #     self._servo.centrer()
        #     self._moteur.avancer(30)  # Vitesse normale

    # def eviter_obstacles(self):
    #     if self.detecter_collision_avant() and self.detecter_collision_droite():
    #         self._moteur.stop()
    #         time.sleep(1)
    #         self._moteur.reculer(-20)
    #         time.sleep(1)
    #         self._moteur.stop()
    #         time.sleep(1)
    #         self._servo.tourner_gauche()
    #         self._moteur.avancer(20)
    #         time.sleep(1)
    #         self._moteur.stop()
    #         self._servo.tourner_droite()
    #         time.sleep(0.06)
    #         self._servo.centrer()

    #     elif self.detecter_collision_avant() and self.detecter_collision_gauche():
    #         self._moteur.stop()
    #         time.sleep(1)
    #         self._moteur.reculer(-20)
    #         time.sleep(1)
    #         self._moteur.stop()
    #         time.sleep(1)
    #         self._servo.tourner_droite()
    #         self._moteur.avancer(20)
    #         time.sleep(1)
    #         self._moteur.stop()
    #         self._servo.tourner_gauche()
    #         time.sleep(0.06)
    #         self._servo.centrer()

    def aller_tout_droit(self):
        self._servo.centrer()
        self._moteur.avancer(20)

    def arreter_voiture(self):
        self._moteur.stop()
        self._servo.desactiver_pwm()
        self._etat_voiture = False  # Mettre à jour l'état de la voiture

    def compteur_tour(self, nb_tour):
        compte = nb_tour
        print(f"Nombre de tours restants : {compte}")
        while compte > 0:
            if not self._capteur_ligne.lire_donnee():
                print(f"Tour terminé. Tours restants : {compte - 1}")
                compte -= 1
                time.sleep(2)  # Pause pour éviter de détecter la même ligne plusieurs fois
        self.arreter_voiture()

    def course(self, nb_tour):

        # Thread pour détecter les collisions et éviter les obstacles
        thread_collision = Thread(target=self.detecter_collision)

        # Thread pour compter les tours
        thread_tours = Thread(target=self.compteur_tour, args=(nb_tour,))

        thread_mur = Thread(target=self.suivre_mur, args=("droite",))

        # Démarrage des threads
        thread_collision.start()
        thread_tours.start()
        thread_mur.start()

        # Attente de la fin des threads
        thread_collision.join()
        thread_tours.join()
        thread_mur.join()


# Création de l'objet voiture et démarrage de la course
voiture = Voiture("Vroum-Mobile")
voiture.course(3)
