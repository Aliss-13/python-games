import copy
from display import display_loot

from events.class_gameevent import GameEvent
from events.class_event import FOREST_EVENTS, get_event_by_flag

from quests.data_quests import FOREST_QUESTS, QUESTS_BY_TARGET
from quests.class_quest import Quest
from quests.unlock_dialogues import unlock_dialogues_for_quest

from protagonists.data_enemies import ENEMIES
from protagonists.utils_enemies import get_enemy_by_id
from protagonists.level import level_up, xp_required, average_level

from inventory.data import ITEMS 
from inventory.inventory import unlock_shop, remove_item_by_id, add_item, get_item_quantity
from inventory.item_generator import generate_item


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

    # déjà terminée ?
    if any(quest.id == quest_id for quest in game.completed_quests):
        return False

    # déjà active ?
    if any(quest.id == quest_id for quest in game.active_quests):
        return False

    quest = create_quest(quest_id)

    if quest is None:
        return

    game.active_quests.append(quest)

    for item in game.inventory:
        if item["id"] in quest.objectives:
            quest.objectives_progress[item["id"]] = item.get("quantity", 1)

    print(f"📜 Nouvelle quête : {quest.name}")
    
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

            if is_objective_complete(game, quest):
                complete_quest(game, quest)

# ------------------------------------------------ kill_each

        if quest.quest_type == "kill_each":

            if event.event_type != "kill":
                continue

            if event.target not in quest.objectives:
                continue

            enemy = get_enemy_by_id(event.target, ENEMIES)
            enemy_name = enemy.name if enemy else event.target

            if enemy and enemy.is_unique:
                progress = (1 if event.target in game.defeated_unique_enemies else 0)

            else:
                quest.objectives_progress[event.target] += event.amount
                progress = quest.objectives_progress[event.target]

            print(f"╰┈> Quête avancée : {quest.name} ({enemy_name} {progress}/{quest.objectives[event.target]})")

            if is_objective_complete(game, quest):
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

            if is_objective_complete(game, quest):
                complete_quest(game, quest)

# ------------------------------------------------ collect_each

        if quest.quest_type == "collect_items":

            if event.event_type != "collect":
                continue

            if event.target not in quest.objectives:
                continue

            name = ITEMS.get(event.target, {}).get("name", event.target)
            progress = quest.get_inventory_progress(game)
            count = progress[event.target]
            required = quest.objectives[event.target]

            print(
                    f"╰┈> Quête avancée : {quest.name} "
                    f"({name} {count}/{required})"
            )

            if is_objective_complete(game, quest):
                complete_quest(game, quest)


def generate_quest_reward(item_id, game):
    item_level = max(1, int(average_level(game.player_team)) - 1)

    return generate_item(
        item_id,
        item_level=item_level
    )

         
def complete_quest(game, quest):

    unlock_dialogues_for_quest(game, quest.id)

    # Retirer les objets consommés par la quête
    if quest.quest_type == "collect_items":
        for item_id, amount in quest.objectives.items():
            remove_item_by_id(game.inventory, item_id, amount)

    progress = quest.get_progress(game)
    quest.objectives_progress.update(progress)
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

        item = generate_quest_reward(item_id, game)

        if item:
            rewards.append(item)

    add_loot(game, rewards)

    if rewards:
        display_loot(rewards)

    if quest.zone_progress:  # au cas où des quêtes ne donneraient pas de progression de zone
        game.current_zone.add_progress(quest.zone_progress)


def get_objective_progress(game, quest):

    if quest.quest_type == "collect_items":

        progress = {}

        for item_id, required in quest.objectives.items():
            progress[item_id] = get_item_quantity(
                game.inventory,
                item_id
            )

        return progress

    return quest.objectives_progress


def is_objective_complete(game, quest):

    if quest.quest_type == "kill_group":
        return quest.progress >= quest.objectives["required"]

    progress = quest.get_progress(game)

    return all(
        progress[key] >= value
        for key, value in quest.objectives.items()
    )


def gain_xp_quest(game, quest):

    reward_xp = quest.reward_xp

    for character in game.player_team:

        character.xp += reward_xp

        print(f"{character.name} gagne {reward_xp} XP !")

        while character.xp >= xp_required(character.level):

            character.xp -= xp_required(character.level)

            level_up(character)


def add_loot(game, loot):

    for item in loot:

        add_item(game.inventory, item)

        process_game_event(
            game, 
            GameEvent(event_type="collect", target=item["id"], amount=item.get("quantity", 1))
        )