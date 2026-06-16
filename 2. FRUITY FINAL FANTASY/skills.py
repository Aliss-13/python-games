import random
import data
import copy
import sac_a_dos


def use_skill(personnage, equipe, ennemi):
    
    skill = skills[personnage["skill"]]
    # personnage["skill"] => "boule_feu" par ex
    # => skills["boule_feu"] => {"fonction" : boule_feu, "type" : "attaque", "cout_mana": 10, "puissance": 2}
    
    skill["fonction"](personnage, equipe, ennemi, skill)
    # => déclenche la fonction boule_feu

def coup_puissant(personnage, equipe, ennemi, skill):
    cout = skill["cout_vie"]
    
    if personnage["vie"] <= cout:
        print(f"{personnage['nom']} n'a pas assez d'énergie !")
        return
    
    personnage["vie"] -= cout
    stats = sac_a_dos.get_stats(personnage)
    degats = stats["puissance"] * skill["puissance"]
    print(f"{personnage['nom']} lance un ⚔️ Coup puissant ⚔️ (-{cout} PV, {degats} dégâts) et inflige {degats} points de dégâts !")
    ennemi["vie"] -= degats

    # effet bouclier
    chance = random.random() # entre 0 et 1
    effets = data.effets
    if chance < effets["bouclier"]["proba"]:
        effet = copy.deepcopy(effets["bouclier"])
        protec_perso = random.choice(equipe)
        effets_actifs = [effet["nom"] for effet in ennemi["effets"]]
        if effet["nom"] not in effets_actifs:
            protec_perso["effets"].append(effet)
            print(f"{protec_perso['nom']} bénéficie de {effet['nom']} !")
    
    if ennemi["vie"] <= 0:
        ennemi["vie"] = 0
        return
    
    else:
        print(f"{ennemi['nom']} n'a plus que {ennemi['vie']} PV !")

def boule_feu(personnage, equipe, ennemi, skill):
    cout = skill["cout_mana"]
    
    if personnage["mana"] < cout:
        print("Pas assez de mana !")
        return

    # dégâts normaux
    personnage["mana"] -= cout
    stats = sac_a_dos.get_stats(personnage)
    degats = stats["puissance"] * skill["puissance"]
    print(f"{personnage['nom']} lance une 🔥Boule de feu🔥 (-{cout} mana, mana : {personnage['mana']})") 
    print(f"{personnage['nom']} inflige {degats} points de dégâts !")
    
    ennemi["vie"] -= degats
     
    # effet brûlure
    chance = random.random() # entre 0 et 1
    effets = data.effets
    effet = copy.deepcopy(effets["brûlure"])
    if chance < effet["proba"]:
        # copy.deepcopy () permet de faire une copie propre de l'effet sans le copier partout
        effets_actifs = [effet["nom"] for effet in ennemi["effets"]]
        if effet["nom"] not in effets_actifs:
            ennemi["effets"].append(effet)
            print(f"{ennemi['nom']} subit {effet['nom']} !")
              
    if ennemi["vie"] <= 0:
        ennemi["vie"] = 0
        return
    
    else:
        print(f"{ennemi['nom']} n'a plus que {ennemi['vie']} PV !")
    
def benediction(personnage, equipe, ennemi, skill):
    cout = skill["cout_mana"]
    if personnage["mana"] < cout:
        print("Pas assez de mana !")
        return
    
    personnage["mana"] -= cout
    stats = sac_a_dos.get_stats(personnage)
    print(f"{personnage['nom']} lance une 🙏 Bénédiction de groupe 🙏 (-{cout} mana, mana : {personnage['mana']}) !")
    for cible in equipe: 
        if cible["vie"] > 0:
            stats_c = sac_a_dos.get_stats(cible)
            soin = stats["puissance"] * skill["puissance"]
            cible_pv = min(cible["vie"] + soin, stats_c["vie_max"])
            soin_reel = cible_pv - cible["vie"]
            cible_pv = cible['vie'] + soin_reel
            cible["vie"] = cible_pv
            print(f"{cible['nom']} gagne (+ {soin_reel} PV) !")
            print(f"{cible['nom']} a maintenant {cible["vie"]} PV !")
            
        # effet régénération
    effets = data.effets
    if random.random() < effets["régénération"]["proba"]:
        effet = copy.deepcopy(effets["régénération"])
        regen_perso = random.choice(equipe)
        effets_actifs = [effet["nom"] for effet in ennemi["effets"]]
        if effet["nom"] not in effets_actifs:
            regen_perso["effets"].append(effet)
            print(f"{regen_perso['nom']} bénéficie de {effet['nom']} !")
        
skills = {
    "coup_puissant" : {"fonction" : coup_puissant, "type" : "attaque", "cout_vie": 10, "puissance": 2},
    "boule_feu" : {"fonction" : boule_feu, "type" : "attaque", "cout_mana": 10, "puissance": 2},
    "benediction" : {"fonction" : benediction, "type" : "soin", "cout_mana": 10, "puissance": 10}
}

def soin_personnage(equipe):
    soigneur = None # Anticipe s'il n'y a pas de soigneur dans l'équipe, empêche les erreurs de type "nameError not defined" plus bas
    for personnage in data.equipe:
        if personnage["skill"] == "benediction":
            soigneur = personnage
            break
    if soigneur is None:
        return

    stats = sac_a_dos.get_stats(personnage)
    allies = [personnage for personnage in data.equipe if personnage["vie"] > 0 and personnage["vie"] < stats["vie_max"]]
    if not allies:
        return

    cible = min(allies, key=lambda personnage: personnage["vie"]/stats["vie_max"])
    stats_c = sac_a_dos.get_stats(cible)
    # key (= critère de comparaison) lambda range les personnages en fonction de leur pourcentage de vie
    # cible le personnage qui a le moins de vie en pourcentage
    soin = stats["puissance"] * 2
    soin_reel = min(stats_c['vie_max'] - cible['vie'], soin)
    cible_pv = cible['vie'] + soin_reel
    cible["vie"] = cible_pv
    print(f"{cible['nom']} gagne (+ {soin_reel} PV) !")
    print(f"{cible['nom']} a maintenant {cible["vie"]} PV !")

def attaque_basique(personnage, equipe, ennemi):
    if personnage["skill"] == "benediction":
        soin_personnage(equipe)

    else:
        stats = sac_a_dos.get_stats(personnage)
        degats = stats["puissance"]
        ennemi["vie"] -= degats
        print(f"⚔ {personnage['nom']} → {ennemi['nom']} : -{degats} PV")
        if ennemi["vie"] > 0:
            print(f"{ennemi['nom']} n'a plus que {ennemi['vie']} PV !")