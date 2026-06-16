import random

def croissance_plantes(state):
    for plante in state.joueur.potager:
        plante.pousser()


def appliquer_temps(state):
    croissance_plantes(state)
    print("Le temps passe...")


def calculer_temps(graine):
    base = 2
    facteur = 2

    temps = base + graine.tier * facteur

    # petite variation pour éviter la monotonie
    return random.randint(temps, temps + 2)