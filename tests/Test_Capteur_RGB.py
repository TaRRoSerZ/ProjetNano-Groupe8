import unittest
from unittest.mock import patch, Mock
from classes.Capteur_RGB import Capteur_RGB


class Test_Capteur_RGB(unittest.TestCase):
    """
    Classe de tests unitaires pour la classe `Capteur_RGB`.
    """

    @patch('classes.Capteur_RGB.TCS34725')
    def test_lire_donnee_valeurs_valides(self, MockTCS34725):
        mock_capteur = MockTCS34725.return_value
        mock_capteur.color_rgb_bytes = (10, 20, 30)
        capteur = Capteur_RGB("capteur")
        result = capteur.lire_donnee()
        expected = {"rouge": 10, "vert": 20, "bleu": 30}
        self.assertEqual(result, expected)
        mock_capteur.color_rgb_bytes.__get__.assert_called_once()

    @patch('classes.Capteur_RGB.TCS34725')
    def test_lire_donnee_exception(self, MockTCS34725):
        mock_capteur = MockTCS34725.return_value
        mock_capteur.color_rgb_bytes.side_effect = Exception("Erreur de lecture")
        capteur = Capteur_RGB("capteur")
        result = capteur.lire_donnee()
        expected = {"rouge": 0, "vert": 0, "bleu": 0}
        self.assertEqual(result, expected)
        mock_capteur.color_rgb_bytes.__get__.assert_called_once()

    @patch('classes.Capteur_RGB.TCS34725')
    def test_detecter_couleur_rouge(self, MockTCS34725):
        mock_capteur = MockTCS34725.return_value
        mock_capteur.color_rgb_bytes = (200, 50, 50)
        capteur = Capteur_RGB("capteur")
        result = capteur.detecter_couleur()
        expected = "Rouge"
        self.assertEqual(result, expected)
        mock_capteur.color_rgb_bytes.__get__.assert_called_once()

    @patch('classes.Capteur_RGB.TCS34725')
    def test_detecter_couleur_valeurs_extremes(self, MockTCS34725):
        mock_capteur = MockTCS34725.return_value
        mock_capteur.color_rgb_bytes = (255, 255, 255)
        capteur = Capteur_RGB("capteur")
        result = capteur.detecter_couleur()
        expected = "Blanc"  # Exemple de couleur pour des valeurs maximales
        self.assertEqual(result, expected)
        mock_capteur.color_rgb_bytes.__get__.assert_called_once()


if __name__ == '__main__':
    unittest.main()