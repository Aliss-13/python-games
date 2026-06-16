# dans Data, stocker uniquement des structures
# pas de fonction !

couleurs = {
    "commun": "\033[90m",       # gris
    "inhabituel": "\033[92m",   # vert
    "rare" : "\033[94m",        # bleu
    "epique": "\033[95m",       # violet
    "legendaire" : "\033[93m",   # orange
    "reset" : "\033[0m"
}

effets = {
    "brûlure" : {"nom" : "brûlure", "proba" : 0.3, "duree" : 3, "degats" : 4},
    "poison" : {"nom" : "poison", "proba" : 0.3, "duree" : 3, "degats" : 5},
    "mélancolie" : {"nom" : "mélancolie", "proba" : 0.3, "duree" : 3, "degats" : 5},
    "régénération" : {"nom" : "régénération", "proba" : 0.3, "duree" : 4, "soin" : 6},
    "bouclier" : {"nom" : "bouclier", "proba" : 0.5, "duree" : 2, "reduction" : 0.5},
    "stun" : {"nom" : "stun", "proba" : 0.4, "duree" : 2}
}

ennemis = [
    {
        "nom": "Gobelin novice",
        "tier": 1,
        "vie": 160,
        "puissance": 55,
        "vitesse" : 9,
        "effets" : [], 
        "effet_attaque" : ["poison"],
        "loot_table": "basique",
        "rarete" : "commun",
        "xp" : 70
    },
    {
        "nom": "Gobelin Vétéran",
        "tier": 2,
        "vie": 220,
        "puissance": 70,
        "vitesse" : 12,
        "effets" : [], 
        "effet_attaque" : ["poison"],
        "loot_table": "ameliore",
        "rarete" : "inhabituel",
        "xp" : 100
    },
    {
        "nom": "Gobelin Berserker",
        "tier": 3,
        "vie": 260,
        "puissance": 90,
        "vitesse" : 15,
        "effets" : [], 
        "effet_attaque" : ["poison"],
        "loot_table": "rare",
        "rarete" : "rare",
        "xp" : 130
    },

     {
        "nom": "Corbeau Malade",
        "tier": 1,
        "vie": 160,
        "puissance": 50,
        "vitesse" : 10,
        "effets" : [], 
        "effet_attaque" : ["mélancolie"],
        "loot_table": "basique",
        "rarete" : "commun",
        "xp" : 80
    },
    {
        "nom": "Grand Corbeau Malade",
        "tier": 2,
        "vie": 250,
        "puissance": 65,
        "vitesse" : 15,
        "effets" : [], 
        "effet_attaque" : ["mélancolie"],
        "loot_table": "ameliore",
        "rarete" : "inhabituel",
        "xp" : 100
    },
    {
        "nom": "Grand Corbeau Putride",
        "tier": 3,
        "vie": 260,
        "puissance": 90,
        "vitesse" : 15,
        "effets" : [], 
        "effet_attaque" : ["mélancolie"],
        "loot_table": "rare",
        "rarete" : "rare",
        "xp" : 120
        },
    {
        "nom": "Orc simplet",
        "tier": 1,
        "vie": 160,
        "puissance": 55,
        "vitesse" : 7,
        "effets" : [], 
        "effet_attaque" : ["stun"],
        "loot_table": "basique",
        "rarete" : "commun",
        "xp" : 70
    },
    {
        "nom": "Orc colérique",
        "tier": 2,
        "vie": 220,
        "puissance": 75,
        "vitesse" : 10,
        "effets" : [], 
        "effet_attaque" : ["stun"],
        "loot_table": "ameliore",
        "rarete" : "inhabituel",
        "xp" : 100
    },
    {
        "nom": "Orc enragé",
        "tier": 3,
        "vie": 260,
        "puissance": 90,
        "vitesse" : 12,
        "effets" : [], 
        "effet_attaque" : ["stun"],
        "loot_table": "rare",
        "rarete" : "rare",
        "xp" : 130
    }
]

inventaire = []

