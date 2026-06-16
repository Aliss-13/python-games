from systems.time import appliquer_temps
from ui.commands_ui import gerer_commandes_ui, nouvelle_commande_ui
from utils.save import sauvegarder
import random


def tour_suivant(state):
    print("\n⏳ --- TOUR SUIVANT ---")

    appliquer_temps(state)
    gerer_commandes_ui(state)

    print(f"📦 Commandes en cours : {len(state.commandes_en_cours)}")

    if len(state.commandes_en_cours) < 3 and random.random() < 0.5:
        print("🆕 Tentative de génération de commande...")
        nouvelle_commande_ui(state)
    
    if random.random() < 0.3:
        sauvegarder(state)
    