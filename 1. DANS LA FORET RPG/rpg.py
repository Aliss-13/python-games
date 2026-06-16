import random

# ==== PERSONNAGE ====

nom = input("Quel est ton nom ? :")
joueur = {
    "nom": nom, 
    "vie": 100, 
    "vie_max" : 100, 
    "attaque": 20, 
    "mana" : 30, 
    "mana_max" : 30, 
    "arme" : None, 
    "armure" : None,
    "rune" : None,
    "potion_vie": 3,
    "potion_mana": 0,
    "xp": 0, 
    "niveau": 1
}

# ==== MONSTRE ====

monstres = [{"nom":"Gobelin", "genre" : "m", "vie": 60, "vie_max" : 60, "attaque": 10, "xp" : 35, "boss" : False}, 
            {"nom":"Orc", "genre" : "m", "vie": 80, "vie_max" : 80, "attaque": 15, "xp" : 40, "boss" : False},
            {"nom":"Squelette", "genre" : "m", "vie": 40, "vie_max" : 40, "attaque": 12, "xp" : 20, "boss" : False},
            {"nom":"Sorcière", "genre" : "f", "vie" : 35, "vie_max" : 35, "attaque": 9, "xp" : 15, "boss" : False},
            {"nom":"Goule blessée", "genre" : "f", "vie" : 5, "vie_max" : 35, "attaque": 9, "xp" : 5, "boss" : False},
            {"nom":"Harpie", "genre" : "f", "vie" : 30, "vie_max" : 30, "attaque": 11, "xp" : 10, "boss" : False}
           ]

boss = [{"nom":"Miranda", "genre" : "f", "vie": 125, "vie_max" : 125, "attaque": 20, "xp" : 100, "boss" : True}, 
            {"nom":"Dali", "genre" : "m", "vie": 130, "vie_max" : 130, "attaque": 22, "xp" : 150, "boss" : True}
            ]

def adapter_monstre(monstre, joueur):
    niveau = joueur["niveau"]
    monstre = monstre.copy() # copy permet de ne pas modifier le monstre de la liste, donc de recharger le monstre avec ses stats d'origine.
    monstre["vie"] += niveau * 10
    monstre["vie_max"] += niveau * 10
    monstre["attaque"] += niveau * 2
    monstre["xp"] = monstre.get("xp", 20) + niveau * 5
    return monstre
    
# ==== EQUIPEMENT ====
# un grand dictionnaire qui contient plusieurs dictionnaires

equipements = {
    "Epée rouillée" : {"type":"arme", "attaque" : 5, "niveau" : 1}, 
    "Grande épée" : {"type":"arme", "attaque" : 10, "niveau" : 2},
    "Flamberge" : {"type":"arme", "attaque" : 15, "niveau" : 3},
    "Claymore" : {"type":"arme", "attaque" : 20, "niveau" : 4},
    "Bouclier" : {"type":"armure", "vie_max" : 20, "niveau" : 1},
    "Bouclier blasonné" : {"type" : "armure", "vie_max" : 40, "niveau" : 2},
    "Pavois" : {"type" : "armure", "vie_max" : 50, "niveau" : 3},
    "Palladium" : {"type" : "armure", "vie_max" : 60, "niveau" : 4},
    "Eihwaz" : {"type" : "rune", "mana_max" : 10, "niveau" : 1},
    "Uruz" : {"type" : "rune", "mana_max" : 20, "niveau" : 2},
    "Jera" : {"type" : "rune", "mana_max" : 25, "niveau" : 3}, 
    "Wunjo" : {"type" : "rune", "mana_max" : 30, "niveau" : 4}
            }
inventaire = []

