import smbus2
from Capteur import Capteur


class Capteur_RGB(Capteur):
    """
    Classe pour le capteur TCS34725 utilisant smbus2 (sans dépendance Adafruit).
    """
    def __init__(self, nom, bus_num=1, address=0x29):
        super().__init__(nom)
        self._bus = smbus2.SMBus(bus_num)  # Bus I2C (1 pour Raspberry Pi)
        self._address = address  # Adresse I2C par défaut du TCS34725
        self._init_capteur()

    def _init_capteur(self):
        try:
            # Configuration du capteur (registres du TCS34725)
            self._bus.write_byte_data(self._address, 0x80 | 0x00, 0x03)  # Power ON
            self._bus.write_byte_data(self._address, 0x80 | 0x01, 0x2C)   # Temps d'intégration = 50 ms
            self._bus.write_byte_data(self._address, 0x80 | 0x0F, 0x00)   # Pas de gain
        except Exception as e:
            print(f"Erreur d'initialisation : {e}")
            self._bus = None

    def _lire_raw(self):
        """Lit les valeurs brutes R, G, B depuis le capteur."""
        if not self._bus:
            return (0, 0, 0)
        data = self._bus.read_i2c_block_data(self._address, 0x80 | 0x14, 6)
        r = data[1] << 8 | data[0]
        g = data[3] << 8 | data[2]
        b = data[5] << 8 | data[4]
        return (r, g, b)

    def lire_donnee(self):
        """Retourne les valeurs RGB normalisées (0-255)."""
        r, g, b = self._lire_raw()
        # Normalisation (ajustez selon vos besoins)
        max_val = max(r, g, b, 1)  # Évite la division par zéro
        return {
            "rouge": int((r / max_val) * 255),
            "vert": int((g / max_val) * 255),
            "bleu": int((b / max_val) * 255)
        }

    def detecter_couleur(self):
        """Détecte la couleur dominante (identique à votre version originale)."""
        couleur = self.lire_donnee()
        r, g, b = couleur["rouge"], couleur["vert"], couleur["bleu"]

        if r > 150 and g < 50 and b < 50:
            return "Rouge"
        elif g > 150 and r < 50 and b < 50:
            return "Vert"
        elif r > 150 and g > 50 and b < 50:
            return "Orange"
        else:
            return "Inconnu"

