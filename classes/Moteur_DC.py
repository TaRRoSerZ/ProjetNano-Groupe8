import PCA9685 as PCA
import RPi.GPIO as GPIO

class Moteur_DC():
    """
        Classe représentant un moteur DC.

        Attributs:

        - nom (str): Le nom du moteur.



        Méthodes :

        avancer : permet au moteur d'avancer

        reculer : permet au mmoteur de reculer

        stop : permet d'arreter le moteur

        nettoyage_gpio : permet de nettoyer les pins gpio
        """

    def __init__(self,nom):
        self._noms = nom
        self.__moteur0_enable_pin = 4
        self.__moteur1_enable_pin = 5
        self.__moteur0_pin_a = 17
        self.__moteur1_pin_a = 27
        self.__moteur0_pin_b = 18
        self.__moteur1_pin_b = 22

        self.__gpio_pins = [
            self.__moteur0_pin_a,
            self.__moteur0_pin_b,
            self.__moteur1_pin_a,
            self.__moteur1_pin_b
        ]

        self.__pwm_controller = PCA.PWM()
        self.__pwm_controller.frequency = 60

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        for pin in self.__gpio_pins:
            GPIO.setup(pin, GPIO.OUT)

    def __appliquer_etat_moteur(self, pin_a, pin_b, pwm_value):
        GPIO.output(pin_a, GPIO.HIGH if pwm_value > 0 else GPIO.LOW)
        GPIO.output(pin_b, GPIO.LOW if pwm_value > 0 else GPIO.HIGH)
        channel = self.__moteur0_enable_pin if pin_a == self.__moteur0_pin_a else self.__moteur1_enable_pin
        self.__pwm_controller.write(channel, 0, int(abs(pwm_value)))

    def __convertir_vitesse(self, speed):
        """
        Convertit une vitesse de -100 à 100 en une valeur PWM comprise entre 0 et 4095.

        vitesse (positive pour avancer, négative pour reculer).
        retourne la valeur PWM correspondante.
        Lève une exception si la vitesse dépasse les bornes autorisées.
        """
        if speed > 100 or speed < -100:
            raise ValueError("La vitesse doit être comprise entre -100 et 100.")
        return speed * 4095 / 100

    def avancer(self, speed=100):
        pwm_val = self.__convertir_vitesse(speed)
        self.__appliquer_etat_moteur(self.__moteur0_pin_a, self.__moteur0_pin_b, pwm_val)
        self.__appliquer_etat_moteur(self.__moteur1_pin_a, self.__moteur1_pin_b, pwm_val)
        return 'La voiture avance'

    def reculer(self, speed=-100):
        pwm_val = self.__convertir_vitesse(speed)
        self.__appliquer_etat_moteur(self.__moteur0_pin_a, self.__moteur0_pin_b, pwm_val)
        self.__appliquer_etat_moteur(self.__moteur1_pin_a, self.__moteur1_pin_b, pwm_val)
        return 'La voiture recule'

    def stop(self):
        self.__appliquer_etat_moteur(self.__moteur0_pin_a, self.__moteur0_pin_b, 0)
        self.__appliquer_etat_moteur(self.__moteur1_pin_a, self.__moteur1_pin_b, 0)
        return 'La voiture est arretee'

    def nettoyage_gpio(self):
        GPIO.cleanup()

