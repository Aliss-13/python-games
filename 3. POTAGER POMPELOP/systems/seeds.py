from data.seeds import SEEDS


def get_seed(seed_id):
    return SEEDS.get(seed_id)


def get_all_seeds(state):
    return {
        id: seed
        for id, seed in SEEDS.items()
        if id in state.graines_disponibles
    }

