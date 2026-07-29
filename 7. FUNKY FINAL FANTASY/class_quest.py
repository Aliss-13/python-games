from level import level_up, xp_required
from inventory import add_item
from display import display_loot
from item_generator import generate_item


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
        self.amount = amount

        self.progress = 0
        self.completed = False

        self.reward_xp = reward_xp
        self.reward_items = reward_items or []


    def to_dict(self):

        return {
            "id": self.id,
            "progress": self.progress,
            "completed": self.completed
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
        quest.completed = data.get("completed", False)

        return quest


FOREST_QUESTS = {

    "spider_hunt": Quest(
        id="spider_hunt",
        name="Des nids un peu trop collants",
        description=
        "Des araignées prolifèrent et menacent les autres animaux de la forêt.",
        objective_type="kill",
        targets=["black_spider", "black_widow", "recluse"],
        amount=5,
        reward_xp=100
    ),

    "test_spider": Quest(
        id="test_spider",
        name="Test araignées",
        description="Tuer des araignées",
        objective_type="kill",
        targets=["black_spider", "black_widow", "recluse"],
        amount=3,
        reward_xp=10
    ),


    "raven_hunt": Quest(
        id="raven_hunt",
        name="Une menace dans les arbres",
        description=
        "Des corbeaux malades attaquent les voyageurs.",
        objective_type="kill",
        targets=["sick_raven", "sick_great_raven", "putrid_great_raven"],
        amount=5,
        reward_xp=100
    ),


    "discover_hut": Quest(
        id="discover_hut",
        name="La cabane oubliée",
        description=
        "Trouvez la vieille cabane abandonnée.",
        objective_type="discovery",
        targets=["hut_found"],
        amount=1,
        reward_xp=50
    ),


    "discover_strange_tree": Quest(
        id="discover_strange_tree",
        name="L'arbre mystérieux",
        description=
        "Trouvez l'arbre mystérieux.",
        objective_type="discovery",
        targets=["strange_tree_found"],
        amount=1,
        reward_xp=50
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

    game.completed_quests.append(quest)
    game.active_quests.remove(quest)

    gain_xp_quest(game, quest)

    
    for item_id in quest.reward_items:
        item = generate_item(item_id)

    if item:
        add_item(game.inventory, item)


def process_game_event(game, event):

    for quest in game.active_quests:

        if quest.completed:
            continue

        if quest.objective_type != event.event_type:
            continue

        if event.target not in quest.targets:
            continue

        quest.progress += event.amount

        print(
            f"📜 {quest.name} : "
            f"{quest.progress}/{quest.amount}"
        )

        if quest.progress >= quest.amount:
            complete_quest(game, quest)