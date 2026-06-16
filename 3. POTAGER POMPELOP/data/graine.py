from models.graine import Graine 

graines_disponibles = {1}
    

graines = {
    1: Graine(
        1, 
        "graine_verte 🟢", 
        1, 
        2, 
        3, 
        loot = [
            {"nom" : "salade 🥬", "chance" : 0.4}, 
            {"nom" : "melon 🍈", "chance" : 0.2},
            {"nom" : "concombre 🥒", "chance" : 0.4}
        ]
    ),

    2 : Graine(
        2,
        "graine_jaune 🟡",
        2,
        3,
        5,
        loot=[
                    {"nom": "melon 🍈", "chance": 0.4},
                    {"nom": "patate 🥔", "chance": 0.2},
                    {"nom": "maïs 🌽", "chance": 0.4}
        ]
    ),

    3 : Graine(
        3, 
        "graine_orange 🟠",
        3, 
        4, 
        7,
        loot = [   
                {"nom" : "carotte 🥕", "chance" : 0.4},
                {"nom" : "patate 🥔", "chance" : 0.4},
                {"nom" : "citrouille 🎃", "chance" : 0.2}
        ]
    ),

    4 : Graine(
        4, 
        "graine_rouge 🔴",
        4, 
        7, 
        10,
        loot  = [
                {"nom" : "tomate 🍅", "chance" : 0.4},
                {"nom" : "fraise 🍓", "chance" : 0.2},
                {"nom" : "citrouille 🎃", "chance" : 0.4}
        ]
    ),
    
    5 : Graine(
        5, 
        "graine_violette 🟣",
        5, 
        10, 
        15,
        loot = [
                {"nom" : "pastèque 🍉", "chance" : 0.3},
                {"nom" : "aubergine 🍆", "chance" : 0.3},
                {"nom" : "myrtille 🫐", "chance" : 0.3}
        ]
    )
}