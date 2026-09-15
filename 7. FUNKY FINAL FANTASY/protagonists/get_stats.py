from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from protagonists.class_character import Character


def get_stats(entite: Character) -> dict[str, int]:

    stats = entite.base_stats.copy()

    for key, value in entite.bonus.items():
        stats[key] = stats.get(key, 0) + value

    return stats