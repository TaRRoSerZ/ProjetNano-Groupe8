try:
    import RPi.GPIO as real_gpio
except ModuleNotFoundError:
    from unittest.mock import MagicMock
    real_gpio = MagicMock()

try:
    import PCA9685 as PCA
except ModuleNotFoundError:
    PCA = MagicMock()
    PCA.PWM = MagicMock()


class Moteur_DC():


    """
        Classe représentant un moteur DC.

        Attributs:
            - nom (str): Le nom du moteur.

        Méthodes :
            - avancer : permet au moteur d'avancer
            - reculer : permet au mmoteur de reculer
            - stop : permet d'arreter le moteur
            - nettoyage_gpio : permet de nettoyer les pins gpio
    """

    def __init__(self, nom, gpio_module=None, pwm_controller=None):


        self._noms = nom
        self.__moteur0_enable_pin = 4
        self.__moteur1_enable_pin = 5
        self.__moteur0_pin_a = 17
        self.__moteur1_pin_a = 27
        self.__moteur0_pin_b = 18
        self.__moteur1_pin_b = 22

        self.__gpio = gpio_module if gpio_module else real_gpio
        self.__pwm_controller = pwm_controller if pwm_controller else PCA.PWM()
        self.__pwm_controller.frequency = 60

        self.__gpio.setwarnings(False)
        self.__gpio.setmode(self.__gpio.BCM)

        self.__gpio_pins = [
            self.__moteur0_pin_a,
            self.__moteur0_pin_b,
            self.__moteur1_pin_a,
            self.__moteur1_pin_b
        ]

        for pin in self.__gpio_pins:
            self.__gpio.setup(pin, self.__gpio.OUT)

    def __appliquer_etat_moteur(self, pin_a, pin_b, pwm_value):
        self.__gpio.output(pin_a, self.__gpio.HIGH if pwm_value > 0 else self.__gpio.LOW)
        self.__gpio.output(pin_b, self.__gpio.LOW if pwm_value > 0 else self.__gpio.HIGH)
        channel = self.__moteur0_enable_pin if pin_a == self.__moteur0_pin_a else self.__moteur1_enable_pin
        self.__pwm_controller.write(channel, 0, int(abs(pwm_value)))

    def __convertir_vitesse(self, speed):
        if speed > 100 or speed < -100:
            raise ValueError("La vitesse doit être comprise entre -100 et 100.")
        return speed * 4095 / 100

    def avancer(self, speed=100):
        pwm_val = self.__convertir_vitesse(speed)
        self.__appliquer_etat_moteur(self.__moteur0_pin_a, self.__moteur0_pin_b, pwm_val)
        self.__appliquer_etat_moteur(self.__moteur1_pin_a, self.__moteur1_pin_b, pwm_val)
        return 'La voiture avance'

    def reculer(self, speed=-100):
        self.avancer(speed)
        return 'La voiture recule'

    def stop(self):
        self.__appliquer_etat_moteur(self.__moteur0_pin_a, self.__moteur0_pin_b, 0)
        self.__appliquer_etat_moteur(self.__moteur1_pin_a, self.__moteur1_pin_b, 0)
        return 'La voiture est arretee'

    def nettoyage_gpio(self):
        self.__gpio.cleanup()
