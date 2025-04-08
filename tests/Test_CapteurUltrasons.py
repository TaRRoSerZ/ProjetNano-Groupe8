import unittest
from unittest.mock import patch, Mock
from classes.Capteur_Ultrasons import Capteur_Ultrasons


class Test_CapteurUltrasons(unittest.TestCase):
    """
       Classe de tests unitaires pour la classe `Capteur_Ultrasons`.

       Ces tests valident le comportement de la méthode `lire_donnee()` pour
       s'assurer que le capteur ultrasons fonctionne correctement dans les
       cas suivants :
       - Lorsque la distance mesurée est trop petite.
       - Lorsque la distance mesurée est normale.

       Méthodes de test :
           test_si_distance_trop_petite() : Teste si `lire_donnee()` retourne `None` pour une distance trop petite.
           test_si_distance_normale() : Teste si `lire_donnee()` retourne la distance correcte pour une mesure normale.
       """

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
