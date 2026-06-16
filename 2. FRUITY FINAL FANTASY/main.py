import traceback
import data
import affichage
import ui
import combat
import sac_a_dos

try:
    print("\n===== FFF ======")
    sac_a_dos.ajouter_item(data.inventaire, "plume_phenix") # équivalent à : data.inventaire.append({"item" : "plume_phenix"})
    sac_a_dos.ajouter_item(data.inventaire, "potion_revigorante")
    affichage.afficher_inventaire(data.inventaire)
    ui.separator()
    for personnage in data.equipe:
        print(f"{personnage['nom']} - {personnage['vie']}")
    combat.combat(data.equipe, data.ennemis, data.inventaire)
except Exception as e:
    traceback.print_exc()

input("Appuie sur entrée pour quitter")