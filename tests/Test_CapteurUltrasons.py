import sys
import os
import unittest
import logging
from unittest.mock import patch, Mock

# Ajouter le répertoire 'classes' au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'classes')))

from classes.Capteur_Ultrasons import Capteur_Ultrasons
from classes.Loggeur import setupLoggeur, lireLogs


class Test_CapteurUltrasons(unittest.TestCase):
    """
       Classe de tests unitaires pour la classe `Capteur_Ultrasons`.

       Ces tests valident le comportement de la méthode `lire_donnee()` pour
       s'assurer que le capteur ultrasons fonctionne correctement dans les
       cas suivants :
       - Lorsque la distance mesurée est trop petite.
       - Lorsque la distance mesurée est normale.
       - Quand une valeur absurde est donnée.
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

    @patch('classes.Capteur_Ultrasons.DistanceSensor')
    def test_si_distance_absurde(self, MockDistanceSensor):
        mock_sensor = MockDistanceSensor.return_value
        mock_sensor.distance = "ddezdzedze"
        with self.assertRaises(ValueError):
            capteur = Capteur_Ultrasons("Capteur 1", 4, 2)
            capteur.lire_donnee()

lireLogs(3)

if __name__ == '__main__':
    unittest.main()
