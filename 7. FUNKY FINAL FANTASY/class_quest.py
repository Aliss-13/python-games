from level import level_up, xp_required
from loot_tables import add_loot
from display import display_loot
from item_generator import generate_item
from class_enemy import ENEMIES, get_enemy_by_id




class Quest:

    def __init__(
        self,
        id,
        name,
        description,
        objective_type,
        targets=None,
        amount=0,
        reward_xp=0,
        reward_items=None
    ):

        self.id = id
        self.name = name
        self.description = description

        self.objective_type = objective_type
        self.targets = targets or []
        self.target_progress = {target: 0 for target in self.targets}
        self.amount = amount

        self.progress = 0
        self.completed = False

        self.reward_xp = reward_xp
        self.reward_items = reward_items or []


    def to_dict(self):

        return {
            "id": self.id,
            "progress": self.progress,
            "target_progress": self.target_progress,
            "completed": self.completed,
            "reward_items": self.reward_items
        }


    @classmethod
    def from_dict(cls, data, quest_database):

        quest_template = quest_database[data["id"]]

        quest = cls(
            id=quest_template.id,
            name=quest_template.name,
            description=quest_template.description,
            objective_type=quest_template.objective_type,
            targets=quest_template.targets,
            amount=quest_template.amount,
            reward_xp=quest_template.reward_xp,
            reward_items=quest_template.reward_items
        )

        quest.progress = data.get("progress", 0)

        quest.target_progress = data.get(
            "target_progress", 
            {target: 0 for target in quest.targets})
        
        quest.completed = data.get("completed", False)

        return quest


QUESTS_BY_TARGET = {
    "werewolf": "kill_the_werewolf",
    "baby_samuel": "free_baby_samuel",
    }

FOREST_QUESTS = {

    "spider_hunt": Quest(
        id="spider_hunt",
        name="Des nids un peu trop collants",
        description=
        "Des araignées prolifèrent et menacent les autres animaux de la forêt.",
        objective_type="kill",
        targets=["black_spider", "black_widow", "recluse"],
        amount=5,
        reward_xp=80
    ),


    "raven_hunt": Quest(
        id="raven_hunt",
        name="Une menace dans les arbres",
        description=
        "Des corbeaux malades attaquent les voyageurs.",
        objective_type="kill",
        targets=["sick_raven", "sick_great_raven", "putrid_great_raven"],
        amount=5,
        reward_xp=80
    ),


    "rare_enemies": Quest(
        id="rare_enemies",
        name="Monstres rares",
        description=
        "Des monstres puissants rôdent...",
        objective_type="kill_each",
        targets=["putrid_great_raven", "recluse", "werewolf", "baby_samuel"],
        amount=1,
        reward_xp=150,
        reward_items=["nothingness"]
    ),


    "free_baby_samuel": Quest(
        id="free_baby_samuel",
        name="Libérer Bébé Samuel",
        description=
        "Samuel est possédé... Sauvez son âme de l'Enfer !",
        objective_type="kill",
        targets=["baby_samuel"],
        amount=1,
        reward_xp=50,
        reward_items=["phoenix_feather", "cosmic_mittens"]
    ),


    "kill_the_werewolf": Quest(
        id="kill_the_werewolf",
        name="Eliminer le loup-garou",
        description=
        "Un loup-garou tue les villageois à chaque pleine lune...",
        objective_type="kill",
        targets=["werewolf"],
        amount=1,
        reward_xp=50,
        reward_items=["phoenix_feather", "star_patterned_hose"]
    ),


    "discover_hut": Quest(
        id="discover_hut",
        name="La cabane oubliée",
        description=
        "Trouvez la vieille cabane abandonnée.",
        objective_type="discovery",
        targets=["hut_found"],
        amount=1,
        reward_xp=20
    ),


    "discover_strange_tree": Quest(
        id="discover_strange_tree",
        name="L'arbre mystérieux",
        description=
        "Trouvez l'arbre mystérieux.",
        objective_type="discovery",
        targets=["strange_tree_found"],
        amount=1,
        reward_xp=20
    )

}


def create_quest(quest_id):

    original = FOREST_QUESTS[quest_id]

    return Quest(
        id=original.id,
        name=original.name,
        description=original.description,
        objective_type=original.objective_type,
        targets=original.targets,
        amount=original.amount,
        reward_xp=original.reward_xp,
        reward_items=original.reward_items
    )


def start_quest(game, quest_id):

    for quest in game.active_quests:

        if quest.id == quest_id:
            return

    quest = create_quest(quest_id)

    game.active_quests.append(quest)

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
    game.active_quests.remove(quest)

    gain_xp_quest(game, quest)
    print("")

    rewards = []

    for item_id in quest.reward_items:

        item = generate_item(item_id, 1)

        if item:
            rewards.append(item)

    add_loot(game.inventory, rewards)

    if rewards:
        display_loot(rewards)

    
def process_game_event(game, event):
    
    if event.target in QUESTS_BY_TARGET:
        start_quest(game, QUESTS_BY_TARGET[event.target])

    for quest in game.active_quests:

        if quest.completed:
            continue

        # kill_each réagit aussi aux événements kill
        if quest.objective_type == "kill_each":

            if event.event_type != "kill":
                continue

            if event.target not in quest.targets:
                continue

            quest.target_progress[event.target] += event.amount

            enemy = get_enemy_by_id(event.target, ENEMIES)
            enemy_name = enemy.name if enemy else event.target
            print(
                f"╰┈> Quête avancée : {quest.name} "
                f"({enemy_name})"
            )
            

            if all(
                value >= quest.amount
                for value in quest.target_progress.values()
            ):
                complete_quest(game, quest)

            continue


        # quêtes normales
        if quest.objective_type != event.event_type:
            continue

        if event.target not in quest.targets:
            continue

        quest.progress += event.amount

        if quest.progress >= quest.amount:
            complete_quest(game, quest)
        else:
            print(
                f"📜 Quête avancée : {quest.name} "
                f"{quest.progress}/{quest.amount}"
            )