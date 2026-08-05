from skills.skills import apply_skill_effects, apply_skill_healing, pay_skill_cost, apply_skill_damage_to_targets, display_skill_message

def execute_skill(context):

    if not pay_skill_cost(context):
        return

    display_skill_message(context)

    actions = {
        "damage": apply_skill_damage_to_targets,
        "heal": apply_skill_healing,
        "apply_effect": apply_skill_effects
    }

    for action in context.skill.actions:
        handler = actions.get(action)

        if handler:
            handler(context)