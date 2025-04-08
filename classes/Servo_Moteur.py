from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory  # Pour un PWM plus précis


class Servo_Moteur():
    """
    Classe pour contrôler un servo-moteur avec GPIOzero.

    Attributs:
        nom (str): Nom du servo
        pin (int): Broche GPIO de contrôle
        angle (float): Angle courant (en degrés)
        min_pulse (float): Largeur d'impulsion min (ms)
        max_pulse (float): Largeur d'impulsion max (ms)
    """

    def __init__(self, nom, pin, angle=0, min_pulse=0.5, max_pulse=2.5):
        self._nom = nom
        self._pin = pin
        self._angle = angle
        self._min_pulse = min_pulse
        self._max_pulse = max_pulse

        # Utilisation de PiGPIOFactory pour un PWM plus stable
        factory = PiGPIOFactory()

        # Initialisation du servo
        self._servo = Servo(
            pin,
            min_pulse_width=min_pulse / 1000,  # Conversion en secondes
            max_pulse_width=max_pulse / 1000,
            pin_factory=factory
        )

        # Applique l'angle initial
        self.regler_angle(angle)

    def regler_angle(self, angle):
        """
        Positionne le servo à un angle spécifique (entre -90 et 90 degrés)
        """
        if -90 <= angle <= 90:
            self._angle = angle
            # Conversion de l'angle (-90 à 90) en valeur (-1 à 1)
            valeur = angle / 90
            self._servo.value = valeur
        else:
            raise ValueError("L'angle doit être entre -90 et 90 degrés")

    def detacher(self):
        """
        Détache le servo (libère la broche PWM)
        """
        self._servo.detach()