ITEMS = {

    #===================== POTIONS ============================

    "healing_potion": {
        "name": "Potion de vie", 
        "type": "potion",
        "tags": [],
        "ingredients": {"herbe_lunaire": 2, "champignon_sombre": 1},
        "level_required": 1,
        "source" : "level",
        "demand": 0.9,
        "price": 10, 
        "xp": 5,
        "upgrade_cost": 50
    },


    "mana_potion": {
        "name": "Potion de mana", 
        "type": "potion",
        "tags": [],
        "ingredients": {"herbe_lunaire": 1, "champignon_sombre": 2},
        "level_required": 1,
        "source" : "level",
        "demand": 0.9,
        "price": 12, 
        "xp": 6,
        "upgrade_cost": 50
    },


    "love_potion": {
        "name": "Philtre d'amour", 
        "type": "potion",
        "tags": [],
        "ingredients": {"herbe_lunaire": 2, "champignon_sombre": 1, "poussiere_etoile": 1},
        "level_required": 2,
        "source" : "level",
        "demand": 0.8,
        "price": 25, 
        "xp": 15,
        "upgrade_cost": 60
    },


    "empowerment": {
        "name": "Empouvoirment", 
        "type": "potion",
        "tags": ["corporate"],
        "ingredients": {"ecorce_ancienne": 4, "eau_enchantee": 2, "croc_feroce": 2},
        "level_required": 3,
        "source" : "level",
        "demand": 0.9,
        "price": 30, 
        "xp": 20,
        "upgrade_cost": 70
    },


    "polyjuice": {
        "name": "Polynectar", 
        "type": "potion",
        "tags": [],
        "ingredients": {"herbe_lunaire": 2, "champignon_sombre": 1, "ecorce_ancienne": 2, "eau_enchantee": 2, "croc_feroce": 1},
        "level_required": 4,
        "source" : "level",
        "demand": 0.6,
        "price": 40, 
        "xp": 25,
        "upgrade_cost": 80
    },


    "bbl": {
        "name": "Brazilian Butt Lift", 
        "type": "potion",
        "tags": ["dat_ass"],
        "ingredients": {"champignon_sombre": 1, "ecorce_ancienne": 2, "eau_enchantee": 2, "croc_feroce": 1, "pierre_noire": 2},
        "level_required": 6,
        "source" : "level",
        "demand": 0.8,
        "price": 60, 
        "xp": 40,
        "upgrade_cost": 100
    },


    "banana_boat": {
        "name": "Bananier day-o", 
        "type": "potion",
        "tags": [],
        "ingredients": {"champignon_sombre": 5, "ecorce_ancienne": 5, "eau_enchantee": 5, "croc_feroce": 3, "pierre_noire": 2},
        "level_required": 10,
        "source" : "level",
        "demand": 0.8,
        "price": 100, 
        "xp": 80,
        "upgrade_cost": 140
    },


    #===================== SORTS ============================
    
    "ass_worms": {
        "name": "Gratte-cul", 
        "type": "magic_scroll",
        "tags": ["dat_ass"],
        "ingredients": {"herbe_lunaire": 3, "champignon_sombre": 2},
        "level_required": 1,
        "source" : "level",
        "demand": 0.8,
        "price": 15, 
        "xp": 10,
        "upgrade_cost": 50
    }, 


    "pebble_in_shoe": {
        "name": "Petit caillou dans chaussure", 
        "type": "magic_scroll",
        "tags": [],
        "ingredients": {"herbe_lunaire": 2, "champignon_sombre": 3, "ecorce_ancienne": 2},
        "level_required": 2,
        "source" : "level",
        "demand": 0.9,
        "price": 20, 
        "xp": 15,
        "upgrade_cost": 60
    }, 


    "hr_optimization": {
        "name": "Optimisation des ressources humaines", 
        "type": "magic_scroll",
        "tags": ["corporate"],
        "ingredients": {"herbe_lunaire": 4, "champignon_sombre": 1, "ecorce_ancienne": 2, "eau_enchantee": 1},
        "level_required": 2,
        "source" : "level",
        "demand": 0.7,
        "price": 22, 
        "xp": 17,
        "upgrade_cost": 60
    }, 


    "knock_pinky": {
        "name": "Pan le petit orteil", 
        "type": "magic_scroll",
        "tags": [],
        "ingredients": {"herbe_lunaire": 4, "champignon_sombre": 3, "ecorce_ancienne": 2, "eau_enchantee": 2},
        "level_required": 3,
        "source" : "level",
        "demand": 0.7,
        "price": 25, 
        "xp": 20,
        "upgrade_cost": 70
    }, 


    "flatulences" : {
        "name": "Flatulences", 
        "type": "magic_scroll", 
        "tags": ["dat_ass"],
        "ingredients": {"herbe_lunaire": 2, "champignon_sombre": 1, "ecorce_ancienne": 1, "eau_enchantee": 4, "aile_de_fee": 1},
        "level_required": 4,
        "source" : "level",
        "demand": 0.5,
        "price": 45, 
        "xp": 30,
        "upgrade_cost": 80
    },


    "tax_audit" : {
        "name": "Contrôle fiscal", 
        "type": "magic_scroll",
        "tags": ["irs"],
        "ingredients": {"ecorce_ancienne": 1, "eau_enchantee": 4, "aile_de_fee": 1, "bezoard": 2, "ecaille_dragon": 2},
        "level_required": 7,
        "source" : "level",
        "demand": 0.8,
        "price": 80, 
        "xp": 60,
        "upgrade_cost": 120
    },


    "no_handy_no_candy" : {
        "name": "Pas de bras, pas de chocolat", 
        "type": "magic_scroll",
        "tags": [],
        "ingredients": {"ecorce_ancienne": 1, "eau_enchantee": 4, "aile_de_fee": 1},
        "level_required": None,
        "source" : "client",
        "demand": 0.8,
        "price": 40, 
        "xp": 40,
        "upgrade_cost": 80
    },


    "harissa_revenge" : {
        "name": "Vengeance à la harissa", 
        "type": "magic_scroll",
        "tags": [],
        "ingredients": {"ecorce_ancienne": 1, "eau_enchantee": 4, "aile_de_fee": 3},
        "level_required": None,
        "source" : "client",
        "demand": 0.8,
        "price": 60, 
        "xp": 60,
        "upgrade_cost": 90
    },


    #===================== GRIMOIRES ============================

    "murphys_laws": {
        "name": "Les Lois de Murphy", 
        "type": "spell_book",
        "tags": [],
        "ingredients": {"herbe_lunaire": 2, "champignon_sombre": 3},
        "level_required": 1,
        "demand": 0.5,
        "price": 18, 
        "xp": 12,
        "upgrade_cost": 50
    },


    "cakes_and_politics": {
        "name": "Cakes et politique", 
        "type": "spell_book",
        "tags": [],
        "ingredients": {"herbe_lunaire": 2, "champignon_sombre": 3, "ecorce_ancienne": 2, "eau_enchantee": 6},
        "level_required": 3,
        "demand": 0.8,
        "price": 30, 
        "xp": 30,
        "upgrade_cost": 70
    },


    "tax_haven_from_hell_to_hell_yeah": {
        "name": "Paradis fiscal : de l'enfer au nirvana", 
        "type": "spell_book",
        "tags": ["irs"],
        "ingredients": {"herbe_lunaire": 2, "champignon_sombre": 3, "ecorce_ancienne": 2, "eau_enchantee": 6, "aile_de_fee": 3},
        "level_required": 4,
        "demand": 0.8,
        "price": 40, 
        "xp": 40,
        "upgrade_cost": 80
    },


    "mimi_the_restroom_queen": {
        "name": "Mimi sur le trône", 
        "type": "spell_book",
        "tags": [],
        "ingredients": {"herbe_lunaire": 5, "champignon_sombre": 2, "ecorce_ancienne": 4, "eau_enchantee": 6, "aile_de_fee": 3},
        "level_required": None,
        "demand": 0.8,
        "price": 60, 
        "xp": 45,
        "upgrade_cost": 80
    },


    "sexy_djinns_and_pentagrams": {
        "name": "Djinns sexy et pentagrammes", 
        "type": "spell_book",
        "tags": [],
        "ingredients": {"eau_enchantee": 4, "aile_de_fee": 3, "pierre_noire": 3, "aconit": 2},
        "level_required": 5,
        "demand": 0.7,
        "price": 60, 
        "xp": 45,
        "upgrade_cost": 100
    },


    "agile": {
        "name": "La Méthode à Gilles", 
        "type": "spell_book",
        "tags": ["corporate"],
        "ingredients": {"poussiere_etoile": 2, "ecorce_ancienne": 5, "eau_enchantee": 4, "pierre_noire": 3, "aconit": 3},
        "level_required": 6,
        "demand": 0.6,
        "price": 70, 
        "xp": 50,
        "upgrade_cost": 110
    }, 


    "jean_marc_synergie_all_songs_lyrics": {
        "name": "Les grands succès de Jean-Marc Synergie : Coworking sentimental, Mergeons nos vies, Confcall me now, Organigramme de nos amours...", 
        "type": "spell_book",
        "tags": ["corporate"],
        "ingredients": {"poussiere_etoile": 2, "ecorce_ancienne": 5, "eau_enchantee": 4, "pierre_noire": 1, "aconit": 1},
        "level_required": None,
        "demand": 0.9,
        "price": 80, 
        "xp": 70,
        "upgrade_cost": 110
    },

    
    "the_devils_best_breakfast_recipes": {
        "name": "Les petits déj d'enfer du Diable", 
        "type": "spell_book",
        "tags": [],
        "ingredients": {"ecorce_ancienne": 1, "eau_enchantee": 4, "aile_de_fee": 3, "croc_feroce": 3, "bezoard": 2, "ecaille_dragon": 3},
        "level_required": 7, 
        "demand": 0.9,
        "price": 90, 
        "xp": 70,
        "upgrade_cost": 120
    }
}