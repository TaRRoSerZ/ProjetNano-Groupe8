from classes.Capteur import Capteur
from gpiozero import DistanceSensor

class Capteur_Ultrasons(Capteur):
    def __init__(self, nom, pin_echo, pin_trig):
        super().__init__(nom)
        self._sensor = DistanceSensor(echo=pin_echo, trigger=pin_trig, max_distance=4)
        self._pin_echo = pin_echo
        self._pin_trig = pin_trig

    def lire_donnee(self):
        try:
            distance = self._sensor.distance
            if distance <= 0.02:
                return None
            return distance
        except Exception as e:
            print("erreur : " + str(e))