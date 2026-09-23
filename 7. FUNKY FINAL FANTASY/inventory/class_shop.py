class Shop:
    def __init__(self, id, name, inventory, level=1):
        self.id = id
        self.name = name
        self.inventory = inventory
        self.level=level



FOREST_SHOPS = {
    "forest_shop": Shop(
        id="forest_shop",
        name="Boutique de la forêt",
        inventory=[
            "life_potion",
            "mana_potion",
            "iron_helmet",
            "ring_of_domination",
            "embroidered_robe",
            "iron_sword",
            "shiny_staff"

        ],
        level=3
    )
}

def shop_locked():
    print("La boutique est encore verrouillée.")