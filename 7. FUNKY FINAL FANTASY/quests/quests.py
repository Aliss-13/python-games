import copy

from display import display_loot

from protagonists.level import level_up, xp_required
from protagonists.data_enemies import ENEMIES
from protagonists.utils_enemies import get_enemy_by_id

from inventory.data import ITEMS 
from inventory.inventory import add_item, unlock_shop
from inventory.item_generator import generate_item

from events.class_gameevent import GameEvent
from events.class_event import FOREST_EVENTS, get_event_by_flag

from quests.class_quest import Quest, FOREST_QUESTS, QUESTS_BY_TARGET


def create_quest(quest_id):

    original = FOREST_QUESTS[quest_id]

    if original is None:
        print(f"Quête inconnue : {quest_id}")
        return None

    return Quest(
        id=original.id,
        name=original.name,
        description=original.description,
        quest_type=original.quest_type,
        objectives=copy.deepcopy(original.objectives),
        reward_xp=original.reward_xp,
        zone_progress=original.zone_progress,
        reward_items=copy.deepcopy(original.reward_items)
    )


def start_quest(game, quest_id):

    for quest in game.active_quests:

        if quest.id == quest_id:
            return

    quest = create_quest(quest_id)

    if quest is None:
        return

    game.active_quests.append(quest)

    for item in game.inventory:
        if item["id"] in quest.objectives:
            quest.objectives_progress[item["id"]] = item.get("quantity", 1)

    print(f"📜 Nouvelle quête : {quest.name}")


def gain_xp_quest(game, quest):

    reward_xp = quest.reward_xp

    for character in game.player_team:

        character.xp += reward_xp

        print(f"{character.name} gagne {reward_xp} XP !")

        while character.xp >= xp_required(character.level):

            character.xp -= xp_required(character.level)

            level_up(character)


def complete_quest(game, quest):

    quest.completed = True

    print(f"✅ Quête terminée : {quest.name}")
    print("")

    game.completed_quests.append(quest)

    if quest in game.active_quests:
        game.active_quests.remove(quest)

    gain_xp_quest(game, quest)
    print("")

    rewards = []

    for item_id in quest.reward_items:

        item = generate_item(item_id, max(1, game.current_zone.progress))

        if item:
            rewards.append(item)

    add_loot(game, rewards)

    if rewards:
        display_loot(rewards)

    if quest.zone_progress:  # au cas où des quêtes ne donneraient pas de progression de zone
        game.current_zone.add_progress(quest.zone_progress)


def is_objective_complete(quest):

    if quest.quest_type == "kill_group":

        return quest.progress >= quest.objectives["required"]

    return all(
        quest.objectives_progress[key] >= value
        for key, value in quest.objectives.items()
    )


def add_loot(game, loot):

    for item in loot:

        add_item(game.inventory, item)

        process_game_event(
            game, 
            GameEvent(event_type="collect", target=item["id"], amount=item.get("quantity", 1))
        )

# ------------------------------------------------ Process game event -----------------------------------------------------------------------------
def process_game_event(game, event):
    
    # Déblocage automatique de quête
    if event.target in QUESTS_BY_TARGET:
        start_quest(game, QUESTS_BY_TARGET[event.target])


    # Gestion des événements spéciaux
    if event.event_type == "shop":
        unlock_shop(game, event.target)
        return {"type": "shop", "shop": event.target}


    # Traitement des quêtes
    for quest in game.active_quests:

        if quest.completed:
            continue
  
# ------------------------------------------------ kill_group
        if quest.quest_type == "kill_group":

            if event.event_type != "kill": # correspond à GameEvent
                continue

            if event.target not in quest.objectives["targets"]:
                continue

            quest.progress += event.amount

            print(
                f"╰┈> Quête avancée : {quest.name} "
                f"{quest.progress}/{quest.objectives['required']}"
            )

            if is_objective_complete(quest):
                complete_quest(game, quest)

# ------------------------------------------------ kill_each

        if quest.quest_type == "kill_each":

            if event.event_type != "kill": # correspond à GameEvent
                continue

            if event.target not in quest.objectives:
                continue

            quest.objectives_progress[event.target] += event.amount

            enemy = get_enemy_by_id(event.target, ENEMIES)
            enemy_name = enemy.name if enemy else event.target
            print(
                f"╰┈> Quête avancée : {quest.name} "
                f"({enemy_name})"
            )

            if is_objective_complete(quest):
                complete_quest(game, quest)

# ------------------------------------------------ discover_each

        if quest.quest_type == "discover_each":
        
            if event.event_type != "discovery":
                continue
        
            if event.target not in quest.objectives:
                continue
        
            quest.objectives_progress[event.target] += event.amount

            discovery_event = get_event_by_flag(event.target, FOREST_EVENTS)

            name = discovery_event.name if discovery_event else event.target

            print(
                f"╰┈> Quête avancée : {quest.name} "
                f"({name})"
            )

            if is_objective_complete(quest):
                complete_quest(game, quest)

# ------------------------------------------------ collect_each

        if quest.quest_type == "collect_each":

            if event.event_type != "collect":
                continue

            if event.target not in quest.objectives:
                continue

            name = ITEMS.get(event.target, {}).get("name", event.target)

            quest.objectives_progress[event.target] += event.amount

            print(
                f"╰┈> Quête avancée : {quest.name} "
                f"({name} "
                f"{quest.objectives_progress[event.target]}/"
                f"{quest.objectives[event.target]})"
            )

            if is_objective_complete(quest):
                complete_quest(game, quest)