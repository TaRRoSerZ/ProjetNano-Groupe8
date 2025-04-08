import unittest
from unittest.mock import patch
from classes.Servo_Moteur import Servo_Moteur


class Test_Servo_Moteur(unittest.TestCase):

    @patch('classes.Servo_Moteur.AngularServo')
    def test_angle_bon(self, AngularServo):
        mock_servo = AngularServo.return_value
        mock_servo.angle = 0
        servo = Servo_Moteur("servo", 4)
        result = servo.regler_angle(0)
        exptected = 0
        self.assertEqual(result, exptected)

    @patch('classes.Servo_Moteur.AngularServo')
    def test_angle_hors_valeur_acceptable(self, AngularServo):
        mock_servo = AngularServo.return_value
        servo = Servo_Moteur("capteur", 4)

        with self.assertRaises(ValueError):
            servo.regler_angle(100)


if __name__ == '__main__':
    unittest.main()
