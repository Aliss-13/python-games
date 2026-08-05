class Enemy:

    def __init__(
        self,
        id,
        name,
        rarity,
        tier,
        base_stats,
        skills,
        rotation=None,
        level=1,
        bonus=None,
        effects=None,
        xp=0,
        is_boss=False,
        is_sub_boss=False
    ):

        self.id = id
        self.name = name
        self.rarity = rarity
        self.tier = tier
        self.life = base_stats.get("life_max",0)
        self.mana = base_stats.get("mana_max",0)
        self.base_stats = base_stats
        self.level = level
        self.skills = skills or []
        self.rotation = rotation or self.skills
        self.sr_index = 0
        self.bonus = bonus or {}
        self.effects = effects or []
        self.xp = xp
        self.is_boss = is_boss
        self.is_sub_boss = is_sub_boss
        self.defeated = False


    def to_dict(self):

        return {
            "id": self.id,
            "defeated": self.defeated
        }

    def __repr__(self):
        return f"{self.name} - {self.rarity}"





  