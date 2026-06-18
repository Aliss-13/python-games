from core.state import GameState
from systems.menu import menu
from utils.save import safe_load_json, normalize_dict
from models.joueur import Joueur
import traceback


def charger_ou_creer():

    data = safe_load_json()
    

    if data is None:
        print("Création nouvelle sauvegarde 💾")
        state = GameState()
        state.joueur = Joueur()
        return state

    data = normalize_dict(data)

    if data is None:
        print("Sauvegarde corrompue → reset ↺ ")
        state = GameState()
        state.joueur = Joueur()
        return state

    print("Partie chargée ⌛️")
    return GameState.from_dict(data)
    

def main():
    try:
        state = charger_ou_creer()
        joueur = state.joueur
        menu(state, joueur)
    except Exception as e:
        print("Crash critique :", e)
        traceback.print_exc()
        input("Appuie sur entrée pour quitter")

if __name__ == "__main__":
    main()