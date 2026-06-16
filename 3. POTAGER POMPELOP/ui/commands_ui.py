import systems.commands as commands
from core.event_handler import handle_events


def barre_progression(commande):
    
    if commande.temps_initial == 0:
        return "[■■■■■■■■■■]"

    ratio = 1 - (commande.temps_restant / commande.temps_initial)
    rempli = int(ratio * 10)
    vide = 10 - rempli

    return "[" + "█" * rempli + "-" * vide + "]"

def couleur_temps(commande):

    if commande.temps_initial == 0:
        return "🔴"

    ratio = commande.temps_restant / commande.temps_initial

    if ratio > 0.6:
        return "🟢"
    elif ratio > 0.3:
        return "🟡"
    else:
        return "🔴"


def nouvelle_commande_ui(state):
    result = commands.nouvelle_commande(state)

    if not result:
        print("⚠️ Erreur génération commande")
        return

    handle_events(result.get("events", []))

    if result.get("priority_command"):
        print("⚠️ COMMANDE PRIORITAIRE !")
    else:
        print("Nouvelle commande !")


def liste_commandes(state):
    print("\nCommandes en cours :")

    for commande in state.commandes_en_cours:
        statut = "PRIORITAIRE ⚠️" if commande.prioritaire else "normale"
        
        print(f"\nCommande {commande.id} ({statut})")
        
        print(f"Temps restant : {commande.temps_restant} {barre_progression(commande)} {couleur_temps(commande)}")

        for legume, quantite in commande.demande.items():
            print(f"- {legume} : {quantite}")

        print(f"Récompense : {commande.gain_xp} points d'expérience - {commande.pieces} pièces.")


def demander_int(message):
    
    try:
        valeur = input(message)
        if valeur.strip() == "":
            return None
        return int(valeur)
    except ValueError:
        return None
    

def commandes_lv(state, id_choisi):
    liste_commandes(state)
    result = commands.valider_commande(state, id_choisi)
    handle_events(result["events"])

    if result["status"] == "ok":
        print("Commande validée ✔")
    elif result["status"] == "not_found":
        print("Commande introuvable")
    elif result["status"] == "incomplete":
        print("Commande incomplète")


def gerer_commandes_ui(state):
    result = commands.gerer_commandes(state)
    handle_events(result["events"])


def valider_commande_ui(state):

    id_choisi = demander_int("ID de la commande : ")

    if id_choisi is None:
        print("Entrée invalide")
        return

    result = commands.valider_commande(state, id_choisi)
    handle_events(result["events"])

    if result["status"] == "ok":
        print("Commande validée ✔")

    elif result["status"] == "not_found":
        print("Commande introuvable")

    elif result["status"] == "incomplete":
        print("Commande incomplète")