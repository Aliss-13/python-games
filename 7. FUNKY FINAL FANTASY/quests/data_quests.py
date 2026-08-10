from quests.class_quest import Quest

QUESTS_BY_TARGET = {
    "werewolf": "kill_the_werewolf",
    "baby_samuel": "free_baby_samuel",
    }

FOREST_QUESTS = {

    "help_build_the_community_hall": Quest(
        id="help_build_the_community_hall",
        name="Aidez à construire la salle du village",
        description=
        "Récoltez du bois pour aider le charpentier du village.",
        quest_type="collect_items",
        objectives= {"log": 10},
        reward_xp=50, 
        zone_progress=2
    ),

    "the_apple_pie": Quest(
        id="the_apple_pie",
        name="La tarte aux pommes",
        description=
        "Récoltez des pommes pour que Dame Lisse prépare sa fameuse tarte.",
        quest_type="collect_items",
        objectives= {"red_apple": 10},
        reward_xp=50, 
        zone_progress=3
    ),

    "spider_hunt": Quest(
        id="spider_hunt",
        name="Des nids un peu trop collants",
        description=
        "Tuer trois araignées géantes.",
        quest_type="kill_group",
        objectives= {
                        "targets": ["black_spider", "black_widow", "recluse"],
                        "required": 3
        },
        reward_xp=80, 
        zone_progress=5
    ),


    "raven_hunt": Quest(
        id="raven_hunt",
        name="Des corbeaux malades agressifs.",
        description=
        "Tuer trois corbeaux malades.",
        quest_type="kill_group",
        objectives={
                    "targets": ["sick_raven", "sick_great_raven", "putrid_great_raven"],
                    "required": 3
        },
        reward_xp=80,
        zone_progress=5
    ),


    "rare_enemies": Quest(
        id="rare_enemies",
        name="Monstres rares",
        description=
        "Tuer les quatre monstres rares : Bébé Samuel, Loup-garou, Recluse et Grand Corbeau Putride.",
        quest_type="kill_each",
        objectives={"baby_samuel": 1, "werewolf": 1, "putrid_great_raven": 1, "recluse": 1},
        reward_xp=150,
        zone_progress=15,
        reward_items=["nothingness"]
    ),


    "free_baby_samuel": Quest(
        id="free_baby_samuel",
        name="Libérer Bébé Samuel",
        description=
        "Samuel est possédé... Sauvez son âme de l'Enfer !",
        quest_type="kill_each",
        objectives={"baby_samuel": 1},
        reward_xp=80,
        zone_progress=5,
        reward_items=["cosmic_mittens"]
    ),


    "kill_the_werewolf": Quest(
        id="kill_the_werewolf",
        name="Eliminer le loup-garou",
        description=
        "Un loup-garou tue les villageois à chaque pleine lune...",
        quest_type="kill_each",
        objectives={"werewolf": 1},
        reward_xp=80,
        zone_progress=5,
        reward_items=["star_patterned_hose"]
    ),


    "forest_mysteries": Quest(
        id="forest_mysteries",
        name="Les mystères de la forêt",
        description=
        "Découvrir quatre lieux mystérieux de la forêt.",
        quest_type= "discover_each",
        objectives={"hut_found": 1, "strange_tree_found": 1, "stone_circle_found": 1, "dark_clearing_found": 1},
        reward_xp=50,
        zone_progress=15
    ),

    "the_seamstress": Quest(
        id="the_seamstress",
        name="La couturière",
        description=
        "Récupérer 5 champignons sombres, 3 soies d'araignée et 5 plumes noires pour aider l'apprentie couturière.",
        quest_type= "collect_items",
        objectives={"dark_mushroom": 5, "spider_silk": 3, "black_feather": 5},
        reward_xp=100,
        zone_progress=15,
        reward_items=["raven_dress"]
    )

}