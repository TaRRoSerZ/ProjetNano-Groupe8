import unittest
from unittest.mock import patch
from classes.Moteur_DC import Moteur_DC


class Test_Moteur_DC(unittest.TestCase):
    """
    Classe de tests unitaires pour la classe Moteur_DC.py.

    Méthodes:
        - test_avancer: Teste si la méthode avancer fonctionne correctement
        - test_reculer: Teste si la méthode reculer fonctionne correctement
        - test_stop: Teste si la méthode stop fonctionne correctement
        - test_convertir_vitesse: Teste la conversion de vitesse
    """

    @patch('classes.Moteur_DC.avancer')
    def test_avancer(self, speed=100):
        """
        Teste si la méthode avancer appelle correctement les fonctions GPIO et PWM
        avec les bonnes valeurs pour faire avancer le moteur.
        """
        moteur = Moteur_DC("Moteur gauche")
        result = moteur.avancer(speed)
        expected = 'La voiture avance'
        self.assertEqual(result, expected)

    def test_avancer_si_speed_plus_100(self, speed=200):
        """
                Teste si la méthode avancer ne dépasse pas une vitesse de 100, si elle dépasse
                alors elle est bloquée à 100.
        """
        moteur = Moteur_DC("Moteur gauche")
        result = moteur.avancer(speed)
        expected = moteur.avancer(speed=100)
        self.assertEqual(result, expected)

    def test_avancer_si_speed_moins_1(self, speed=0):
        """
                Teste si la méthode avancer n'est pas inférieur à 1 sinon elle se bloque à minimum 1
                pour qu'elle ne s'arrête pas.
        """
        moteur = Moteur_DC("Moteur gauche")
        result = moteur.avancer(speed)
        expected = moteur.avancer(speed=1)
        self.assertEqual(result, expected)


    @patch('classes.Moteur_DC.reculer')
    def test_reculer(self, speed=-100):
        """
        Teste si la méthode reculer() fait bien reculer la voiture à -100 prédéfini
        """
        moteur = Moteur_DC("Moteur gauche")
        result = moteur.reculer(speed)
        expected = 'La voiture recule'
        self.assertEqual(result, expected)

    def test_reculer_si_moins_100(self, speed=-200):
        """
               Teste si la méthode reculer() bloque la vitesse de recul à maximum -100 et ne la dépasse pas
        """
        moteur = Moteur_DC("Moteur gauche")
        result = moteur.reculer(speed)
        expected = moteur.reculer(speed=-100)
        self.assertEqual(result, expected)

    def test_reculer_si_plus_1(self, speed=-1):
        """
               Teste si la méthode reculer() bloque la vitesse si elle est au dessus de -1
        """
        moteur = Moteur_DC("Moteur gauche")
        result = moteur.reculer(speed)
        expected = moteur.reculer(speed=-100)
        self.assertEqual(result, expected)


    @patch('classes.Moteur_DC.stop')
    def test_stop(self):
        """
        Teste si la méthode stop() fait bien arrêter la voiture
        """
        moteur = Moteur_DC("Moteur gauche")
        result = moteur.stop()
        expected = 'La voiture est arretee'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()