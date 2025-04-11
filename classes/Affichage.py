import time
from threading import Thread


class VoitureInterface:
    """

    Classe d'interface pour la voiture.
    Cette classe gère l'affichage et les interactions avec l'utilisateur.

    """
    def __init__(self, voiture):
        """
        Initialise l'interface de la voiture.
        """
        self.voiture = voiture
        self.thread_actif = True
        self.thread = Thread(target=self.mise_a_jour_capteurs)
        self.thread.daemon = True
        self.thread.start()

        self.demander_mode_initial()
        self.menu_principal()

    def mise_a_jour_capteurs(self):
        """
        Met à jour les données des capteurs et affiche leur état.
        """
        while self.thread_actif:
            for nom, capteur in self.voiture._capteurs.items():
                distance = capteur.lire_donnee()
                etat = "Actif" if distance is not None and distance < 0.15 else "Inactif"
                texte = f"{nom}: {etat}"
                if distance:
                    texte += f" ({distance:.1f} m)"

                # Afficher uniquement si un mode spécifique est actif
                if self.voiture.mode == "Test":  # Exemple de condition
                    print(texte)
            time.sleep(1)

    def demander_mode_initial(self):
        """
        Demande à l'utilisateur de choisir le mode initial.
        """
        print("Choix du mode initial :")
        print("1. Test")
        print("2. Course")
        print("3. Grand 8")
        print("4. Avant-Arrière")
        choix = input("Entrez le numéro du mode : ")
        modes = {"1": "Test", "2": "Course", "3": "Grand 8", "4": "Avant-Arrière"}
        mode = modes.get(choix)
        if mode:
            if mode == "Course":
                self.demander_tours()
            elif mode == "Test":
                for nom, capteur in self.voiture._capteurs.items():
                    actif = capteur.lire_donnee() is not None
                    print(f"{nom} : {'Actif' if actif else 'Inactif'}")
                return
            elif mode == "Grand 8":
                self.voiture.grand_8()
            elif mode == "Avant-Arrière":
                self.voiture.aller_tout_droit()
            self.voiture.definir_mode(mode)
            print(f"Mode {mode} activé.")
        else:
            print("Aucun mode sélectionné. Interface en attente.")

    def menu_principal(self):
        """
        Affiche le menu principal et gère les choix de l'utilisateur.
        """
        while True:
            print("\nMenu principal :")
            print("1. Changer de mode")
            print("2. Quitter le mode actuel")
            print("3. Réinitialiser la voiture")
            print("4. Quitter l'application")
            choix = input("Entrez votre choix : ")

            if choix == "1":
                self.changer_mode()
            elif choix == "2":
                self.quitter_mode()
            elif choix == "3":
                self.reset_module()
            elif choix == "4":
                self.fermer()
                break
            else:
                print("Choix invalide. Veuillez réessayer.")

    def changer_mode(self):
        """
        Change le mode de la voiture.
        """
        print("Choix du mode :")
        print("1. Test")
        print("2. Course")
        print("3. Grand 8")
        print("4. Avant-Arrière")
        choix = input("Entrez le numéro du mode : ")
        modes = {"1": "Test", "2": "Course", "3": "Grand 8", "4": "Avant-Arrière"}
        mode = modes.get(choix)
        if mode:
            self.voiture.arreter_voiture()
            if mode == "Course":
                self.demander_tours()
            elif mode == "Test":
                for nom, capteur in self.voiture._capteurs.items():
                    actif = capteur.lire_donnee() is not None
                    print(f"{nom} : {'Actif' if actif else 'Inactif'}")
                return
            elif mode == "Grand 8":
                self.voiture.grand_8()
            elif mode == "Avant-Arrière":
                self.voiture.aller_tout_droit()
            self.voiture.definir_mode(mode)
            print(f"Mode {mode} activé.")
            self.voiture.definir_mode(mode)
            print(f"Mode {mode} activé.")
        else:
            print("Mode invalide.")

    def demander_tours(self):
        """
        Demande à l'utilisateur le nombre de tours à effectuer.
        """
        try:
            tours = int(input("Entrez le nombre de tours à effectuer : "))
            self.voiture._nombre_tours = tours
            print(f"Nombre de tours défini à {tours}.")
        except ValueError:
            print("Entrée invalide. Le nombre de tours est défini à 1 par défaut.")
            self.voiture._nombre_tours = 1

    def quitter_mode(self):
        """
        Quitte le mode actuel de la voiture.
        """
        self.voiture.arreter_voiture()
        print("Le mode actuel a été quitté.")
        relancer = input("Souhaitez-vous choisir un nouveau mode ? (o/n) : ")
        if relancer.lower() == 'o':
            self.changer_mode()

    def reset_module(self):
        """
        Réinitialise le module de la voiture.
        """
        print("Redémarrage complet du module...")
        self.voiture.arreter_voiture()
        self.demander_mode_initial()

    def fermer(self):
        """
        Ferme l'application et arrête le thread de mise à jour des capteurs.
        """
        self.thread_actif = False
        self.thread.join()
        print("Application terminée.")
