DIALOGUE_UNLOCKS = {

    "free_baby_samuel": ["catharine_baby_samuels_mother"],

    "the_seamstress": ["lia_young_seamstress"],

    "help_build_the_community_hall": ["thomas_the_carpenter"],

    "the_apple_pie": ["lady_lisse", "rupaul_the_fool"],

    "forest_mysteries": ["gregoire_the_old_man", "sophy_the_midwife"],

    "kill_the_werewolf": [
        "magda_the_fortune_teller",
        "melin_the_alpha_drood",
        "mayor_paulson"
    ],

    "the_vvitch": [
        "cockhitch_keeper",
        "ronald_farmer",
        "the_purple_cat",
        "matthew_the_priest"
    ],
        
    "black_phillip": ["the_twins", "frocque"]
}


def unlock_dialogues_for_quest(game, quest_id):

    for npc_id in DIALOGUE_UNLOCKS.get(quest_id, []):
        
        if npc_id not in game.npcs_with_new_dialogue:
            game.npcs_with_new_dialogue.append(npc_id)


def unlock_dialogues_for_defeated_unique_enemies(game, enemy_id):

    for npc_id in DIALOGUE_UNLOCKS.get(enemy_id, []):
        
        if npc_id not in game.npcs_with_new_dialogue:
            game.npcs_with_new_dialogue.append(npc_id)