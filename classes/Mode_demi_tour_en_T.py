from Mode import Mode

class Mode_Grand8(Mode):
    def __init__(self):
        super().__init__()


    def executer(self):
        self._servo.centrer()
        self._moteur.avancer(30)
        time.sleep(2)
        self._servo.tourner_gauche()
        time.sleep(2)
        self._moteur.stop()
        self._servo.centrer()
        time.sleep(2)
        self._servo.tourner_droite()
        time.sleep(2)
        self._moteur.reculer()
        time.sleep(2)
        self._moteur.stop()
        self._servo.centrer()
        self._moteur.avancer()
        time.sleep(2)
        self._moteur.stop()



