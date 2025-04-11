import sys
import unittest
from unittest.mock import MagicMock, PropertyMock


sys.modules['board'] = MagicMock()
sys.modules['board'].SCL = MagicMock()
sys.modules['board'].SDA = MagicMock()

sys.modules['busio'] = MagicMock()
sys.modules['adafruit_tcs34725'] = MagicMock()

from classes.Capteur_RGB import Capteur_RGB  

class Test_Capteur_RGB(unittest.TestCase):
    """
    Classe qui permet de tester le code du capteur RGB que l'on utilise pour détecter la lumière verte et démarrer la voiture lors du
    passage du feu au vert. 
    """
    
    def setUp(self):
        self.mock_tcs = sys.modules['adafruit_tcs34725'].TCS34725.return_value
        type(self.mock_tcs).color_rgb_bytes = PropertyMock(return_value=(100, 150, 200))

        self.capteur = Capteur_RGB("test")

    def test_lire_donnee(self):
        result = self.capteur.lire_donnee()
        self.assertEqual(result, {"rouge": 100, "vert": 150, "bleu": 200})

    def test_detecter_couleur(self):
        self.assertEqual(self.capteur.detecter_couleur(), "Bleu")

if __name__ == '__main__':
    unittest.main()
