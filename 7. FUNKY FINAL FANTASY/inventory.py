from data import ITEMS

# ----------------------------------------- Ajout, retrait, sélection dans l'inventaire --------------------------------------------------------

def add_item(inventory, item):
    inventory.append(item.copy())


def remove_item(inventory, index):
    if not isinstance(index, int):
        print("Index invalide :", index)
        return None

    return inventory.pop(index)


def get_item(inventory, choix):

    if choix < 0 or choix >= len(inventory):
        return None

    item = inventory[choix]

    if not isinstance(item, dict):
        return None

    return item

# ----------------------------------------- Consommables --------------------------------------------------------

def apply_item_effect(player_team, item):
    
    effect = item.get("effect")

    for character in player_team:
        stats = get_stats(character)

    if effect == "gain_pv":
        allies = [character for character in player_team if character.life > 0 and character.life < stats["life_max"]]

        if not allies:
            return
        
        target = min(allies, key=lambda character: character.life/stats["life_max"])
        # key (= critère de comparaison) lambda range les personnages en fonction de leur pourcentage de vie
        # cible le personnage qui a le moins de vie en pourcentage
        stats_target = get_stats(target)
        healing = item["healing"]
        life_before_heal = target.life
        target.life = min(target.life + healing, stats_target["life_max"])
        real_healing = target.life - life_before_heal

        if real_healing > 0:
            print(f"{target.name} gagne {real_healing} PV → PV : {target.life}/{stats_target["life_max"]} !")

        if real_healing == 0:
            print(f"{target.name} est déjà au maximum de ses PV !")


    if effect == "resurrection":
        
        dead = [character for character in player_team if character.life <= 0]
        if not dead:
            print("Personne à ressusciter.")
            return

        print("\nCibles :")

        for i, character in enumerate(dead):
            print(f"{i} - {character.name}")

            try:
                target_choice = int(input("Choisir cible : "))
            except ValueError:
                return
    
            target = dead[target_choice]
            stats_target = get_stats(target)
            target.life = min(item["healing"], stats_target["life_max"])
            print(f"{target.name} revient à la vie avec {item['healing']} PV !")


def use_item(player_team, inventory):

    try:
        choix = int(input("Choisir numéro de l'objet :"))
    except ValueError:
        print("Entrée invalide.")
        return

    if choix < 0 or choix >= len(inventory):
        print("Choix invalide.")
        return

    item = get_item(inventory, choix)

    if item is None:
        return

    item_id = item["id"]
    
    if item["type"] != "consumable":
        print("Cet objet n'est pas un consommable.")
        return
    
    apply_item_effect(player_team, item)
    
    remove_item(inventory, choix)
    print(f"{ITEMS[item_id]["name"]} disparaît de l'inventaire !")

# ----------------------------------------- Statistiques de base + bonus --------------------------------------------------------

def get_stats(entite):

    stats = entite.base_stats.copy()

    for key, value in entite.bonus.items():
        stats[key] = stats.get(key, 0) + value

    return stats


def get_item_stats(item):

    data = ITEMS[item["id"]]

    level = item.get("item_level", 1)

    stats = {}

    for stat, value in data["bonus"].items():

        scaling = data.get("scaling", {}).get(stat, 0)

        stats[stat] = value + int(level * scaling)

    return stats
    
# ----------------------------------------- Equipement --------------------------------------------------------

def equip_from_inventory(character, inventory):

    try:
        choix = int(input("Choisir numéro de l'objet :"))
    except ValueError:
        print("Entrée invalide.")
        return

    if choix < 0 or choix >= len(inventory):
        print("Choix invalide.")
        return

    item_inv = inventory[choix] # objet réel (avec item_level et bonus scalés)
    item_id, item_data = get_item(inventory, choix) # données de base (slot, classe, etc.)

    if item_id is None:
        return

    if item_data["type"] == "consumable":
        print("Cet objet est un consommable.")
        return

    if character.character_class not in item_data["class"]:
        print("Classe incompatible")
        return

    slot = item_data["slot"]

    ancien = character.equipment.get(slot)

    if ancien:
        for stat, val in ancien["bonus"].items():
            character.bonus[stat] -= val
        inventory.append(ancien.copy())

    character.equipment[slot] = item_inv.copy()

    for stat, val in item_inv["bonus"].items():
        character.bonus[stat] += val

    remove_item(inventory, choix)

    print(f"{character.name} équipe {item_data['name']}")