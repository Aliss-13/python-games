def get_stats(entite):

    stats = entite.base_stats.copy()

    for key, value in entite.bonus.items():
        stats[key] = stats.get(key, 0) + value

    return stats