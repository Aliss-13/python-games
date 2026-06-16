import random
import data
import copy
import affichage
import ui
import level
import effects
import menu
import sac_a_dos


def get_morts(equipe):
    return [personnage for personnage in equipe if personnage["vie"] <= 0]

def get_vivants(equipe):
    return [personnage for personnage in equipe if isinstance(personnage, dict) and personnage.get("vie", 0) > 0]

def get_ennemis_vivants(ennemis):
    return [ennemi for ennemi in ennemis if isinstance(ennemi, dict) and ennemi.get("vie", 0) > 0]

def ordre_initiative(equipe, ennemi):
    
    tous = equipe + [ennemi]
    return sorted(
        tous, 
        key = lambda entite : sac_a_dos.get_stats(entite)["vitesse"], 
        reverse=True
    )

def calcul_degats(ennemi, cible):
    reduction_totale = 0
    degats = random.randint(5, ennemi["puissance"])
    for effet in cible["effets"]:
        if effet["nom"] == "bouclier":
            reduction_totale += effet["reduction"]
            reduction_totale = min(reduction_totale, 0.9)
    return int(degats * (1 - reduction_totale))

def gerer_debut_tour(entite):
    effects.debut_tour(entite)
    for effet in entite['effets']:
        if effects.appliquer_stun(entite, effet):
            print (f"{entite['nom']} est stun ⛔️ et ne joue pas !")
            return False
    
    return True

def tour_ennemi(equipe, ennemi):
    print(f"\n---Tour de {ennemi['nom']}---")
    if ennemi["vie"] <= 0:
        return
    
    if not gerer_debut_tour(ennemi):
        return
    
    vivants = get_vivants(equipe).copy()
    if not vivants:
        return
    cible = random.choice(vivants)
    degats = calcul_degats(ennemi, cible)
    cible["vie"] -= degats
    print(f"⚔ {ennemi['nom']} → {cible['nom']} : -{degats} PV")
        
    if cible["vie"] <= 0:
        cible["vie"] = 0
        print(f"{cible['nom']} est KO.")
    
    else:
        print(f"{cible['nom']} n'a plus que {cible['vie']} PV !")
    
    # effets des attaques selon l'ennemi
    for effet_attaque in ennemi.get("effet_attaque", []): 
        # get permet de renvoyer une liste vide si la clé n'existe pas chez l'ennemi
        effet = copy.deepcopy(data.effets[effet_attaque]) 
        
        if random.random() < effet["proba"]:
            effets_actifs = [effet["nom"] for effet in cible["effets"]]
            
            if effet["nom"] not in effets_actifs:
                cible["effets"].append(effet)
                print(f"{cible['nom']} subit {effet_attaque} !")
            
def tour_joueur(personnage, equipe, ennemi, inventaire):
    ui.separator()
    ui.header(f"Tour de {personnage['nom']}")
    sac_a_dos.calcul_stats(personnage)
    stats = sac_a_dos.get_stats(personnage)
    
    print(f"PV : {personnage['vie']} / {stats['vie_max']}")
    if "mana" in personnage:
        print(f"mana : {personnage['mana']} / {stats['mana_max']}")
    print(f"Puissance : {stats['puissance']} / Vitesse : {stats['vitesse']}")

    if not gerer_debut_tour(personnage):
        return
    
    menu.menu_tour(personnage, equipe, ennemi, inventaire)

def un_tour(equipe, ennemi, inventaire):
    ordre = ordre_initiative(get_vivants(equipe), ennemi)

    for entite in ordre:
        # mort → skip
        if entite.get("vie", 0) <= 0:
            continue
        if entite in equipe:
            tour_joueur(entite, equipe, ennemi, inventaire)
            if ennemi["vie"] <= 0:
                return "ennemi mort"
        else:
            tour_ennemi(equipe, ennemi)
            if all(personnage["vie"] <= 0 for personnage in equipe):
                return "defaite"
    
    return "continuer"

def combat(equipe, ennemis, inventaire):
    while get_ennemis_vivants(ennemis):
        ennemi_base = random.choice(get_ennemis_vivants(ennemis))
        ennemi = level.scale_ennemi(equipe, ennemi_base)
        print("\nUn ennemi apparaît !")
        affichage.afficher_ennemi(ennemi)
        
        while ennemi["vie"] > 0:
            result = un_tour(equipe, ennemi, inventaire)
            
            if result == "ennemi mort":
                print(f"{ennemi['nom']} est vaincu !")
                loot = level.generer_loot(ennemi)
                
                affichage.afficher_loot(loot)
                level.ajouter_loot(inventaire, loot)
                level.gain_xp(equipe, ennemi)
                ennemis.remove(ennemi_base)
                
                break
            
            if result == "defaite":
                print("GAME OVER")
                return
    
    print("Victoire totale !")