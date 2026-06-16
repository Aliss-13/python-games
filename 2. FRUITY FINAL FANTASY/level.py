import copy
import random
import data
import ui
import sac_a_dos

def xp_requis(niveau):
    return 50 + ((niveau - 1) * 25) # niveau 1 = 50 xp requis, niveau 2 = 75 xp requis, niveau 3 = 100 xp requis etc.

def niveau_moyen(equipe):
    return sum((personnage["niveau"]) for personnage in equipe) / len(equipe)
    
def scale_ennemi(equipe, ennemi):
    ennemi_scaled = copy.deepcopy(ennemi)
    niveau_equipe = niveau_moyen(equipe)
    facteur = 1 + (niveau_equipe - ennemi["tier"]) * 0.1
    ennemi_scaled['vie'] = int(ennemi_scaled['vie'] * facteur)
    ennemi_scaled['puissance'] = int(ennemi_scaled['puissance'] * facteur)
    ennemi_scaled['vitesse'] = int(ennemi_scaled['vitesse'] * facteur)
    ennemi_scaled["vitesse"] = ennemi_scaled.get("vitesse", 10)
    return ennemi_scaled

def level_up(personnage):
    personnage["niveau"] +=1
    personnage["base_stats"]["vie_max"] += 20
    personnage["vie"] = personnage["base_stats"]["vie_max"]
    personnage["base_stats"]["puissance"] += 5
    personnage["base_stats"]["vitesse"] += 5
    if "mana" in personnage:
        personnage["base_stats"]["mana_max"] += 10
        personnage["mana"] = personnage["base_stats"]["mana_max"]
    print(f"LEVEL UP ! {personnage['nom']} passe au niveau {personnage['niveau']} !")
    print(f"{personnage['nom']} - PV : {personnage["base_stats"]['vie_max']} - puissance : {personnage["base_stats"]['puissance']} - vitesse : {personnage["base_stats"]['vitesse']}")
    if "mana" in personnage:
        print(f"mana : {personnage["base_stats"]["mana_max"]}")
          
def gain_xp(equipe, ennemi):
    xp_gagne = ennemi["xp"]
    for personnage in equipe:
        if personnage["vie"] > 0:
            personnage["xp"] += xp_gagne
            ui.separator()
            print(f"{personnage['nom']} gagne {xp_gagne} XP !")
            while personnage["xp"] >= xp_requis(personnage["niveau"]):
                requis = xp_requis(personnage["niveau"]) 
                personnage["xp"] -= requis
                level_up(personnage)

def generer_loot(ennemi):
    table = data.loot_tables.get(ennemi["loot_table"], [])
    loot = []
    max_loot = 2
    
    for drop in table:
        if len(loot) >= max_loot:
            break

        if random.random() < drop["chance"]:
            loot.append({"item": drop["item"], "quantite": 1})

    return loot

def ajouter_loot(inventaire, loot):
    inventaire.extend(loot)