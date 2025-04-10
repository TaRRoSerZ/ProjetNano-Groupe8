import unittest
from unittest.mock import MagicMock
from classes.Moteur_DC import Moteur_DC

class TestMoteurDC(unittest.TestCase):

    def setUp(self):
        self.mock_gpio = MagicMock()
        self.mock_pwm = MagicMock()
        self.moteur = Moteur_DC("Moteur gauche", gpio_module=self.mock_gpio, pwm_controller=self.mock_pwm)

    def test_avancer(self):
        result = self.moteur.avancer(100)
        self.assertEqual(result, 'La voiture avance')
        self.assertTrue(self.mock_pwm.write.called)

    def test_avancer_si_speed_plus_100(self):
        with self.assertRaises(ValueError):
            self.moteur.avancer(200)

    def test_avancer_si_speed_moins_1(self):
        result = self.moteur.avancer(1)
        self.assertEqual(result, 'La voiture avance')

    def test_reculer(self):
        result = self.moteur.reculer(-100)
        self.assertEqual(result, 'La voiture recule')
        self.assertTrue(self.mock_pwm.write.called)

    def test_reculer_si_moins_100(self):
        with self.assertRaises(ValueError):
            self.moteur.reculer(-200)

    def test_reculer_si_plus_1(self):
        result = self.moteur.reculer(-1)
        self.assertEqual(result, 'La voiture recule')

    def test_stop(self):
        result = self.moteur.stop()
        self.assertEqual(result, 'La voiture est arretee')
        self.assertTrue(self.mock_pwm.write.called)


if __name__ == '__main__':
    unittest.main()
