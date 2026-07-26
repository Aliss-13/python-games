from data import ITEMS

# ----------------------------------------- Ajout, retrait, sélection dans l'inventaire --------------------------------------------------------

def add_item(inventory, item_id):
    
    item = ITEMS[item_id]

    inventory.append({
        "id": item_id,
        "name": item["name"],
        "type": item["type"],
        "rarity": item["rarity"],
        "quantity": 1
    })

def remove_item(inventory, index):
    if not isinstance(index, int):
        print("Index invalide :", index)
        return None

    return inventory.pop(index)


def get_item(inventory, choix):
    if not isinstance(choix, int):
        return None, None

    if choix < 0 or choix >= len(inventory):
        return None, None

    item = inventory[choix]

    if not isinstance(item, dict):
        return None, None

    item_id = item.get("id")

    if item_id not in ITEMS:
        return None, None

    return item_id, ITEMS[item_id]

# ----------------------------------------- Consommables --------------------------------------------------------

def apply_item_effect(player_team, item):
    
    effect = item.get("effect")
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

    item_id, item = get_item(inventory, choix)
    
    if item_id is None:
        return
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


def calcul_stats(character):
    stats = character.base_stats.copy()
    for stat, val in character.bonus.items():
        stats[stat] += val
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

    item_id, item = get_item(inventory, choix)
    
    if item_id is None:
        return
    
    if item["type"] == "consumable":
        print("Cet objet est un consommable.")
        return

    if character.character_class not in item["class"]:
        print("Classe incompatible")
        return

    slot = item["slot"]
    

    ancien_id = character.equipment.get(slot)
    ancien = ITEMS[ancien_id] if ancien_id else None

    if ancien:
        for stat, val in ancien["bonus"].items():
            character.bonus[stat] = character.bonus.get(stat,0) - val
            calcul_stats(character)

        inventory.append({
            "id": ancien_id,
            "name": ITEMS[ancien_id]["name"],
            "type": ITEMS[ancien_id]["type"],
            "rarity": ITEMS[ancien_id]["rarity"],
            "quantity": 1,
            "item_level": 1,
            "bonus": ITEMS[ancien_id]["bonus"]
        })

    character.equipment[slot] = item_id

    for stat, val in item["bonus"].items():
        character.bonus[stat] = character.bonus.get(stat,0) + val
        calcul_stats(character)
    
    remove_item(inventory, choix)

    item_name = ITEMS[item_id]["name"]

    print(f"{character.name} équipe {item_name}")