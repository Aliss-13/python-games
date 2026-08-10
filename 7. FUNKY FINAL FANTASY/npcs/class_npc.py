class NPC:

    def __init__(
        self,
        id,
        name,
        description,
        dialogues=None,
        quests=None, 
        zone=None,
        dialogue_states=None
    ):
        self.id = id
        self.name = name
        self.description = description

        self.dialogues = dialogues or []
        self.quests = quests or []
        self.zone = zone
        self.dialogue_states = dialogue_states or {}