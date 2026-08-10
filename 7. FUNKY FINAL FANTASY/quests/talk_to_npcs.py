from quests.quests import start_quest
from npcs.utils_npcs import get_npc_state


def talk_to_npc(game, npc):
    
    if npc.id not in game.met_npcs:
        game.met_npcs.append(npc.id)

    if npc.id in game.npcs_with_new_dialogue:
        game.npcs_with_new_dialogue.remove(npc.id)

    state = get_npc_state(game, npc)

    print(state["description"])
    print(state["dialogues"])

    for id in npc.quests:
        if id not in [
            quest.id for quest in game.active_quests + game.completed_quests
        ]:
            start_quest(game, id)



