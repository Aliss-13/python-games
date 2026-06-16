def valider_commande_dict(d):
    required = ["id", "demande", "gain_xp", "pieces", "tier_max", "temps_restant"]

    missing = [k for k in required if k not in d]
    if missing:
        raise ValueError(f"Commande invalide, clés manquantes: {missing}")


class Commande:
    def __init__(self, id, demande, gain_xp, pieces, tier_max, temps_restant, prioritaire=False):
        self.id = id
        self.demande = demande
        self.gain_xp = gain_xp
        self.pieces = pieces
        self.tier_max = tier_max
        self.temps_restant = temps_restant
        self.temps_initial = temps_restant
        self.prioritaire = prioritaire

    def to_dict(self):
        return {
            "id": self.id,
            "demande": self.demande,
            "gain_xp": self.gain_xp,
            "pieces": self.pieces,
            "tier_max" : self.tier_max,
            "temps_restant": self.temps_restant,
            "temps_initial": self.temps_initial,
            "prioritaire": self.prioritaire
        }
    

    @classmethod
    def from_dict(cls, d):
        valider_commande_dict(d)
        return cls(
            id=d["id"],
            demande=d["demande"],
            gain_xp=d["gain_xp"],
            pieces=d["pieces"],
            tier_max=d["tier_max"],
            temps_restant=d["temps_restant"],
            prioritaire=d.get("prioritaire", False)
            )
    
    