

class Moteur_DC():
    """
        Classe représentant un moteur servo.

        Attributs:

        - nom (str): Le nom du moteur.
        - pins (dict): Dictionnaire des numéros de pins associés au moteur.
        - vitesse (int): La vitesse du moteur.
        - direction (str): La direction du moteur.

        Méthodes:

        - regler_vitesse :Actionne le moteur DC avec les données fournies.
        :param vitesse:

        -changer_direction :Change la direction du moteur DC.
        :param direction:
        """

    def __init__(self,nom,pins,vitesse,direction):
        self._noms = nom
        self._pins = pins
        self._vitesse = vitesse
        self._direction = direction


    def regler_vitesse(self, vitesse):
        """Règle la vitesse (0-100%)"""
        if 0 <= vitesse <= 100:
            self._vitesse = vitesse
            self._en.value = vitesse / 100
        else:
            raise ValueError("Vitesse doit être entre 0 et 100")


    def changer_direction(self, direction):
        """Change la direction"""
        if direction in ['avant', 'arrière']:
            self._direction = direction
            if direction == 'avant':
                self._in1.on()
                self._in2.off()
            else:
                self._in1.off()
                self._in2.on()
        else:
            raise ValueError("Direction doit être 'avant' ou 'arrière'")

    def arreter(self):
        """Arrête le moteur"""
        self._in1.off()
        self._in2.off()
        self._en.value = 0