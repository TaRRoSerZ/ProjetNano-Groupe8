class Capteur_RGB:
    def __init__(self, nom):
        import board
        import busio
        import adafruit_tcs34725

        i2c = busio.I2C(board.SCL, board.SDA)
        self.capteur = adafruit_tcs34725.TCS34725(i2c)
        self.nom = nom

    def lire_donnee(self):
        rouge, vert, bleu = self.capteur.color_rgb_bytes
        return {"rouge": rouge, "vert": vert, "bleu": bleu}

    def detecter_couleur(self):
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