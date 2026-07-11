import traceback
from menu import menu
from witch import Witch
from garden import Garden, garden_levels
from save import load_game


def main():

    witch = Witch()
    garden = Garden(garden_levels)
    loaded = load_game(witch, garden)

    if not loaded:
        print("🦇 Nouvelle partie créée.")

    try:
        menu(witch, garden)
    
    except Exception as e:
        traceback.print_exc()
        input("Appuie sur entrée pour quitter")
    
    
print("\n★ ·. · ´¯` ·. · ★ LA MAGIQUE BOUTIQUE ★ ·. · ´¯` ·. ★")
print("\n·. · ★ « What sorcery is this ???? » ★ ·. · ")
print("")
print("DEBUG : godmode123")
main()