from systems.farming import planter, recolter, recolter_tout, appliquer_engrais
from data.data import boutique
from systems.inventory import retirer_item, afficher_inventaire
from systems.seeds import get_all_seeds
from core.event_handler import handle_events

RECOLTES = boutique["recoltes"]
ENGRAIS = boutique["engrais"]

def etat_plante(plante):

    if plante.est_pourrie():
        return "pourrie"

    if plante.est_prete():
        return "prête"

    return "pousse encore"


def planter_ui(state):

    graines = get_all_seeds(state)

    print("Graines disponibles :")

    for id_graine, graine in graines.items():
        print(
            f"{id_graine} - {graine.nom} "
            f"(tier {graine.tier}, prix {graine.prix})"
        )

    try:
        graine_id = int(input("ID graine : "))
    except ValueError:
        print("Entrée invalide")
        return

    result = planter(state, graine_id, quantite=1)

    if result["status"] == "ok":
        print("Planté ✔")

    elif result["status"] == "invalid_seed":
        print("Graine inconnue")

    elif result["status"] == "potager_plein":
        print("Pas assez de place")

    elif result["status"] == "pas_assez_pieces":
        print("Pas assez de pièces")

    print(f"Places restantes : {state.joueur.potager_max - len(state.joueur.potager)}")


def planter_multiple_ui(state):
    
    graines = get_all_seeds(state)

    print("Graines disponibles :")

    for id_graine, graine in graines.items():
        loots = ", ".join(
            f"{loot['nom']} ({int(loot['chance'] * 100)}%)"
            for loot in graine.loot
        )

        print(
            f"{id_graine} - {graine.nom} "
            f"(tier {graine.tier}, prix {graine.prix}) "
            f"→ {loots}"
        )

    try:
        graine_id = int(input("ID graine : "))
        quantite = int(input("Quantité : "))
    except ValueError:
        print("Entrée invalide")
        return

    result = planter(state, graine_id, quantite)

    if result["status"] == "ok":
        print("Planté ✔")
    elif result["status"] == "graine_invalide":
        print("Graine inconnue")
    elif result["status"] == "potager_plein":
        print("Pas assez de place")
    elif result["status"] == "pas_assez_pieces":
        print("Pas assez de pièces")

    print(f"Places restantes : {state.joueur.potager_max - len(state.joueur.potager)}")
 
    
def recolter_ui(state):

    for i, graine in enumerate(state.joueur.potager):
        print(f"{i} - {graine.nom}")

    try:
        choix = int(input("Index : "))
    except ValueError:
        print("Entrée invalide")
        return

    result = recolter(state, choix)
    handle_events(result["events"], state)


def recolter_tout_ui(state):

    result = recolter_tout(state)

    handle_events(result["events"], state)

    summary = result["summary"]

    total = summary["ok"] + summary["pourrie"]

    if total == 0:
        print("Aucune récolte.")
    else:
        print(
            f"{total} plante(s) récoltée(s) ✔ "
            f"({summary['ok']} ok, {summary['pourrie']} pourries)"
        )


def afficher_potager_ui(state):

    print(f"Capacité du potager : {state.joueur.potager_max - len(state.joueur.potager)} plantes.")

    if not state.joueur.potager:
        print("Rien ne pousse ici.")
        return

    for i, graine in enumerate(state.joueur.potager):

        etat = etat_plante(graine)

        print(f"{i} - {graine.nom} : {etat} ({graine.temps}/{graine.croissance})")
    
    
def afficher_garde_manger_ui(state):
    print("Garde-manger 🧺 :")
    for (nom, quantite) in (state.joueur.garde_manger.items()): # pour un dictionnaire
        print(f"- {nom} : {quantite}")


def afficher_bourse_ui(state):
    print(f"Bourse 💰 : {state.joueur.pieces}")


def utiliser_objet_ui(state):

    if not state.joueur.inventaire:
        print("Inventaire vide.")
        return

    afficher_inventaire(state)

    try:
        choix = int(input("Choisir objet : "))
    except ValueError:
        return

    nom_objet = list(state.joueur.inventaire.keys())[choix]

    objet = next(
        (i for i in ENGRAIS if i["nom"] == nom_objet),
        None
    )

    if not objet:
        print("Objet inconnu")
        return

    appliquer_engrais(state, objet["bonus"])
    retirer_item(state.joueur.inventaire, nom_objet)

    print(f"{nom_objet} utilisé ✔")
