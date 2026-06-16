from data.graine import graines

class Plante:

    def __init__(self, graine, temps=0):
        self.graine = graine
        self.temps = temps

    def to_dict(self):
        return {
            "graine_id": self.graine.id,
            "temps": self.temps
        }

    @classmethod
    def from_dict(cls, d):
        

        return cls(
            graine=graines[d["graine_id"]],
            temps=d["temps"]
        )

    @classmethod
    def from_graine(cls, graine):
        return cls(graine)

    @property
    def nom(self):
        return self.graine.nom

    @property
    def tier(self):
        return self.graine.tier

    @property
    def croissance(self):
        return self.graine.croissance

    def pousser(self):
        self.temps += 1

    def est_pourrie(self):
        return self.temps >= self.croissance * 2

    def est_prete(self):
        return self.temps >= self.croissance