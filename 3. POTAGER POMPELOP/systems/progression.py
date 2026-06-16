from data.graine import graines, graines_disponibles
from systems.unlock import verifier_deblocage
from core.event_handler import handle_events

def debloquer_graine(nom, tier, croissance, prix, loot):
 
    # vérifier si déjà existant
    for graine in graines_disponibles.values():
        if graine.nom == nom:
            return  # déjà débloquée

    next_id = max(graines_disponibles.keys()) + 1

    graines_disponibles[next_id] = {
        "nom": nom,
        "croissance": croissance,
        "tier" : tier,
        "prix": prix,
        "loot" : graines.get(loot, [])
    }

def verifier_level_up(state):

    events = []

    while True:
        seuil = state.joueur.niveau * 10

        if state.joueur.xp < seuil:
            break

        state.joueur.xp -= seuil
        state.joueur.niveau += 1

        events.append({
            "type": "level_up",
            "niveau": state.joueur.niveau
        })

    unlock_events = verifier_deblocage(state)
    events += unlock_events

    return events