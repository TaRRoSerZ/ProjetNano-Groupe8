import unittest
from unittest.mock import patch, Mock
from classes.Capteur_Ultrasons import Capteur_Ultrasons


class Test_CapteurUltrasons(unittest.TestCase):

    @patch('classes.Capteur_Ultrasons.DistanceSensor')
    def test_si_distance_trop_petite(self, MockDistanceSensor):
        mock_sensor = MockDistanceSensor.return_value
        mock_sensor.distance = 0.01
        capteur = Capteur_Ultrasons("Capteur 1", 4, 2)
        result = capteur.lire_donnee()
        expected = None
        self.assertEqual(result, expected)

    @patch('classes.Capteur_Ultrasons.DistanceSensor')
    def test_si_distance_normale(self, MockDistanceSensor):
        mock_sensor = MockDistanceSensor.return_value
        mock_sensor.distance = 0.47
        capteur = Capteur_Ultrasons("Capteur 1", 4, 2)
        result = capteur.lire_donnee()
        expected = 0.47
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
