import unittest
from unittest.mock import patch
from classes.Servo_Moteur import Servo_Moteur


class Test_Servo_Moteur(unittest.TestCase):
    """
    Classe de tests unitaires pour la classe Servo_Moteur.

    Méthodes:
        - test_angle_bon: Vérifie que la méthode regler_angle fonctionne correctement avec un angle valide.
        - test_angle_hors_valeur_acceptable: Vérifie que la méthode regler_angle lève une exception pour un angle invalide.
    """

    @patch('classes.Servo_Moteur.AngularServo')
    def test_angle_bon(self, AngularServo):
        """
        Teste si la méthode regler_angle retourne correctement l'angle réglé
        lorsqu'un angle valide est fourni.
        """
        mock_servo = AngularServo.return_value
        mock_servo.angle = 0
        servo = Servo_Moteur("servo", 4)
        result = servo.regler_angle(0)
        exptected = 0
        self.assertEqual(result, exptected)

    @patch('classes.Servo_Moteur.AngularServo')
    def test_angle_trop_haut(self, AngularServo):
        """
        Teste si la méthode regler_angle lève une exception ValueError
        lorsqu'un angle hors des limites (-90 à 90) est fourni.
        """
        servo = Servo_Moteur("capteur", 4)

        with self.assertRaises(ValueError):
            servo.regler_angle(100)

    @patch('classes.Servo_Moteur.AngularServo')
    def test_angle_trop_bas(self, AngularServo):
        """
        Teste si la méthode regler_angle lève une exception ValueError
        lorsqu'un angle hors des limites (-90 à 90) est fourni.
        """
        servo = Servo_Moteur("capteur", 4)

        with self.assertRaises(ValueError):
            servo.regler_angle(-1)


if __name__ == '__main__':
    unittest.main()