def equiper_objet(joueur, objet):
    equipement = equipements[objet]
    
    if equipement["type"] == "arme":
        ancienne_arme = joueur["arme"]
        
        if ancienne_arme is not None: # retirer bonus ancienne arme
            ancien_bonus = equipements[ancienne_arme]["attaque"]
            joueur["attaque"] -= ancien_bonus
            inventaire.append(ancienne_arme)
            print(f"{ancienne_arme} retourne dans l'inventaire.")
        
        joueur["arme"] = objet # équiper nouvelle arme
        bonus = equipement["attaque"]
        joueur["attaque"] += bonus
        print(f"{joueur['nom']} équipe {objet} ! Attaque : {joueur['attaque']}")
    
    elif equipement["type"] == "armure":
        ancienne_armure = joueur["armure"]
        
        if ancienne_armure is not None: # retirer bonus ancienne armure
            ancien_bonus = equipements[ancienne_armure]["vie_max"]
            joueur["vie_max"] -= ancien_bonus
            inventaire.append(ancienne_armure)
            print(f"{ancienne_armure} retourne dans l'inventaire.")
        
        joueur["armure"] = objet # équiper nouvelle armure
        bonus = equipement["vie_max"]
        joueur["vie_max"] += bonus
        print(f"{joueur['nom']} équipe {objet} ! Vie max : {joueur['vie_max']}")
    
    elif equipement["type"] == "rune":
        ancienne_rune = joueur["rune"]
        
        if ancienne_rune is not None: # retirer bonus ancienne rune
            ancien_bonus = equipements[ancienne_rune]["mana_max"]
            joueur["mana_max"] -= ancien_bonus
            inventaire.append(ancienne_rune)
            print(f"{ancienne_rune} retourne dans l'inventaire.")
        
        joueur["rune"] = objet # équiper nouvelle armure
        bonus = equipement["mana_max"]
        joueur["mana_max"] += bonus
        print(f"{joueur['nom']} équipe {objet} ! Mana max : {joueur['mana_max']}")


def menu_equipement(joueur, inventaire):
    afficher_inventaire(inventaire)
    choix = input("\nQuel objet veux-tu équiper ?").strip().lower()
    objet_trouve = None
    for item in inventaire:
        if item.lower() == choix.lower():
            objet_trouve = item
            break
    if objet_trouve:
        equiper_objet(joueur, objet_trouve)
        inventaire.remove(objet_trouve)
    else:
        print("Objet introuvable.")

# ==== AFFICHAGE ==== 

def afficher_inventaire(inventaire):
    print(f"\nInventaire de {joueur['nom']}:")
    if len(inventaire) == 0:
        print ("Vide (triste mais honnête).")
    else:
        for item in inventaire:
            print(f"-{item}") 

def afficher_nom_monstre(monstre):
    nom = monstre["nom"]
    genre = monstre["genre"]
    if nom[0].lower() in "aeiouy":
        return f"L'{nom}"
    if genre == "f":
        return f"La {nom}"
    if genre == "m":
        return f"Le {nom}"
    
def afficher_vie_joueur(joueur):
    total = joueur["vie_max"]
    vie = joueur["vie"]

    barres = int(vie / total * 10)
    vide = 10 - barres

    print(f"Vie {joueur['nom']} : [{'█' * barres}{'.' * vide}] {vie}/{total}")

def afficher_mana_joueur(joueur):
    total = joueur["mana_max"]
    mana = joueur["mana"]

    barres = int(mana / total * 10)
    vide = 10 - barres

    print(f"Mana {joueur['nom']} : [{'█' * barres}{'.' * vide}] {mana}/{total}")

def afficher_vie_monstre(monstre):
    total = monstre["vie_max"]
    vie = monstre["vie"]

    barres = int(vie / total * 10)
    vide = 10 - barres

    print(f"Vie {monstre['nom']} : [{'█' * barres}{'.' * vide}] {vie}/{total}")

# ==== RECOMPENSES ====

def xp_requis(niveau):
    return 50 + (niveau - 1) * 25 # niveau 1 = 50, niveau 2 = 75, niveau 3 = 100 etc.

