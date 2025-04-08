from gpiozero import AngularServo


class Servo_Moteur:
    """
    Classe pour contrôler un servo-moteur avec GPIOzero (sans pigpio).

    Attributs:
        nom (str): Nom du servo
        pin (int): Broche GPIO de contrôle
        angle (float): Angle courant (-90 à 90°)
        min_pulse (float): Largeur impulsion min (ms, défaut 0.5)
        max_pulse (float): Largeur impulsion max (ms, défaut 2.5)
    """

    def __init__(self, nom, pin, angle=0, min_pulse=0.5, max_pulse=2.5):
        self._nom = nom
        self._pin = pin
        self._angle = angle

        # Initialisation avec PWM natif
        self._servo = AngularServo(
            pin,
            min_angle=-90,
            max_angle=90,
            min_pulse_width=min_pulse / 1000,
            max_pulse_width=max_pulse / 1000,
            pin_factory=None  # Utilise le PWM par défaut
        )

        self.regler_angle(angle)

    def regler_angle(self, angle):
        """Règle l'angle (-90° à 90°)"""
        if -90 <= angle <= 90:
            self._angle = angle
            self._servo.angle = angle
            return angle
        raise ValueError("Angle doit être entre -90 et 90 degrés")

    def detacher(self):
        """Désactive le servo"""
        self._servo.detach()


# Exemple d'utilisation
if __name__ == '__main__':
    servo = Servo_Moteur(nom="Servo1", pin=17)
    servo.regler_angle(45)  # Tourne à 45°
    servo.regler_angle(-30)  # Tourne à -30°
    servo.detacher()