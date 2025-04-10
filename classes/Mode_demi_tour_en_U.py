from Mode import Mode

class Mode_Grand8(Mode):
    def __init__(self):
        super().__init__()


    def executer(self):
        self._servo.centrer()
        print("La voiture se remet droite")
        self._moteur.avancer(30)
        print("La voiture avance")
        time.sleep(2)
        self._servo.tourner_droite()
        print("La voiture tourne à gauche")
        time.sleep(2)
        self._servo.centrer()
        print("La voiture se remet droite")
        time.sleep(2)
        print("La voiture s'arrête")
        self._moteur.stop()



