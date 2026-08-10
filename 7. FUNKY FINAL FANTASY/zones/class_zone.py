from display import display_boss_name

class Zone:

    def __init__(
        self,
        id,
        name,
        description,
        events,
        loot_profile,
        enemies=None,
        rare_enemies=None,
        rare_chance=0.05,
        sub_boss=None,
        boss=None,
        flags=None,
        progress=0,
        recommended_level=1,
        sub_boss_progress=10,
        boss_progress=20,
        total_progress=30
    ):

        self.id = id
        self.name = name
        self.description = description

        # événements
        self.events = events

        # loot et scaling objets
        self.loot_profile = loot_profile
        self.min_item_level = loot_profile["item_level"][0]
        self.max_item_level = loot_profile["item_level"][1]

        # ennemis
        self.enemies = enemies or []
        self.enemy_kills = {}
        self.rare_enemies = rare_enemies or []
        self.rare_chance = rare_chance

        # boss
        self.sub_boss = sub_boss
        self.boss = boss

        self.sub_boss_progress = sub_boss_progress
        self.boss_progress = boss_progress
        self.total_progress = total_progress

        self.sub_boss_unlocked = False
        self.boss_unlocked = False

        self.sub_boss_defeated = False
        self.boss_defeated = False

        # progression zone
        self.flags = flags or []
        self.progress = progress
        
        # découverte
        self.discovered = False

        # niveau conseillé
        self.recommended_level = recommended_level

        # état final
        self.completed = False


    def to_dict(self):

        return {
            "id": self.id,
            "progress": self.progress,
            "flags": self.flags,
            "discovered": self.discovered,
            "sub_boss_unlocked": self.sub_boss_unlocked,
            "boss_unlocked": self.boss_unlocked,
            "sub_boss_defeated": self.sub_boss_defeated,
            "boss_defeated": self.boss_defeated,
            "enemy_kills": self.enemy_kills,   
        }

    def load_state(self, data):

        self.progress = data.get("progress", 0)
        self.flags = data.get("flags", [])
        self.discovered = data.get("discovered", False)
        self.sub_boss_unlocked = data.get("sub_boss_unlocked", False)
        self.boss_unlocked = data.get("boss_unlocked", False)
        self.sub_boss_defeated = data.get("sub_boss_defeated", False)
        self.boss_defeated = data.get("boss_defeated", False)
        self.enemy_kills = data.get("enemy_kills", {})


    @property
    def difficulty(self):

        if self.progress < self.sub_boss_progress:
            return 1

        elif self.progress < self.boss_progress:
            return 2

        else:
            return 3


    def add_progress(self, amount):

        if amount <= 0:
            return

        self.progress += amount

        print(f"Vous gagnez +{amount} progression de zone !")

        self.check_unlocks()


    def check_unlocks(self):

        if (
            self.progress >= self.sub_boss_progress
            and not self.sub_boss_unlocked
        ):
            self.sub_boss_unlocked = True
            sub_boss = display_boss_name(self.sub_boss)
            print(f"⚔️ {sub_boss} est accessible !")


        if (
            self.progress >= self.boss_progress
            and self.sub_boss_defeated
            and not self.boss_unlocked
        ):
            self.boss_unlocked = True
            boss = display_boss_name(self.boss)
            print(f"👑 {boss} est accessible !")