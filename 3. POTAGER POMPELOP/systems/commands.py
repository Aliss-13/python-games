import random
from models.commande import Commande
from systems.seeds import get_all_seeds
from systems.progression import verifier_level_up, update_prestige

def generer_commande(state):

    commande = Commande(
        id=None,
        demande={},
        gain_xp=0,
        pieces=0,
        tier_max=0,
        temps_restant=0
    )

    tier_max = min(1 + state.joueur.niveau // 2, 5)
    commande.tier_max = tier_max

    taille = random.randint(1, 3)
    temps_total = 0

    all_seeds = get_all_seeds(state)

    for _ in range(taille):

        candidates = [
            g for g in all_seeds.values()
            if g.tier <= tier_max
        ]

        if not candidates:
            raise ValueError("Aucune graine disponible pour ce tier")

        graine = random.choice(candidates)

        if not graine.loot:
            continue

        quantite = random.randint(1, 3)
        nom = random.choice(graine.loot)["nom"]

        commande.demande[nom] = commande.demande.get(nom, 0) + quantite

        commande.gain_xp += graine.tier * 6
        commande.pieces += graine.tier * 10

        temps_total += graine.croissance * quantite

    commande.temps_restant = max(temps_total, 1)

    return commande


def nouvelle_commande(state):

    events = []

    commande = generer_commande(state)

    if not commande:
        return {
        "status": "empty",
        "events": []
    }


    state.next_commande_id += 1
    commande.id = state.next_commande_id

    commande.temps_restant = max(commande.temps_restant, 3)
    commande.temps_initial = commande.temps_restant

    if random.random() < 0.25:
        commande.prioritaire = True
        commande.pieces *= 2
        events.append({"type": "priority_command"})

    state.commandes_en_cours.append(commande)

    return {"status": "ok", "events": events}
    

def gerer_commandes(state):

    events = []

    for commande in state.commandes_en_cours[:]:
        if commande.temps_restant <= 0:
            state.commandes_en_cours.remove(commande)

            events.append({
                "type": "command_expired",
                "id": commande.id
            })

    return {"status": "ok", "events": events}


def trouver_commande_par_id(state, id_choisi):
    for commande in state.commandes_en_cours:
        if commande.id == id_choisi:
            return commande
    return None


def valider_commande(state, id_choisi):

    events = []

    commande = next(
        (c for c in state.commandes_en_cours if c.id == id_choisi),
        None
    )

    if not commande:
        return {
            "status": "not_found",
            "events": []
        }
    
    for legume, quantite in commande.demande.items():
        if state.joueur.garde_manger.get(legume, 0) < quantite:
            return {
                "status": "incomplete",
                "events": []
            }

    for legume, quantite in commande.demande.items():
        state.joueur.garde_manger[legume] -= quantite
        if state.joueur.garde_manger[legume] <= 0:
            del state.joueur.garde_manger[legume]

    valeur_prestige = commande.gain_xp + int(commande.pieces * 0.5)

    if commande.prioritaire:
        valeur_prestige = int(valeur_prestige * 1.5)
    
    state.joueur.ajouter_xp(commande.gain_xp)
    state.joueur.ajouter_pieces(commande.pieces)
    state.joueur.prestige += valeur_prestige
    update_prestige(state)

    state.commandes_en_cours.remove(commande)

    events.append({
        "type": "command_completed",
        "data": {
            "id": commande.id,
            "xp": commande.gain_xp,
            "pieces": commande.pieces,
            "prioritaire": commande.prioritaire
        }
    })

    
    
    events += verifier_level_up(state)
    
    return {
            "status": "ok",
            "events": events
    }
    