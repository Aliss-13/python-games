from models.joueur import Joueur
from models.commande import Commande
from models.plante import Plante


class GameState:
    def __init__(self):
        self.version = 1
        self.joueur = Joueur()
        self.commandes_en_cours = []
        self.next_commande_id = 0
        self.tour = 0
        self.graines_disponibles = set([1])

    def to_dict(self):
        return {
            "version": self.version,
            "joueur": self.joueur.to_dict(),
            "commandes_en_cours": [commande.to_dict() for commande in self.commandes_en_cours],
            "next_commande_id": self.next_commande_id,
            "tour": self.tour,
            "graines_disponibles": list(self.graines_disponibles)
        }
    
    @classmethod
    def from_dict(cls, data):
        state = cls()

        joueur_data = data.get("joueur", {})

        state.joueur.pieces = joueur_data.get("pieces", 0)
        state.joueur.xp = joueur_data.get("xp", 0)
        state.joueur.niveau = joueur_data.get("niveau", 1)
        state.joueur.potager_max = joueur_data.get("potager_max", 5)
        state.joueur.garde_manger = dict(joueur_data.get("garde_manger", {}))
        state.joueur.inventaire = dict(joueur_data.get("inventaire", {}))
        state.joueur.potager = [Plante.from_dict(plante) for plante in joueur_data.get("potager", [])]
        state.commandes_en_cours = [Commande.from_dict(commande) for commande in data.get("commandes_en_cours", [])]
        state.next_commande_id = data.get("next_commande_id", 0)
        state.tour = data.get("tour", 0)
        state.graines_disponibles = set(data.get("graines_disponibles", [1]))

        return state