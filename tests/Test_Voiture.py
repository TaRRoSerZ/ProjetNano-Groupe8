import unittest
from classes.Voiture import Voiture

class Test_Voiture(unittest.TestCase):
    def test_affichage_vitesse(self):
        voiture = Voiture("TestCar")
        voiture.vitesse = 0  # Modifie directement l'attribut vitesse
        self.assertEqual(voiture.affichage_vitesse(), print(f"Vitesse : {voiture.vitesse}"))

if __name__ == "__main__":
    unittest.main()