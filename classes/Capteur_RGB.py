class Capteur_RGB:
    """
    Classe implémentant le fonctionnement des capteurs infrarouges.

    Attributs :

    nom : Nom du capteur
    capteur : Capteur venant du module adafruit_tcs34725

    Methodes :

    lire_donnee() : Renvoie la veleur de detection du capteur.
    detecter_couleur() : Renvoie la couleur la plus haute entre Rouge, Vert et Bleu
    """
    def __init__(self, nom):
        import board
        import busio
        import adafruit_tcs34725

        i2c = busio.I2C(board.SCL, board.SDA)
        self.capteur = adafruit_tcs34725.TCS34725(i2c)
        self.nom = nom

    def lire_donnee(self):
        """Méthode renvoyant un dictionnaire {rouge : int, vert : int, bleu : int) """
        rouge, vert, bleu = self.capteur.color_rgb_bytes
        return {"rouge": rouge, "vert": vert, "bleu": bleu}

    def detecter_couleur(self):
        """Méthode spécifiant quel couleur est la plus forte entre le rouge, le vert et le bleu"""
        data = self.lire_donnee()
        r, v, b = data["rouge"], data["vert"], data["bleu"]
        # Juste un exemple simple
        if r > v and r > b:
            return "Rouge"
        elif v > r and v > b:
            return "Vert"
        elif b > r and b > v:
            return "Bleu"
        else:
            return "Inconnu"