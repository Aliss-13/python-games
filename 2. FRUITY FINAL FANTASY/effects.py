import sac_a_dos

def appliquer_brulure(cible, effet):
    cible["vie"] -= effet["degats"]
    print(f"{cible['nom']} subit {effet['degats']} dégâts de {effet['nom']} ❤️‍🔥 !")

def appliquer_poison(cible, effet):
    cible["vie"] -= effet["degats"]
    print(f"{cible['nom']} subit {effet['degats']} dégâts de {effet['nom']} ☠️ !")

def appliquer_melancolie(cible, effet):
    cible["vie"] -= effet["degats"]
    print(f"{cible['nom']} subit {effet['degats']} dégâts de {effet['nom']} 😭 !")

def appliquer_regeneration(cible, effet):
    stats = sac_a_dos.get_stats(cible)
    cible["vie"] = min(cible["vie"] + effet["soin"], stats["vie_max"])
    print(f"{cible['nom']} bénéficie de {effet['nom']} 🪴 et gagne {effet['soin']} PV !")

def appliquer_bouclier(cible, effet):
    print(f"{cible['nom']} bénéficie de {effet['nom']} 🛡 (-{int(effet['reduction']*100)}%) !")

def appliquer_stun(cible, effet):
    return any(effet["nom"] == "stun" for effet in cible["effets"])

effets_handlers = {
    "poison" : appliquer_poison,
    "brûlure" : appliquer_brulure,
    "mélancolie" : appliquer_melancolie,
    "régénération" : appliquer_regeneration,
    "bouclier" : appliquer_bouclier,
    "stun" : appliquer_stun
}
   
def debut_tour(cible):
    
    print(f"\nEffets de {cible['nom']} :", [effet["nom"] for effet in cible["effets"]])
   
    if not cible["effets"]:
        print("Aucun effet actif.")
        return
    
    nouveaux_effets = []
    
    for effet in cible["effets"]:
        handler = effets_handlers.get(effet["nom"])
        if handler:
            handler(cible, effet)
            effet["duree"] -= 1
        if effet["duree"] > 0:
            nouveaux_effets.append(effet)
            
        else:
            print(f"L'effet {effet['nom']} disparaît de {cible['nom']}.")

    cible["effets"] = nouveaux_effets
    print("Effets restants :", [effet["nom"] for effet in cible["effets"]])