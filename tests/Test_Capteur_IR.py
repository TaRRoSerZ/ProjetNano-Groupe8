import unittest
from unittest.mock import Mock, patch
from classes.Capteur_IR import Capteur_IR


class Test_Capteur_IR(unittest.TestCase):
    """
    Test Unitaires concernant la classe Capteur_IR qui représente le capteur Infra rouge qui nous permet de gérer
    la détection de la ligne d'arrivée sur le module Voiture. 
    """

    @patch('classes.Capteur_IR.DigitalInputDevice')
    def test_lire_donnee_aucune_ligne(self, MockDigitalInputDevice):
        mock_capteur = MockDigitalInputDevice.return_value
        mock_capteur.value = not False
        capteur = Capteur_IR("capteur", 4)
        result = capteur.lire_donnee()
        exptected = False
        self.assertEqual(result, exptected)

    @patch('classes.Capteur_IR.DigitalInputDevice')
    def test_lire_donnee_ligne(self, MockDigitalInputDevice):
        mock_capteur = MockDigitalInputDevice.return_value
        mock_capteur.value = not True
        capteur = Capteur_IR("capteur", 4)
        result = capteur.lire_donnee()
        expected = True
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
