import unittest
from unittest.mock import patch, Mock
from classes.Capteur_RGB import Capteur_RGB


class Test_Capteur_RGB(unittest.TestCase):
    """
    Classe de tests unitaires pour la classe `Capteur_RGB`.

    Ces tests valident le comportement des méthodes `lire_donnee()` et
    `detecter_couleur()` afin de s'assurer que le capteur RGB fonctionne
    correctement dans les cas suivants :

    - Lorsque la lecture de la couleur retourne des valeurs valides.
    - Lorsqu'une exception survient pendant la lecture (par exemple, capteur non détecté).
    - Lorsque les valeurs RGB permettent d'identifier correctement une couleur (ex : rouge).

    """
    @patch('classes.Capteur_RGB.TCS34725')
    def test_lire_donnee(self, MockTCS34725):
        mock_capteur = MockTCS34725.return_value
        mock_capteur.color_rgb_bytes = (10, 20, 30)
        capteur = Capteur_RGB("capteur")
        result = capteur.lire_donnee()
        expected = {"rouge": 10, "vert": 20, "bleu": 30}
        self.assertEqual(result, expected)

    @patch('classes.Capteur_RGB.TCS34725')
    def test_lire_donnee_exception(self, MockTCS34725):
        mock_capteur = MockTCS34725.return_value
        mock_capteur.color_rgb_bytes.side_effect = Exception("Erreur de lecture")
        capteur = Capteur_RGB("capteur")
        result = capteur.lire_donnee()
        expected = {"rouge": 0, "vert": 0, "bleu": 0}
        self.assertEqual(result, expected)

    @patch('classes.Capteur_RGB.TCS34725')
    def test_detecter_couleur(self, MockTCS34725):
        mock_capteur = MockTCS34725.return_value
        mock_capteur.color_rgb_bytes = (200, 50, 50)
        capteur = Capteur_RGB("capteur")
        result = capteur.detecter_couleur()
        expected = "Rouge"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