objets = {
    "plume_phenix": {"type": "consommable", "rarete": "rare", "effet": "resurrection","soin": 50},
    "potion_revigorante": {"type": "consommable", "rarete": "inhabituel", "effet": "gain_pv", "soin": 80},
    "gants_puissance" : {"type" : "equipement", "classe" : ["magie", "cac"], "slot" : "mains", "rarete" : "commun", "bonus" : {"puissance" : 10}},
    "anneau_de_pouvoir" : {"type" : "equipement", "classe" : ["magie", "cac"], "slot" : "mains", "rarete" : "commun", "bonus" : {"puissance" : 10}},
    "gants_brillants" : {"type" : "equipement", "classe" : ["magie", "cac"], "slot" : "mains", "rarete" : "inhabituel", "bonus" : {"vie_max" : 20}},
    "chaussures_ailees" : {"type" : "equipement", "classe" : ["magie", "cac"], "slot" : "pieds", "rarete" : "commun", "bonus" : {"vitesse" : 3}},
    "souliers_rouges" : {"type" : "equipement", "classe" : ["magie", "cac"], "slot" : "pieds", "rarete" : "inhabituel", "bonus" : {"vitesse" : 5}},
    "bottes_de_7_lieues" : {"type" : "equipement", "classe" : ["magie", "cac"], "slot" : "pieds", "rarete" : "rare", "bonus" : {"vitesse" : 7}},
    "robe_brodee" : {"type" : "equipement", "classe" : ["magie"], "slot" : "armure", "rarete" : "commun", "bonus" : {"mana_max" : 10}},
    "robe_de_sorcier" : {"type" : "equipement", "classe" : ["magie"], "slot" : "armure", "rarete" : "inhabituel", "bonus" : {"mana_max" : 20}},
    "champ_force" : {"type" : "equipement", "classe" : ["magie"], "slot" : "armure", "rarete" : "rare", "bonus" : {"vie_max" : 40}},
    "radiance" : {"type" : "equipement", "classe" : ["magie"], "slot" : "armure", "rarete" : "epique", "bonus" : {"vie_max" : 60}},
    "epee_fer" : {"type" : "equipement", "classe" : ["cac"], "slot" : "arme", "rarete" : "commun", "bonus" : {"puissance" : 10}},
    "claymore" : {"type" : "equipement", "classe" : ["cac"], "slot" : "arme", "rarete" : "inhabituel", "bonus" : {"puissance" : 20}},
    "cimeterre" : {"type" : "equipement", "classe" : ["cac"], "slot" : "arme", "rarete" : "rare", "bonus" : {"puissance" : 40}},
    "armure_fer" : {"type" : "equipement", "classe" : ["cac"], "slot" : "armure", "rarete" : "commun", "bonus" : {"vie_max" : 20}},
    "armure_brillante" : {"type" : "equipement", "classe" : ["cac"], "slot" : "armure", "rarete" : "inhabituel", "bonus" : {"vie_max" : 30}},
    "armure_du_roi" : {"type" : "equipement", "classe" : ["cac"], "slot" : "armure", "rarete" : "rare", "bonus" : {"vie_max" : 40}},
    "baton_brillant" : {"type" : "equipement", "classe" : ["magie"], "slot" : "arme", "rarete" : "commun", "bonus" : {"puissance" : 10}},
    "sceptre_lunaire" : {"type" : "equipement", "classe" : ["magie"], "slot" : "arme", "rarete" : "inhabituel", "bonus" : {"puissance" : 20}},
    "orbe_solaire" : {"type" : "equipement", "classe" : ["magie"], "slot" : "arme", "rarete" : "rare", "bonus" : {"puissance" : 30}},
    "vortex_cosmique" : {"type" : "equipement", "classe" : ["magie"], "slot" : "arme", "rarete" : "epique", "bonus" : {"puissance" : 50}}
}

loot_tables = {
    "basique" : [
        {"item" : "chaussures_ailees", "chance" : 0.8},
        {"item" : "gants_puissance", "chance" : 0.8},
        {"item" : "robe_brodee", "chance" : 0.6}, 
        {"item" : "epee_fer", "chance" : 0.5},
        {"item" : "baton_brillant", "chance" : 0.5},
        {"item" : "armure_fer", "chance" : 0.6},
        {"item" : "armure_brillante", "chance" : 0.2},
        {"item" : "claymore", "chance" : 0.2},
        {"item" : "robe_de_sorcier", "chance" : 0.2},
        {"item" : "sceptre_lunaire", "chance" : 0.2}
        ],

    "ameliore" : [
        {"item" : "anneau_de_pouvoir", "chance" : 0.8},
        {"item" : "potion_revigorante", "chance" : 0.5},
        {"item" : "souliers_rouges", "chance" : 0.6}, 
        {"item" : "robe_de_sorcier", "chance" : 0.5},
        {"item" : "sceptre_lunaire", "chance" : 0.5},
        {"item" : "armure_brillante", "chance" : 0.6},
        {"item" : "claymore", "chance" : 0.5},
        {"item" : "sceptre_lunaire", "chance" : 0.2},
        {"item" : "orbe_solaire", "chance" : 0.2},
        {"item" : "armure_du_roi", "chance" : 0.2}
        ],

    "rare" : [
        {"item" : "bottes_de_7_lieues", "chance" : 0.6},
        {"item" : "potion_revigorante", "chance" : 0.8},
        {"item" : "champ_force", "chance" : 0.6}, 
        {"item" : "cimeterre", "chance" : 0.5},
        {"item" : "sceptre_lunaire", "chance" : 0.5},
        {"item" : "orbe_solaire", "chance" : 0.6},
        {"item" : "armure_du_roi", "chance" : 0.6},
        {"item" : "vortex_cosmique", "chance" : 0.2},
        {"item" : "radiance", "chance" : 0.2}
        ]
}


equipe = [ 
    {
        "nom" : "Guerrier", 
        "classe" : "cac", 
        "vie" : 100,
        "base_stats": {"vie_max": 100, "puissance": 20,"vitesse": 8},  
        "skill" : "coup_puissant",
        "effets" : [],
        "niveau" : 1,
        "xp" : 0,
        "equipement" : {"arme" : None, "armure" : None, "mains" : None, "pieds" : None},
        "bonus": {"vie_max": 0, "puissance": 0, "vitesse": 0}
        },
    {
        "nom" : "Mage",
        "classe" : "magie",
        "vie" : 70,
        "base_stats": {"vie_max": 70, "mana_max" : 50, "puissance": 15,"vitesse": 12},  
        "mana" : 50, 
        "skill" : "boule_feu",
        "effets" : [],
        "niveau" : 1,
        "xp" : 0,
        "equipement" : {"arme" : None, "armure" : None, "mains" : None, "pieds" : None},
        "bonus" : {"vie_max" : 0, "mana_max" : 0, "puissance" : 0, "vitesse" : 0}
    },
    {
        "nom" : "Prêtre",
        "classe" : "magie",
        "vie" : 60, 
        "base_stats": {"vie_max": 60, "mana_max" : 50, "puissance": 10,"vitesse": 12}, 
        "mana" : 50,  
        "skill" : "benediction",
        "effets" : [],
        "niveau" : 1,
        "xp" : 0,
        "equipement" : {"arme" : None, "armure" : None, "mains" : None, "pieds" : None},
        "bonus" : {"vie_max" : 0, "mana_max" : 0, "puissance" : 0, "vitesse" : 0}
    }
]