import random
from models.plante import Plante
from data.seeds import graines_disponibles as GR
from systems.seeds import get_seed

def get_graines_disponibles():
    return GR


def appliquer_engrais(state, bonus):

    for plante in state.joueur.potager:
        max_temps = plante.graine.croissance * 2
        plante.temps = min(plante.temps + bonus, max_temps)


def tirer_loot(loot_table):
    tirage = random.random()
    cumul = 0

    for item in loot_table:
        cumul += item["chance"]
        if tirage <= cumul:
            return item["nom"]

    return loot_table[-1]["nom"]


def planter(state, graine_id, quantite=1):

    events = []

    graine = get_seed(graine_id)

    if not graine:
        return {
            "status": "invalid_seed",
            "events": []
        }

    if len(state.joueur.potager) + quantite > state.joueur.potager_max:
        return {
            "status": "potager_plein",
            "events": []
        }

    total_prix = graine.prix * quantite

    if not state.joueur.payer(total_prix):
        return {
            "status": "pas_assez_pieces",
            "events": []
        }

    for _ in range(quantite):
        state.joueur.ajouter_plante(Plante.from_graine(graine))

    events.append({
        "type": "plant_seed",
        "graine_id": graine.id,
        "graine_nom": graine.nom,
        "quantite": quantite,
        "cost": total_prix
    })

    return {
        "status": "ok",
        "events": events
    }


def process_recolte(state, plante):
    
    events = []

    if plante.est_pourrie():
        return "pourrie", events

    if not plante.est_prete():
        return "pas_prete", events

    loot_nom = tirer_loot(plante.graine.loot)

    # mise à jour state
    state.joueur.garde_manger[loot_nom] = (
        state.joueur.garde_manger.get(loot_nom, 0) + 1
    )

    events.append({
        "type": "loot_received",
        "item": loot_nom
    })

    return "ok", events


def recolter(state, index):
    events = []

    potager = state.joueur.potager

    if index < 0 or index >= len(potager):
        return {
            "status": "invalid",
            "events": []
        }

    plante = potager[index]

    status, plant_events = process_recolte(state, plante)
    events += plant_events

    if status in ["ok", "pourrie"]:
        potager.pop(index)
        events.append({
            "type": "plant_removed",
            "reason": status,
            "index": index
        })

    return {
        "status": status,
        "events": events
    }


def recolter_tout(state):
    events = []

    potager = state.joueur.potager

    ok_count = 0
    pourrie_count = 0

    for plante in potager[:]:

        status, plant_events = process_recolte(state, plante)
        events += plant_events

        if status in ["ok", "pourrie"]:
            potager.remove(plante)

            events.append({
                "type": "plant_removed",
                "reason": status
            })

            if status == "ok":
                ok_count += 1
            else:
                pourrie_count += 1

    return {
        "status": "done",
        "summary": {
            "ok": ok_count,
            "pourrie": pourrie_count,
        },
        "events": events
    }