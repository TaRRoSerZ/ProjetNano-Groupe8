from classes.Capteur import Capteur
from gpiozero import DistanceSensor
import logging
from Loggeur import setupLoggeur, lireLogs


setupLoggeur()

class Capteur_Ultrasons(Capteur):
    """
        Classe représentant un capteur à ultrasons, héritée de la classe `Capteur`.

        Cette classe utilise un capteur à ultrasons (via la classe `DistanceSensor` de gpiozero)
        pour mesurer la distance à un objet. Elle fournit une méthode pour obtenir la distance
        et une gestion des distances trop petites.

        Attributs :
            nom (str) : Le nom du capteur.
            _sensor (DistanceSensor) : Instance du capteur à ultrasons.
            _pin_echo (int) : Pin GPIO utilisé pour l'écho du capteur.
            _pin_trig (int) : Pin GPIO utilisé pour le déclenchement du capteur.

        Méthodes :
            lire_donnee() : Retourne la distance mesurée par le capteur, ou None si la distance est trop petite.
        """

    def __init__(self, nom, pin_echo, pin_trig):
        super().__init__(nom)
        self._sensor = DistanceSensor(echo=pin_echo, trigger=pin_trig, max_distance=4)
        self._pin_echo = pin_echo
        self._pin_trig = pin_trig

    def lire_donnee(self):
        try:
            distance = self._sensor.distance
            if not isinstance(distance, (int, float)):
                raise ValueError(f"Distance invalide reçue: {distance}")

            if distance <= 0.02:
                logging.warning(f"Distance trop petite pour le capteur {self.nom}: {distance} m.")
                return None

            logging.info(f"Distance mesurée pour le capteur {self.nom}: {distance} m.")
            return distance
        except ValueError as e:
            logging.error(f"Erreur de valeur lors de la lecture du capteur {self.nom}: {str(e)}.")
            raise

        except Exception as e:
            logging.error(f"Erreur lors de la lecture du capteur {self.nom}: {str(e)}.")
            raise

lireLogs(5)
