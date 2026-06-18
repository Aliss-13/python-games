def verifier_deblocage(state):

    events = []

    if state.joueur.niveau >= 2 and 2 not in state.graines_disponibles:
        state.graines_disponibles.add(2)
        events.append({"type": "unlock_seed", "seed": 2})

    if state.joueur.niveau >= 5 and 3 not in state.graines_disponibles:
        state.graines_disponibles.add(3)
        events.append({"type": "unlock_seed", "seed": 3})

    if state.joueur.niveau >= 7 and 4 not in state.graines_disponibles:
        state.graines_disponibles.add(4)
        events.append({"type": "unlock_seed", "seed": 4})

    if state.joueur.niveau >= 10 and 5 not in state.graines_disponibles:
        state.graines_disponibles.add(5)
        events.append({"type": "unlock_seed", "seed": 5})

    return events