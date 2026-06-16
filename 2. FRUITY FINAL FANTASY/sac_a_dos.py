import data

def ajouter_item(inventaire, item_id):
    inventaire.append({"item": item_id})

def retirer_item(inventaire, index):
    if not isinstance(index, int):
        print("Index invalide :", index)
        return None

    return inventaire.pop(index)

def get_item(inventaire, choix):
    if not isinstance(choix, int):
        return None, None

    if choix < 0 or choix >= len(inventaire):
        return None, None

    item = inventaire[choix]

    if not isinstance(item, dict):
        return None, None

    item_id = item.get("item")

    if item_id not in data.objets:
        return None, None

    return item_id, data.objets[item_id]

def appliquer_effet_objet(equipe, item):
    
    effet = item.get("effet")
    for personnage in equipe :
        stats = get_stats(personnage)
    
    if effet == "gain_pv":
        allies = [personnage for personnage in data.equipe if personnage["vie"] > 0 and personnage["vie"] < stats["vie_max"]]
        if not allies:
            return
        
        cible = min(allies, key=lambda personnage: personnage["vie"]/stats["vie_max"])
        # key (= critère de comparaison) lambda range les personnages en fonction de leur pourcentage de vie
        # cible le personnage qui a le moins de vie en pourcentage
        stats_c = get_stats(cible)
        soin = item["soin"]
        soin_reel = min(stats_c['vie_max'] - cible['vie'], soin)
        cible_pv = cible['vie'] + soin_reel
        cible["vie"] = cible_pv
        print(f"{cible['nom']} gagne (+ {soin_reel} PV) !")
        print(f"{cible['nom']} a maintenant {cible["vie"]} PV !")

    if effet == "resurrection":
        
        morts = [p for p in equipe if p["vie"] <= 0]
        if not morts:
            print("Personne à ressusciter.")
            return

        print("\nCibles :")

        for i, perso in enumerate(morts):
            print(f"{i} - {perso['nom']}")

            try:
                cible_choix = int(input("Choisir cible : "))
            except ValueError:
                return
    
            cible = morts[cible_choix]
            stats_c = get_stats(cible)
            cible["vie"] = min(item["soin"], stats_c["vie_max"])
            print(f"{cible['nom']} revient à la vie avec {item['soin']} PV !")

def utiliser_objet(equipe, inventaire):

    try:
        choix = int(input("Choisir numéro de l'objet :"))
    except ValueError:
        print("Entrée invalide.")
        return

    if choix < 0 or choix >= len(inventaire):
        print("Choix invalide.")
        return

    item_id, item = get_item(inventaire, choix)
    
    if item_id is None:
        return
    if item["type"] != "consommable":
        print("Cet objet n'est pas un consommable.")
        return
    
    appliquer_effet_objet(equipe, item)
    
    retirer_item(inventaire, choix)
    print(f"{item_id} disparaît de l'inventaire !")

def get_stats(entite):

    if "base_stats" not in entite:
        return {
            "vie_max": entite.get("vie_max", entite.get("vie", 100)),
            "puissance": entite.get("puissance", 10),
            "vitesse": entite.get("vitesse", 10)
        }

    stats = entite["base_stats"].copy()

    for key, value in entite["bonus"].items():
        stats[key] += value

    return stats

def calcul_stats(personnage):
    stats = personnage["base_stats"].copy()
    for stat, val in personnage["bonus"].items():
        stats[stat] += val
    return stats
    
def equiper_depuis_inventaire(personnage, inventaire):

    try:
        choix = int(input("Choisir numéro de l'objet :"))
    except ValueError:
        print("Entrée invalide.")
        return

    if choix < 0 or choix >= len(inventaire):
        print("Choix invalide.")
        return

    item_id, item = get_item(inventaire, choix)
    
    if item_id is None:
        return
    
    if item["type"] == "consommable":
        print("Cet objet est un consommable.")
        return

    if personnage["classe"] not in item["classe"]:
        print("Classe incompatible")
        return

    slot = item["slot"]
    

    ancien_id = personnage["equipement"].get(slot)
    ancien = data.objets[ancien_id] if ancien_id else None

    if ancien:
        for stat, val in ancien["bonus"].items():
            personnage["bonus"][stat] -= val
            calcul_stats(personnage)

        inventaire.append({"item": ancien_id})

    personnage["equipement"][slot] = item_id

    for stat, val in item["bonus"].items():
        personnage["bonus"][stat] += val
        calcul_stats(personnage)
    
    retirer_item(inventaire, choix)

    print(f"{personnage['nom']} équipe {item_id}")