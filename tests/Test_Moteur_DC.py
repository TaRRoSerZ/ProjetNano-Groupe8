import unittest
from unittest.mock import MagicMock
from classes.Moteur_DC import Moteur_DC

class TestMoteurDC(unittest.TestCase):
    """
       Classe de tests unitaires pour la classe Moteur_DC.py.

       Méthodes:
           - test_avancer: Teste si la méthode avancer fonctionne correctement
           - test_reculer: Teste si la méthode reculer fonctionne correctement
           - test_stop: Teste si la méthode stop fonctionne correctement
           - test_convertir_vitesse: Teste la conversion de vitesse
       """
    def setUp(self):
        self.mock_gpio = MagicMock()
        self.mock_pwm = MagicMock()
        self.moteur = Moteur_DC("Moteur gauche", gpio_module=self.mock_gpio, pwm_controller=self.mock_pwm)

    def test_avancer(self):
        result = self.moteur.avancer(100)
        self.assertEqual(result, 'La voiture avance')
        self.assertTrue(self.mock_pwm.write.called)
        """
                Teste si la méthode avancer appelle correctement les fonctions GPIO et PWM
                avec les bonnes valeurs pour faire avancer le moteur.
        """

    def test_avancer_si_speed_plus_100(self):
        with self.assertRaises(ValueError):
            self.moteur.avancer(200)
            """
                Teste si la méthode avancer ne dépasse pas une vitesse de 100, si elle dépasse
                alors elle est bloquée à 100.
            """

    def test_avancer_si_speed_moins_1(self):
        with self.assertRaises(ValueError):
            self.moteur.avancer(0)
        """
                Teste si la méthode avancer n'est pas inférieur à 1 sinon elle se bloque à minimum 1
                pour qu'elle ne s'arrête pas.
        """

    def test_reculer(self):
        result = self.moteur.reculer(-100)
        self.assertEqual(result, 'La voiture recule')
        self.assertTrue(self.mock_pwm.write.called)
        """
        Teste si la méthode reculer() fait bien reculer la voiture à -100 prédéfini
        """

    def test_reculer_si_moins_100(self):
        with self.assertRaises(ValueError):
            self.moteur.reculer(-200)
            """
                   Teste si la méthode reculer() bloque la vitesse de recul à maximum -100 et ne la dépasse pas
            """

    def test_reculer_si_plus_1(self):
        with self.assertRaises(ValueError):
            self.moteur.reculer(1)
        """
               Teste si la méthode reculer() bloque la vitesse si elle est au dessus de -1
        """

    def test_stop(self):
        result = self.moteur.stop()
        self.assertEqual(result, 'La voiture est arretee')
        self.assertTrue(self.mock_pwm.write.called)
        """
             Teste si la méthode stop() fait bien arrêter la voiture
       """


if __name__ == '__main__':
    unittest.main()
