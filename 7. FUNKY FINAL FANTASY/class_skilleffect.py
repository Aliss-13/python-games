class SkillEffect:

    def __init__(
        self,
        effect_id,
        chance,
        target="skill_target"
    ):
        self.effect_id = effect_id
        self.chance = chance
        self.target = target