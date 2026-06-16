from data.graine import graines


def get_graine(state, graine_id):
    if graine_id not in state.graines_disponibles:
        return None
    return graines.get(graine_id)


def get_all_graines(state):
    return {
        id: g for id, g in graines.items()
        if id in state.graines_disponibles
    }