def level_up(joueur):
    joueur["xp"] = joueur.get("xp", 0) # si une valeur existe on prend, sinon on prend 0
    joueur["niveau"] = joueur.get("niveau", 1)
    while joueur["xp"] >= xp_requis(joueur["niveau"]):
        joueur["xp"] -= xp_requis(joueur["niveau"]) 
        joueur["niveau"] +=1
        joueur["vie_max"] += 20
        joueur["vie"] = joueur["vie_max"]
        joueur["mana_max"] += 10
        joueur["mana"] = joueur["mana_max"]
        joueur["attaque"] += 5
        print(f"\nLEVEL UP ! {joueur['nom']} passe au niveau {joueur['niveau']} !")
        print(f"+20 pv, +5 attaque, +10 mana")
        print(joueur)
        
def recompense(joueur, monstre): 
    # on donne les paramètres pour chaque fonction. 
    # La fonction recompense utilise "joueur"(dictionnaire) et "inventaire"(liste)
    # par contre elle crée la liste loots donc pas besoin de la rajouter dans la parenthèse
    accessibles = [
        item for item in equipements.keys()
        if equipements[item]["niveau"] == joueur["niveau"]]
    
    loots = ["Potion de vie", "Potion de mana", "Rien hihi"] + accessibles
    
    loots_boss = []
    for nom, equipement in equipements.items():
        if equipement["niveau"] == 4:
            loots_boss.append(nom)
    
    if monstre["boss"]:
        loot = random.choice(loots_boss)
    else:
        loot = random.choice(loots)
            
    xp_gagne = monstre.get("xp", 20) 
    # la fonction get va chercher la valeur de la première clé ("xp rapportée du monstre"), sinon elle prend la valeur 20 par défaut
    joueur["xp"] = joueur.get("xp", 0) + xp_gagne 
    # la fonction get va chercher la valeur de la première clé ("xp du joueur"), sinon elle prend la valeur 0 par défaut.
    print(f"{joueur['nom']} gagne {monstre['xp']} xp !")
    
    if loot == "Rien hihi":
        print(f"{joueur['nom']} ne récupère rien.")
    
    elif loot == "Potion de vie":
        joueur["potion_vie"] += 1
        print(f"{joueur['nom']} récupère une potion de vie ! Il en a maintenant {joueur['potion_vie']}.")

    elif loot == "Potion de mana":
        joueur["potion_mana"] += 1
        print(f"{joueur['nom']} récupère une potion de mana ! Il en a maintenant {joueur['potion_mana']}.")
        
    else:
        print(f"{joueur['nom']} récupère {loot}!")
        if loot in equipements:
            equipement = equipements[loot]
            if equipement["type"] == "arme":
                print(f"+{equipement['attaque']} attaque !")
            if equipement["type"] == "armure":
                print (f"+{equipement['vie_max']} vie max !")
            if equipement["type"] == "rune":
                print(f"+{equipement['mana_max']} mana max !")
        choix = input("Veux-tu équiper cet objet ? Oui/Non :")
        if choix.lower() == "oui":
            equiper_objet(joueur, loot)
        else:
            inventaire.append(loot)
            print(f"{joueur['nom']} range {loot} dans son inventaire.")
        
# ==== ACTION ====

def attaque_monstre(joueur, monstre):
    degats = random.randint(8, monstre["attaque"])
    joueur["vie"] -= degats
    if joueur["vie"] <= 0: # ne pas afficher de PV négatifs
        joueur["vie"] = 0
        return f"{joueur['nom']} est mort."
    print(f"{afficher_nom_monstre(monstre)} attaque {joueur['nom']} ! {afficher_nom_monstre(monstre)} inflige {degats} dégâts !")
    afficher_vie_joueur(joueur)
    
