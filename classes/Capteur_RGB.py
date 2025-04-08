import board
import busio
import adafruit_tcs34725
from Capteur import Capteur


class Capteur_RGB(Capteur):
    """
    Classe représentant un capteur RGB basé sur le modèle TCS34725.

    Cette classe permet de lire les valeurs RGB et de détecter la couleur dominante en fonction des seuils définis.

    Attributs :
    ----------
    - capteur : adafruit_tcs34725.TCS34725
        Instance du capteur RGB TCS34725.
    - nom : str
        Nom du capteur.

    Methodes :

    Lire_donnee():
        Lit les valeurs RGB du capteur.

        Retourne :
        ---------
        dict
            Un dictionnaire contenant les valeurs des composantes rouge, vert et bleu.

    Detecter_couleur():
        Détecte la couleur dominante en fonction des seuils prédéfinis.

        Retourne :
        ---------
        str
            La couleur dominante détectée : "Rouge", "Vert", "Orange" ou "Inconnu".


    """

    def __init__(self, nom):
        super().__init__(nom)
        i2c = busio.I2C(board.SCL, board.SDA)
        try:
            self._capteur = adafruit_tcs34725.TCS34725(i2c)
            self._capteur.integration_time = 50  # Ajuste le temps d'intégration (ms)
        except (ValueError, RuntimeError) as e:
            print(f"Erreur d'initialisation du capteur : {e}")
            self._capteur = None

    def lire_donnee(self):
        if not self._capteur:
            return {"rouge": 0, "vert": 0, "bleu": 0}
        r, g, b = self._capteur.color_rgb_bytes
        return {"rouge": r, "vert": g, "bleu": b}

    def detecter_couleur(self):
        if not self._capteur:
            return "Capteur non initialisé"

        couleur = self.lire_donnee()
        r, g, b = couleur["rouge"], couleur["vert"], couleur["bleu"]

        # Seuils de détection des couleurs
        if r > 150 and g < 50 and b < 50:
            return "Rouge"
        elif g > 150 and r < 50 and b < 50:
            return "Vert"
        elif r > 150 and g > 50 and b < 50:
            return "Orange"
        else:
            return "Inconnu"