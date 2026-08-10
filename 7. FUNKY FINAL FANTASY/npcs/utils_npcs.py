from npcs.data_npcs import FOREST_NPCS


def get_available_npcs(game, zone):

    available = []

    for npc in FOREST_NPCS.values():

        if npc.zone != zone.id:
            continue

        if npc.id in game.met_npcs and npc.id not in game.npcs_with_new_dialogue:
            continue

        available.append(npc)

    return available


def unlock_npc_dialogue(game, npc_id):
    if npc_id not in game.npcs_with_new_dialogue:
        game.npcs_with_new_dialogue.append(npc_id)


def get_npc_state(game, npc):

    for condition, data in npc.dialogue_states.items():

        if check_condition(game, condition):
            return {
                "name": data.get("name", npc.name),
                "description": data.get("description", npc.description),
                "dialogues": data["dialogues"]
            }
    
    return {
        "name": npc.name,
        "description": npc.description,
        "dialogues": npc.dialogues
    }
    
def check_condition(game, condition):

    if condition in game.defeated_unique_enemies:
        return True

    if condition in [
        quest.id for quest in game.completed_quests
    ]:
        return True

    return False


