import sac_a_dos
import ui
import skills
import affichage

def menu_inventaire(equipe, personnage, inventaire):
    affichage.afficher_equipement(personnage)
    while True:
        
        affichage.afficher_inventaire(inventaire)

        ui.section("Inventaire")
        print("[1] Équiper")
        print("[2] Utiliser objet")
        print("[3] Retour")

        choix = input("> ")

        if choix == "1":
            sac_a_dos.equiper_depuis_inventaire(personnage, inventaire)

        elif choix == "2":
            sac_a_dos.utiliser_objet(equipe, inventaire)

        elif choix == "3":
            return

        else:
            print("Choix invalide")

def menu_tour(personnage, equipe, ennemi, inventaire):

    while True:

        ui.section("Actions")
        print("[a] Attaquer")
        print("[s] Skill")
        print("[i] Inventaire")
        print("[q] Fin du tour")

        choix = input("> ").lower()

        # =====================
        # ATTAQUE
        # =====================
        if choix == "a":
            skills.attaque_basique(personnage, equipe, ennemi)
            return "fin_tour"

        # =====================
        # SKILL
        # =====================
        elif choix == "s":
            skills.use_skill(personnage, equipe, ennemi)
            return "fin_tour"

        # =====================
        # INVENTAIRE
        # =====================
        elif choix == "i":
            menu_inventaire(equipe, personnage, inventaire)
            # on reste dans le tour

        # =====================
        # FIN VOLONTAIRE
        # =====================
        elif choix == "q":
            return "fin_tour"

        else:
            print("Choix invalide")