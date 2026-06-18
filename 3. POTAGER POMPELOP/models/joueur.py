# ❌ input dans Joueur
# ❌ print dans Joueur
# ❌ accès à GRAINES dans Joueur
# ❌ logique de boutique dans Joueur


# Joueur → cerveau du personnage
# main.py → mains + interface
# Plante → objet du monde
class Joueur:

    def __init__(self):
        self.pieces = 50
        self.xp = 0
        self.niveau = 1
        self.potager_max = 5
        self.garde_manger = {}
        self.inventaire = {}
        self.potager = []
        self.prestige = 0
        self.game_won = False

    def to_dict(self):
        return {
            "pieces": self.pieces,
            "xp": self.xp,
            "niveau": self.niveau,
            "potager_max": self.potager_max,
            "garde_manger": dict(self.garde_manger),
            "inventaire": dict(self.inventaire),
            "potager": [plante.to_dict() for plante in self.potager],
            "prestige": self.prestige
        }


    def ajouter_plante(self, plante):
        self.potager.append(plante)

    
    def retirer_plante(self, index):
        if 0 <= index < len(self.potager):
            return self.potager.pop(index)
        raise IndexError("Index de plante invalide")  
    
    
    def ajouter_xp(self, xp):
        self.xp += xp


    def ajouter_pieces(self, pieces):
        self.pieces += pieces


    def payer(self, montant):
        if self.pieces < montant:
            return False
        self.pieces -= montant
        return True
    
    
    def ajouter_item(self, nom, quantite=1):
        self.inventaire[nom] = self.inventaire.get(nom, 0) + quantite


    def ajouter_recolte(self, nom, quantite=1):
        self.garde_manger[nom] = self.garde_manger.get(nom, 0) + quantite


    def retirer_item(self, nom, quantite=1):
        if nom not in self.inventaire:
            return False

        self.inventaire[nom] -= quantite

        if self.inventaire[nom] <= 0:
            del self.inventaire[nom]

        return True
     