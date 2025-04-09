from Mode import Mode
import unittest
from gpiozero import Device, InputDevice, OutputDevice
from gpiozero.pins.mock import MockFactory

#utilisation des broches simulées en attendant
Device.pin_factory = MockFactory()

class Mode_test(unittest.TestCase, Mode):
    """
    Classe représentant un mode de test basé sur les tests unitaires et la vérification des composants.

    Cette classe permet d'exécuter des tests unitaires dans un environnement de test, de déterminer l'état du système en fonction du succès ou de l'échec des tests, et de vérifier si les composants matériels sont actifs avant l'exécution des tests.

    Attributs :
    ----------
    - _result : bool
        Résultat des tests, True si tous les tests ont réussi, False sinon.
    - _mode : str
        Mode d'exécution des tests, qui peut être 'success' ou 'failure'.
    - _capteurs : dict
        Dictionnaire contenant les capteurs connectés avec leur nom comme clé et l'objet `InputDevice` comme valeur.

    Méthodes :
    ---------
    - is_active(composants) :
        Vérifie si un composant est actif.

        Args :
        ------
        - component (gpiozero.Device) : Le composant à vérifier.

        Retourne :
        ---------
        bool : True si le composant est actif, False sinon.

    - vérifier_composants() :
        Vérifie l'état de tous les composants et indique si tous sont actifs.

        Retourne :
        ---------
        bool : True si tous les composants sont actifs, False sinon.

    - executer() :
        Exécute les tests unitaires et vérifie l'état des composants avant l'exécution des tests.

        Retourne :
        ---------
        None
    """

    def __init__(self):
        super().__init__()
        self._result = None
        self._mode = None
        self._capteurs = {
            'Capteur_IR': InputDevice(4),  # broches gpio à changer
            'Capteur_RGB': InputDevice(17),
            'Capteur_Ultrasons': InputDevice(18)
        }

    @property
    def result(self):
        return self._result

    @property
    def mode(self):
        return self._mode

    @property
    def capteurs(self):
        return self._capteurs

    @result.setter
    def result(self, value):
        self._result = value

    @mode.setter
    def mode(self, value):
        self._mode = value


    def is_active(self, composant):
        """
        Vérifie si un composant est actif.

        Args:
            component (gpiozero.Device): Le composant à vérifier.

        Returns:
            bool: True si le composant est actif, False sinon.
        """
        try:
            if isinstance(composant, InputDevice):
                return composant.is_active
            return True
        except Exception as e:
            print(f"Erreur lors de la vérification du composant: {e}")
            return False

    def verifier_composants(self):
        """
        Vérifie l'état de tous les composants.

        Returns:
            bool: True si tous les composants sont actifs, False sinon.
        """
        all_active = True
        for nom, capteur in self.capteurs.items():
            if not self.is_active(capteur):
                print(f"Composant {nom} (GPIO {capteur.pin.number}) inactif !")
                all_active = False
        return all_active

    def executer(self):
        """
        Exécute les tests unitaires et vérifie l'état des composants.
        """
        composants_ok = self.verifier_composants()
        if not composants_ok:
            print("Alerte : Certains composants ne sont pas actifs !")

        loader = unittest.TestLoader()
        tests = loader.discover('tests')
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(tests)

        if result.wasSuccessful() and composants_ok:
            self._result = True
            self._mode = 'success'
            print("Tous les tests ont réussi et les composants sont actifs.")
        else:
            self._result = False
            self._mode = 'failure'
            if not result.wasSuccessful():
                print("Échec des tests unitaires.")
            if not composants_ok:
                print("Problème de composants inactifs.")