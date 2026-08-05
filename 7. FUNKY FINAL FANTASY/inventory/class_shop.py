class Shop:
    def __init__(self, id, name, inventory):
        self.id = id
        self.name = name
        self.inventory = inventory



FOREST_SHOPS = {
    "village_shop": Shop(
        id="village_shop",
        name="Boutique du village",
        inventory=[
            "life_potion",
            "mana_potion",
            "iron_helmet",
            "ring_of_domination",
            "embroidered_robe",
            "iron_sword",
            "shiny_staff"

        ]
    )
}