def choose_target(targets, title="Cibles"):

    if not targets:
        return None

    print(f"\n{title} :")

    for i, target in enumerate(targets):
        print(f"{i} - {target.name}")

    try:
        choice = int(input("> "))

    except ValueError:
        print("Choix invalide.")
        return None

    if choice < 0 or choice >= len(targets):
        print("Choix invalide.")
        return None

    return targets[choice]