class Graine:
    def __init__(self, id, nom, tier, croissance, prix, loot=None):
        self.id = id
        self.nom = nom
        self.tier = tier
        self.croissance = croissance
        self.prix = prix
        self.loot = loot or []

    @classmethod
    def from_dict(cls, id, data):
        return cls(
            id,
            data["nom"],
            data["tier"],
            data["croissance"],
            data["prix"],
            data.get("loot", [])
        )
    
    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "tier": self.tier,
            "croissance": self.croissance,
            "prix": self.prix,
            "loot": self.loot
        }