def action(joueur, monstre):
    while monstre["vie"] > 0 and joueur["vie"] > 0:
        choix = input("Attaque(a), Magie(m), Potion de vie(p), Potion de mana(pm), Inventaire(in) ou Fuir(f) ?").strip().lower()
        
        if choix == "a":
            degats = random.randint(10, joueur["attaque"]) # randint crée un entier aléatoire entre un min et un max.
            monstre["vie"] -= degats
            print(f"{joueur['nom']} attaque {afficher_nom_monstre(monstre)} ! {joueur['nom']} inflige {degats} dégâts !")
            if verifier_fin_combat(joueur, monstre):
                break
            afficher_vie_monstre(monstre)
            afficher_vie_joueur(joueur)
            attaque_monstre(joueur, monstre)
        
        elif choix == "m":
            if joueur["mana"] >= 10:
                joueur["mana"] -= 10
                degats = random.randint(joueur["attaque"], joueur["attaque"]*2)
                monstre["vie"] -= degats
                print(f"°•*⁀➷ Attaque puissante ! {joueur['nom']} inflige {degats} dégâts !")
                if verifier_fin_combat(joueur, monstre):
                    break
                afficher_vie_monstre(monstre)
                afficher_mana_joueur(joueur)
                attaque_monstre(joueur, monstre)
            
            elif joueur["mana"] < 10:
                print("Pas assez de mana !")         
            
        elif choix == "p":
            if joueur["potion_vie"] > 0 :
                joueur["vie"] = min(joueur["vie"]+30, joueur["vie_max"])
                joueur["potion_vie"] -=1
                print(f"{joueur['nom']} boit une potion de vie !")
                print(f"Ses points de vie sont maintenant de {joueur['vie']} et il lui reste {joueur['potion_vie']} potions de vie.")
                attaque_monstre(joueur, monstre)
            else:
                print(f"{joueur['nom']} n'a plus de potion de vie !")

        elif choix == "pm":
            if joueur["potion_mana"] > 0 :
                joueur["mana"] = min(joueur["mana"]+20, joueur["mana_max"])
                joueur["potion_mana"] -=1
                print(f"{joueur['nom']} boit une potion de mana !")
                print(f"Ses points de mana sont maintenant de {joueur['mana']} et il lui reste {joueur['potion_mana']} potions de mana.")
                attaque_monstre(joueur, monstre)
            else:
                print(f"{joueur['nom']} n'a plus de potion de mana !")
        
        elif choix == "in":
            menu_equipement(joueur, inventaire)
        
        elif choix == "f":
            print(f"{joueur['nom']} prend la fuite !")
            return 
        
        else: 
            print("Action inconnue.")
            
# ==== COMBAT ====

def fin_combat(joueur, monstre):
        print(f"{joueur['nom']} gagne le combat !")
        recompense(joueur, monstre)
        afficher_inventaire(inventaire)
        level_up(joueur)

def verifier_fin_combat(joueur, monstre):
    if monstre["vie"] <= 0:
        monstre["vie"] = 0
        afficher_vie_monstre(monstre)
        afficher_vie_joueur(joueur)
        fin_combat(joueur, monstre)
        return True

    if joueur ["vie"] <= 0:
        joueur ["vie"] = 0
        afficher_vie_monstre(monstre)
        afficher_vie_joueur(joueur)
        print(f"{joueur['nom']} est vaincu.")
        return True
            
    return False
            
def combat():
    for i in range(6):
        if i == 3:
            monstre = random.choice(boss).copy()
            print("\n===BOSS===")
            print(f"{afficher_nom_monstre(monstre)} apparaît !")
            action(joueur, monstre)
        else:
            monstre_base = random.choice(monstres)
            monstre = adapter_monstre(monstre_base, joueur)
            print (f"{afficher_nom_monstre(monstre)} apparaît !")
            action(joueur, monstre)

# ===LAUNCH===

try:
    print("==== mini RPG ====")
    print("Tududum...")
    print(f"{joueur['nom']} entre dans la forêt...")
    combat()
except Exception as e:
    print("\nErreur:")
    print(e)

input("\nAppuie sur entrée pour quitter...")  