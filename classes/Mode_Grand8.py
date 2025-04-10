from Mode import Mode

class Mode_Grand8(Mode):
    def __init__(self):
        super().__init__()


    def executer(self):
        self._servo.centrer()
        self._moteur.avancer(30)
        time.sleep(2)
        self._servo._tourner_droite()
        time.sleep(4)
        self._servo._tourner_gauche()
        time.sleep(4)
        self._moteur.stop()

