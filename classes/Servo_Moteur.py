import PCA9685 as PCA



class Servo_Moteur:
    """
    Classe pour contrôler un servo-moteur avec le PCA9685.

    Attributs:
        nom (str): Nom du servo
        channel (int): Canal PWM du PCA9685
        angle (float): Angle courant (0 à 90°)
        min_pulse (float): Largeur impulsion min (ms, défaut 0.5)
        max_pulse (float): Largeur impulsion max (ms, défaut 2.5)
        pca (PCA9685): Contrôleur PWM
    """

    def __init__(self, nom):
        self._nom = nom
        self._channel = 0
        self._pulse = 320
        self._min_pulse = 200
        self._max_pulse = 500
        self._pca = PCA.PWM()
        self._pca.frequency = 60


    def regler_angle(self, angle):
        """Règle l'angle (0° à 90°)"""
        angle = max(0, min(180, angle)) + 20
        pulse = self._pulse + ((angle / 180.0) * (self._max_pulse - self._min_pulse))
        self._pca.write(0, 0, int(pulse))
        self.desactiver_pwm()

    def tourner_gauche(self):
        """Tourne à gauche (angle 0°)"""
        self.regler_angle(0)

    def tourner_droite(self):
        """Tourne à droite (angle 90°)"""
        self.regler_angle(90)

    def centrer(self):
        """Centre le servo (angle 45°)"""
        self.regler_angle(45)

    def desactiver_pwm(self):
        """
        Désactive la sortie PWM pour libérer le servo
        """
        self._pca.write(0, 0, 4096)
