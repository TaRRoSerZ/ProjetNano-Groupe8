import unittest
from unittest.mock import patch
from classes.Servo_Moteur import Servo_Moteur


class Test_Servo_Moteur(unittest.TestCase):
    """
    Classe de tests unitaires pour la classe Servo_Moteur.

    Méthodes:
        - test_regler_angle: Teste la méthode regler_angle pour un angle valide.
        -tourner_gauche: Teste la méthode tourner_gauche.
        - tourner_droite: Teste la méthode tourner_droite.
        - centrer: Teste la méthode centrer.
        - desactiver_pwm: Teste la méthode desactiver_pwm.
    """

    def setUp(self, mock_pwm):
        """ Initialise un objet Servo_Moteur pour les tests."""
        patcher = patch('classes.PCA9685.PWM')
        self.mock_pwm_class = patcher.start()
        self.addCleanup(patcher.stop)
        self.servo = Servo_Moteur("servo_test")

    def test_regler_angle(self, mock_pwm):
        """Test la méthode regler_angle pour un angle valide."""

        angle = 90
        self.servo.regler_angle(angle)

        expected_value = int(self.servo._pulse + ((angle / 180.0) * (self.servo._max_pulse - self.servo._min_pulse)))
        self.mock_pwm_class.return_value.write.assert_called_once_with(0, 0, expected_value)

    def test_tourner_gauche(self, mock_pwm):
        """Teste la méthode tourner_gauche."""

        angle = 0
        self.servo.tourner_gauche()

        expected_value = int(self.servo._pulse + ((angle / 180.0) * (self.servo._max_pulse - self.servo._min_pulse)))
        self.mock_pwm_class.return_value.write.assert_called_once_with(0, 0, expected_value)

    def test_tourner_droite(self, mock_pwm):
        """Teste la méthode tourner_droite."""

        angle = 90
        self.servo.tourner_droite()

        expected_value = int(self.servo._pulse + ((angle / 180.0) * (self.servo._max_pulse - self.servo._min_pulse)))
        self.mock_pwm_class.return_value.write.assert_called_once_with(0, 0, expected_value)

    def test_centrer(self, mock_pwm):
        """Teste la méthode centrer."""

        angle = 45
        self.servo.centrer()

        expected_value = int(self.servo._pulse + ((angle / 180.0) * (self.servo._max_pulse - self.servo._min_pulse)))
        self.mock_pwm_class.return_value.write.assert_called_once_with(0, 0, expected_value)

    def test_desactiver_pwm(self, mock_pwm):
        """Teste la méthode desactiver_pwm."""

        self.servo.desactiver_pwm()
        self.mock_pwm_class.return_value.write.assert_called_once_with(0, 0, 4096)


if __name__ == '__main__':
    unittest.main()