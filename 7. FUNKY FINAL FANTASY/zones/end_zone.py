
def is_zone_complete(game):
    return (
        game.current_zone.progress >= game.current_zone.total_progress
        and game.current_zone.boss_defeated
    )


def display_zone_end(game):

    zone = game.current_zone
    
    print()
    print("══════════════════════════════════════")
    print(f"       🌲 {zone.name.upper()} CONQUISE 🌲")
    print("══════════════════════════════════════")
    print()
    print(f"Vous avez traversé {zone.name}.")
    print()
    print("✨ Zone terminée !")
    print()
    print("Les créatures qui la hantaient ont été vaincues,")
    print("ses secrets ont été révélés,")
    print("et les habitants peuvent enfin respirer un peu.")
    print()
    print("              — FIN DE LA ZONE —")
    print()