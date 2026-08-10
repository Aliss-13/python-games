# dans Data, stocker uniquement des structures
# pas de fonction !

ITEMS = {

#---------------------------- Consommables ------------------------------------------------
    "phoenix_feather": {
        "name": "Plume de phénix",
        "description": "Résurrection personnage avec 50 PV",
        "type": "consumable", 
        "rarity": "rare", 
        "effects": {"resurrection": 50},
        "cost": 0
    },

    "mana_potion": {
        "name": "Potion de mana",
        "description": "+80 mana",
        "type": "consumable", 
        "rarity": "uncommon", 
        "effects": {"restore_mana": 80}, 
        "cost": 10
    },

    "life_potion": {
        "name": "Potion de vie",
        "description": "+80 PV",
        "type": "consumable", 
        "rarity": "uncommon", 
        "effects": {"heal": 80},
        "cost": 10
    },


    "greater_healing_potion": {
        "name": "Grande potion de soin",
        "description": "Soigne tous les alliés de 100 PV",
        "type": "consumable",
        "rarity": "rare",
        "effects": {"heal_all": 100},
        "cost": 50
    },


    "iron_skin_potion": {
        "name": "Potion de peau de fer",
        "description": "+20 défense pendant 3 tours",
        "type": "consumable",
        "rarity": "rare",
        "effects": {"iron_skin": 1},
        "cost": 75
    },

#---------------------------- Base craft ------------------------------------------------
    "red_apple": {
        "name": "Pomme rouge",
        "description": "Une pomme rouge, on dirait de la Red Delicious... Est ce qu'elle est bio ?",
        "type": "base_craft",
        "rarity": "common",
        "cost": 0.5,
    },

    "dark_mushroom": {
        "name": "Champignon sombre",
        "description": "Un champignon noir aux propriétés étranges.",
        "type": "base_craft",
        "rarity": "common",
        "cost": 0.5,
    },

    "spider_silk": {
        "name": "Soie d'araignée",
        "description": "Brille légèrement.",
        "type": "base_craft",
        "rarity": "uncommon",
        "cost": 2,
    },

    "log": {
        "name": "Bûche",
        "description": "Une bûche. Pratique pour construire des trucs.",
        "type": "base_craft",
        "rarity": "common",
        "cost": 0.5,
    },

    "black_feather": {
        "name": "Plume noire",
        "description": "Une plume noire avec des tons bleutés.",
        "type": "base_craft",
        "rarity": "common",
        "cost": 0.5,
    },
#---------------------------- Tête ------------------------------------------------

    "iron_helmet" : {
        "name": "Casque de fer",
        "description": "Parce qu'avec les casques, on a des têtes de gland.",
        "type": "equipment", 
        "character_class": ["hand_to_hand"], 
        "slot": "head", 
        "rarity": "common", 
        "bonus": {"defense": 5},
        "scaling": {"defense": 0.5},
        "cost": 20
    },

    "black_hood" : {
        "name": "Capuche noire",
        "description": "Protège de la chaleur et des insectes.",
        "type": "equipment", 
        "character_class": ["magic", "hand_to_hand"], 
        "slot": "head", 
        "rarity": "common", 
        "bonus": {"power": 5, "speed": 5},
        "scaling": {"power": 0.5, "speed": 0.5},
        "cost": 20
    },

    "shiny_helmet" : {
        "name": "Casque rutilant",
        "description": "Quand on tape dessus, on obtient un mi majeur.",
        "type": "equipment", 
        "character_class": ["hand_to_hand"], 
        "slot": "head", 
        "rarity": "uncommon", 
        "bonus": {"life_max": 8, "defense": 5},
        "scaling": {"life_max": 0.75, "defense": 0.75},
        "cost": 30
    },

    "mysterious_headband" : {
        "name": "Bandeau mystérieux",
        "description": "Vous donne un air mystérieux.",
        "type": "equipment", 
        "character_class": ["magic"], 
        "slot": "head", 
        "rarity": "uncommon", 
        "bonus": {"mana_max": 8, "power": 5},
        "scaling": {"mana_max": 0.75, "power": 0.75},
        "cost": 30
    },


    "great_golden_helm" : {
        "name": "Grand heaume d'or",
        "description": "Vous gagnez 20 cm ! Non, pas là, non...",
        "type": "equipment", 
        "character_class": ["hand_to_hand"], 
        "slot": "head", 
        "rarity": "rare", 
        "bonus": {"life_max": 12, "power": 10, "defense": 8},
        "scaling": {"life_max": 1, "power": 1, "defense": 1},
        "cost": 30
    },

    "new_moon_tiara" : {
        "name": "Tiare de la nouvelle lune",
        "description": "Vous vous sentez comme une princesse.",
        "type": "equipment", 
        "character_class": ["magic"], 
        "slot": "head", 
        "rarity": "rare", 
        "bonus": {"mana_max": 15, "power": 10, "speed": 8},
        "scaling": {"mana_max": 1, "power": 1, "speed": 1},
        "cost": 30
    },

    "beyond_the_veil" : {
        "name": "Au-delà du voile",
        "description": "Une mélopée inquiétante s'en échappe...",
        "type": "equipment", 
        "character_class": ["magic"], 
        "slot": "head", 
        "rarity": "epic", 
        "bonus": {"mana_max": 20, "power": 12, "speed": 10},
        "scaling": {"mana_max": 1.5, "power": 1.5, "speed": 1.5},
        "cost": 30
    },

#---------------------------- Mains ------------------------------------------------

    "power_gloves" : {
        "name": "Gants de puissance",
        "description": "Vous sentez la puissance entre vos mains !",
        "type": "equipment", 
        "character_class": ["magic", "hand_to_hand"], 
        "slot": "hands", 
        "rarity": "common", 
        "bonus": {"power": 10},
        "scaling": {"power": 0.5},
        "cost": 20
    },

    "ring_of_domination" : {
        "name": "Anneau de domination",
        "description": "La pierre de cet anneau émet une curieuse lumière...",
        "type": "equipment", 
        "character_class": ["magic", "hand_to_hand"], 
        "slot": "hands", 
        "rarity": "common", 
        "bonus": {"power": 5, "speed": 5},
        "scaling": {"power": 0.5, "speed": 0.5},
        "cost": 20
    },

    "shiny_gloves" : {
        "name": "Gants rutilants",
        "description": "Protège bien vos doigts.",
        "type": "equipment", 
        "character_class": ["hand_to_hand"], 
        "slot": "hands", 
        "rarity": "uncommon", 
        "bonus": {"life_max": 8, "defense": 5},
        "scaling": {"life_max": 0.75, "defense": 0.75},
        "cost": 30
    },

    "immaculate_gloves" : {
        "name": "Gants immaculés",
        "description": "Vous imprègne d'une force tranquille.",
        "type": "equipment", 
        "character_class": ["magic"], 
        "slot": "hands", 
        "rarity": "uncommon", 
        "bonus": {"mana_max": 8, "power": 5},
        "scaling": {"mana_max": 0.75, "power": 0.75},
        "cost": 30
    },

    "cosmic_mittens" : {
        "name": "Gants cosmiques",
        "description": "Vous contrôlez la galaxie !",
        "type": "equipment", 
        "character_class": ["magic"], 
        "slot": "hands", 
        "rarity": "rare", 
        "bonus": {"mana_max": 10, "power": 5, "speed": 5},
        "scaling": {"mana_max": 0.75, "power": 0.75, "speed": 0.75},
        "cost": 50
    },

    "obsidian_ring" : {
        "name": "Anneau d'obsidienne",
        "description": "La noirceur vous va si bien...",
        "type": "equipment", 
        "character_class": ["hand_to_hand", "magic"], 
        "slot": "hands", 
        "rarity": "rare", 
        "bonus": {"life_max": 10, "power": 5, "defense": 5},
        "scaling": {"life_max": 1, "power": 1, "defense": 1},
        "cost": 50
    },

    "black_phillips_signed_ring" : {
        "name": "Chevalière de Black Phillip",
        "description": "Vous aimez vivre délicieusement.",
        "type": "equipment", 
        "character_class": ["hand_to_hand", "magic"], 
        "slot": "hands", 
        "rarity": "epic", 
        "bonus": {"power": 15, "speed": 15, "defense": 5},
        "scaling": {"power": 1.5, "speed": 1.5, "defense": 1.5},
        "cost": 70
    },

#---------------------------- Jambes ------------------------------------------------

    "chainmail_trousers" : {
        "name": "Pantalon cotte-de-maille",
        "description": "Très prisé dans certaines soirées.",
        "type": "equipment", 
        "character_class": ["hand_to_hand"], 
        "slot": "legs", 
        "rarity": "common", 
        "bonus": {"defense": 8},
        "scaling": {"defense": 0.5},
        "cost": 20
    },

    "black_trousers" : {
        "name": "Pantalon noir",
        "description": "Un classique indémodable.",
        "type": "equipment", 
        "character_class": ["magic", "hand_to_hand"], 
        "slot": "legs", 
        "rarity": "common", 
        "bonus": {"power": 7, "speed": 7},
        "scaling": {"power": 0.5, "speed": 0.5},
        "cost": 20
    },

    "iron_thigh_guard" : {
        "name": "Cuissard en fer",
        "description": "Quand on tape dessus, on obtient un sol bémol majeur.",
        "type": "equipment", 
        "character_class": ["hand_to_hand"], 
        "slot": "legs", 
        "rarity": "uncommon", 
        "bonus": {"life_max": 10, "defense": 8},
        "scaling": {"life_max": 0.75, "defense": 0.75},
        "cost": 30
    },

    "star_patterned_hose" : {
        "name": "Chausses étoilées",
        "description": "Pour des cuisses qui mettent des étoiles plein les yeux !",
        "type": "equipment", 
        "character_class": ["magic"], 
        "slot": "legs", 
        "rarity": "uncommon", 
        "bonus": {"mana_max": 15, "power": 8},
        "scaling": {"mana_max": 0.75, "power": 0.75},
        "cost": 30
    },


    "levis_501" : {
        "name": "Levis 501",
        "description": "Est-ce nécessaire de le présenter ?",
        "type": "equipment", 
        "character_class": ["magic", "hand_to_hand"], 
        "slot": "legs", 
        "rarity": "rare", 
        "bonus": {"power": 10, "speed": 8, "defense": 12},
        "scaling": {"power": 1, "speed": 1, "defense": 1},
        "cost": 50
    },

#---------------------------- Pieds ------------------------------------------------

    "winged_boots" : {
        "name": "Bottes ailées",
        "description": "Les bottes-qui-courent-vite !",
        "type": "equipment", 
        "character_class": ["magic", "hand_to_hand"], 
        "slot": "feet", 
        "rarity": "common", 
        "bonus": {"speed": 3},
        "scaling": {"speed": 0.5},
        "cost": 20
    },

    "red_shoes" : {
        "name": "Souliers rouges",
        "description": "Elles sont vernies avec un joli noeud. Pas très epic fantasy tout ça...",
        "type": "equipment", 
        "character_class": ["magic", "hand_to_hand"], 
        "slot": "feet", 
        "rarity": "uncommon", 
        "bonus": {"speed" : 5},
        "scaling": {"speed": 0.75},
        "cost": 30
    },

    "seven_league_boots" : {
        "name": "Bottes de 7 lieues",
        "description": "Est-ce nécessaire de les présenter ?",
        "type": "equipment", 
        "character_class": ["magic", "hand_to_hand"], 
        "slot": "feet", 
        "rarity": "rare", 
        "bonus": {"speed" : 8},
        "scaling": {"speed" : 1},
        "cost": 50
    },

    "light_infused_shoes" : {
        "name": "Chaussures infusées de lumière",
        "description": "La vitesse de la lumière dans un accessoire de mode.",
        "type": "equipment", 
        "character_class": ["magic", "hand_to_hand"], 
        "slot": "feet", 
        "rarity": "epic", 
        "bonus": {"power": 10, "speed" : 10},
        "scaling": {"power": 1.5, "speed" : 1.5},
        "cost": 70
    },

#---------------------------- Torse ------------------------------------------------

    "embroidered_robe" : {
        "name": "Robe brodée",
        "description": "Brodée à la main avec du fil de qualité.",
        "type": "equipment", 
        "character_class": ["magic"], 
        "slot": "chest", 
        "rarity": "common", 
        "bonus": {"mana_max": 10},
        "scaling": {"mana_max": 0.5},
        "cost": 20
    },

    "wizard_robe" : {
        "name": "Robe de sorcier",
        "description": "Une robe de sorcier de seconde main. Très bon état. Merci Vinted !",
        "type": "equipment", 
        "character_class": ["magic"], 
        "slot": "chest", 
        "rarity": "uncommon", 
        "bonus": {"mana_max": 15, "power": 5},
        "scaling": {"mana_max": 0.75, "power": 0.75},
        "cost": 30
    },

    "force_field" : {
        "name": "Champ de force",
        "description": "BzZZzBzZZz...",
        "type": "equipment", 
        "character_class": ["magic"], 
        "slot": "chest", 
        "rarity": "rare", 
        "bonus": {"mana_max": 20, "power": 10, "defense": 5},
        "scaling": {"mana_max": 1, "power": 1, "defense": 1},
        "cost": 50
    },

    "raven_dress" : {
        "name": "Robe du Corbeau",
        "description": "Magnifique robe brodée de noir avec des reflets bleutés. Du bel artisanat.",
        "type": "equipment", 
        "character_class": ["magic"], 
        "slot": "chest", 
        "rarity": "rare", 
        "bonus": {"mana_max": 10, "power": 15, "speed": 5},
        "scaling": {"mana_max": 1, "power": 1, "speed": 1},
        "cost": 50
    },

    "radiance" : {
        "name": "Radiance",
        "description": "Lunettes de soleil obligatoires !",
        "type": "equipment", 
        "character_class": ["magic"], 
        "slot": "chest", 
        "rarity": "epic", 
        "bonus": {"mana_max": 25, "power": 10, "defense": 10},
        "scaling": {"mana_max": 1.5, "power": 1.5, "defense": 1.5},
        "cost": 70
    },

    "iron_breastplate" : {
        "name": "Plastron de fer",
        "description": "Un honnête plastron de fer.",
        "type": "equipment", 
        "character_class": ["hand_to_hand"], 
        "slot": "chest", 
        "rarity": "common", 
        "bonus": {"life_max" : 20},
        "scaling": {"life_max" : 0.5},
        "cost": 20
    },

    "shiny_breastplate" : {
        "name": "Plastron rutilant",
        "description": "Rutilant, ça veut dire « Qui brille beaucoup. ». J'ai appris ce mot avec un chaudron...",
        "type": "equipment", 
        "character_class": ["hand_to_hand"], 
        "slot": "chest", 
        "rarity": "uncommon", 
        "bonus": {"life_max": 10, "defense" : 5},
        "scaling": {"life_max": 0.75, "defense": 0.75},
        "cost": 30
    },

    "the_kings_breastplate" : {
        "name": "Plastron du Roi",
        "description": "Orné de symboles à la feuille d'or.",
        "type": "equipment", 
        "character_class": ["hand_to_hand"], 
        "slot": "chest", 
        "rarity": "rare", 
        "bonus": {"life_max": 15, "power": 10, "defense" : 10},
        "scaling": {"life_max": 1, "power": 1, "defense" : 1},
        "cost": 50
    },

    "dark_armor" : {
        "name": "Armure sombre",
        "description": "Une énergie maléfique s'en dégage...",
        "type": "equipment", 
        "character_class": ["hand_to_hand"], 
        "slot": "chest", 
        "rarity": "epic", 
        "bonus": {"life_max": 20, "power": 15, "defense" : 15},
        "scaling": {"life_max": 1.5, "power": 1.5, "defense" : 1.5},
        "cost": 70
    },

#---------------------------- Armes ------------------------------------------------

    "iron_sword" : {
        "name": "Epée de fer",
        "description": "Une épée ordinaire.",
        "type": "equipment", 
        "character_class": ["hand_to_hand"], 
        "slot": "weapon", 
        "rarity": "common", 
        "bonus": {"power" : 10},
        "scaling": {"power" : 0.5},
        "cost": 20
    },

    "claymore" : {
        "name": "Claymore",
        "description": "Une épée imposante.",
        "type": "equipment", 
        "character_class": ["hand_to_hand"], 
        "slot": "weapon", 
        "rarity": "uncommon", 
        "bonus": {"power" : 20},
        "scaling": {"power": 0.75},
        "cost": 30
    },

    "scimitar" : {
        "name": "Cimeterre",
        "description": "Tu l'as vue ma grosse lame ?",
        "type": "equipment", 
        "character_class": ["hand_to_hand"], 
        "slot": "weapon", 
        "rarity": "rare", 
        "bonus": {"power" : 30, "speed": 10},
        "scaling": {"power" : 1, "speed": 1},
        "cost": 50
    },

    "memento_mori" : {
        "name": "Memento Mori",
        "description": "Rappelle-toi que tu vas mourir...",
        "type": "equipment", 
        "character_class": ["hand_to_hand"], 
        "slot": "weapon", 
        "rarity": "epic", 
        "bonus": {"life_max": 10, "power" : 35, "speed": 12},
        "scaling": {"life_max": 1.5, "power" : 1.5, "speed": 1.5},
        "cost": 70
    },
    
    "shiny_staff" : {
        "name": "Bâton brillant",
        "description": "Très tendance aux concerts de Coldplay.",
        "type": "equipment", 
        "character_class": ["magic"], 
        "slot": "weapon", 
        "rarity": "common", 
        "bonus": {"power" : 10},
        "scaling": {"power" : 0.5},
        "cost": 20
    },

    "lunar_scepter" : {
        "name": "Sceptre lunaire",
        "description": "Il y a une lune argentée au bout.",
        "type": "equipment", 
        "character_class": ["magic"], 
        "slot": "weapon", 
        "rarity": "uncommon", 
        "bonus": {"power" : 15, "speed": 5},
        "scaling": {"power": 0.75, "speed": 0.75},
        "cost": 30
    },

    "solar_orb" : {
        "name": "Orbe solaire",
        "description": "Il émet des rayons flamboyants.",
        "type": "equipment", 
        "character_class": ["magic"], 
        "slot": "weapon", 
        "rarity": "rare", 
        "bonus": {"power" : 20, "speed": 10},
        "scaling": {"power" : 1, "speed": 1},
        "cost": 50
    },

    "nothingness" : {
        "name": "Néant",
        "description": "Un puissant vide de désespoir...",
        "type": "equipment", 
        "character_class": ["magic"], 
        "slot": "weapon", 
        "rarity": "epic", 
        "bonus": {"mana_max": 15, "power" : 25, "speed": 15},
        "scaling": {"mana_max": 1.5, "power" : 1.5, "speed": 1.5},
        "cost": 70
    }
}