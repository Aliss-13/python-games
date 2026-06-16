import random
import display

class Player:

    def __init__(self):
        self.satiety = 50
        self.satiety_max = 100
        self.stamina = 80
        self.stamina_max = 100
        self.mentalhealth = 100
        self.mentalhealth_max = 100
        self.flying_dutchman_parts = []
        self.inventory = {"🪵" : 0, "🪨" : 0, "🌿" : 0, "🪢" : 0, "🟩" : 0, "💰": 0}
        self.food = {"🥩" : 0, "🍖" : 0, "🥛" : 0, "🧀" : 3}
        self.stuff = {"tête" : None, "corps" : None, "mains" : None, "pieds" : None}
        self.tools = {"axe": False, "pickaxe": False, "knife": False, "scythe" : False}
        self.structures = {
            "campfire": False, 
            "shelter" : False, 
            "sewing_machine" : False,
            "faraday_cage" : False,
            "portable_shower" : False,
            "banjo" : False,
            "livestock" : False, 
            "creamery" : False, 
            "dairy" : False}
        self.flying_dutchman = False

    
    def to_dict(self):

        return {
            "satiety": self.satiety,
            "stamina": self.stamina,
            "mentalhealth": self.mentalhealth,
            "flying_dutchman_parts" : self.flying_dutchman_parts,
            "inventory": self.inventory,
            "food" : self.food,
            "stuff": self.stuff,
            "structures": self.structures,
            "tools": self.tools
        }

    def from_dict(self, data):

        self.satiety = data["satiety"]
        self.stamina = data["stamina"]
        self.mentalhealth = data["mentalhealth"]
        self.flying_dutchman_parts = data["flying_dutchman_parts"]
        self.inventory = data["inventory"]
        self.food = data["food"]
        self.stuff = data["stuff"]
        self.structures = data["structures"]
        self.tools = data["tools"]

#============================ Le joueur est-il en vie ? ===========================================
    def is_alive(self):

        self.stamina = max(0, self.stamina)
        self.satiety = max(0, self.satiety)
        self.mentalhealth = max(0, self.mentalhealth)

        if self.stamina <= 0:
            print("☠️  Epuisement... 🪫")
            return False

        if self.satiety <= 0:
            print("☠️  Famine... 🦴")
            return False
        
        if self.mentalhealth <= 0:
            print("☠️  Folie... 👀")
            return False

        return True
        
#============================ Conditions climatiques (saisonnières/météo) ===========================================
    def apply_climate_conditions(self, world):

        # --- WINTER ---
        if world.season == "hiver":
            cold_penalty = 5
            satiety_penalty = 3

            # équipements réduisent le froid
            if self.stuff["tête"] == "chapeau":
                cold_penalty -= 1

            if self.stuff["corps"] == "manteau":
                cold_penalty -= 2
                satiety_penalty += 2

            cold_penalty = max(0, cold_penalty)

            self.stamina -= cold_penalty
            self.satiety += satiety_penalty

            if not self.is_alive():
                return False

            print(f"❄️  Le froid t'épuise (-{cold_penalty}) endurance, +{satiety_penalty} faim.")

            return True

        # --- NIGHT ---
        if world.time_of_day == "nuit":
            night_penalty = 2

            if self.stuff["tête"] == "chapeau":
                night_penalty -= 1

            if self.stuff["corps"] == "manteau":
                night_penalty -= 1

            night_penalty = max(0, night_penalty)

            self.stamina -= night_penalty
            self.mentalhealth -= night_penalty
            
            if not self.is_alive():
                return False
            
            print(f"🌙 La nuit te transit (-{night_penalty} endurance, -{night_penalty} santé mentale).")

            return True

#============================ Production passive grâce aux buildings ===========================================
    def produce_resources(self, world):

        if world.time_of_day == "jour":

            if self.structures.get("banjo"):
                self.mentalhealth += 5
                self.mentalhealth = min(self.mentalhealth + 5, self.mentalhealth_max)
                print("🪕 +5 santé mentale (banjo) « Ça me rappelle un film... »")

            if self.structures.get("creamery"):
                self.food["🥛"] += 5
                print("🥛 +5 lait (laiterie)")

        if world.time_of_day == "nuit":

            if self.structures.get("portable_shower"):
                self.mentalhealth += 10
                self.mentalhealth = min(self.mentalhealth + 10, self.mentalhealth_max)
                print("🚿 +10 santé mentale (douche portative) « Ça fait du bien une bonne douche ! »")

            if self.structures.get("livestock"):
                self.food["🥩"] += 5
                print("🥩 +5 viande (élevage)")

#============================ Dormir ===========================================
    def sleep(self, world):

        if self.structures["shelter"]:
            if self.satiety < 10:
                print("Tu as trop faim pour dormir.")
                return False
            
            self.stamina += 50
            self.stamina = min(self.stamina + 50, self.stamina_max)
            self.satiety -= 10
            self.mentalhealth += 10
            self.mentalhealth = min(self.mentalhealth + 10, self.mentalhealth_max)
            print("Tu dors à l'abri 🛖  (-10 satiété, +10 santé mentale, max endurance)")
            display.display_bars_simple(self)
        
        else:
            if self.satiety < 20:
                print("Tu as trop faim pour dormir.")
                return False
            
            self.stamina += 30
            self.stamina = min(self.stamina + 30, self.stamina_max)
            self.satiety -= 20
            self.mentalhealth += 5
            self.mentalhealth = min(self.mentalhealth + 5, self.mentalhealth_max)
            print(f"Tu dors dans le froid 🌙 (+20 faim, +30 endurance)")
            display.display_bars_simple(self)
        
        world.next_cycle(self)

        return True
        
#============================ Récolte ===========================================
    def roll_rare_loot(self, resource):
        if resource == "🪨":
            if random.randint(1, 100) <= 40:
                self.inventory["💰"] += 1
                print("✨ Pépite d'or trouvée !")
    

    def gather(self, resource, world, min_amount=1, max_amount=3):
       
        # effort
        effort_cost = 5

        if self.stuff["mains"] == "gants":
            effort_cost -= 1

        if self.stuff["pieds"] == "bottes":
            effort_cost -= 2

        effort_cost = max(0, effort_cost)

        if self.stamina < effort_cost: 
            print("Tu n'as pas assez d'énergie pour récolter quoi que ce soit.")
            return False
        
        if self.satiety < effort_cost:
            print("Tu as trop faim pour récolter quoi que ce soit.")
            return False
            
        self.stamina -= effort_cost
        self.satiety -= effort_cost
        
        # coût de l'action
        cost = 1

        if not world.spend_action(cost):
            return
        
        world.check_cycle(self)
        
        # adaptation des ressources au terrain
        biome = world.areas[world.current_area]
        success_rate = biome.get(resource, 10)
        

        # nuit danger
        if world.time_of_day == "nuit":
            if random.randint(1, 100) < 40:
                attack_damage = 10

                if self.structures["faraday_cage"]:
                    attack_damage -= 7

                self.stamina -= attack_damage
                print(f"Tu es attaqué pendant la récolte (-{attack_damage} endurance) !")
                display.display_bars_simple(self)
                
                if not self.is_alive():
                    return False
                
                return True


        # réussite de la récolte
        if random.randint(1, 100) <= success_rate:
            amount = random.randint(min_amount, max_amount)


            # modif du résultat du random selon la saison
            modifier = world.get_season_modifier(resource)
            amount = max(0, int(amount * modifier))


            # bonus outils
            if resource == "🪵" and self.tools.get("axe"):
                amount += 1
            if resource == "🪨" and self.tools.get("pickaxe"):
                amount += 1
            if resource == "🌿" and self.tools.get("scythe"):
                amount += 1
            if resource == "🥩" and self.tools.get("knife"):
                amount += 1

            if resource in self.food:
                self.food[resource] += amount

            if resource in self.inventory:
                self.inventory[resource] += amount


            # chance loot rare : or
            self.roll_rare_loot(resource)

            # récolte réussie
            print(f"Tu travailles dur (-{effort_cost} endurance, -{effort_cost} satiété)")
            print(f"Tu récoltes : {amount} {resource}")
            display.display_bars_simple(self)
            
        # récolte ratée
        else:
            print(f"Tu travailles dur (-{effort_cost} endurance, -{effort_cost} satiété)")
            print(f"Tu ne trouves pas de {resource}.")
            display.display_bars_simple(self)

        return True
#============================ Amélioration ressources de base ===========================================
    def braid_rope(self):
        print("🪢 = 3🌿")
        
        try:
            quantite = int(input("Quantité : "))

            if quantite <= 0:
                print("Quantité invalide.")
                return

        except ValueError:
            print("Entrée invalide.")
            return
        
        if self.inventory["🌿"] < 3:
            print("Pas assez de 🌿.")
            return

        self.inventory["🌿"] -= 3*quantite
        self.inventory["🪢"] += quantite

        print(f"Corde tressée : (+{quantite} 🪢)")


    def make_cloth(self):
        print("🟩 = 3🪢") 
        if not self.structures["sewing_machine"]:
            print("Pas de machine à coudre.")
            return
        
        try:
            quantite = int(input("Quantité : "))

            if quantite <= 0:
                print("Quantité invalide.")
                return

        except ValueError:
            print("Entrée invalide.")
            return
        
        if self.inventory["🪢"] < 3:
            print("Pas assez de 🪢.")
            return

        self.inventory["🪢"] -= 3
        self.inventory["🟩"] += 1

        print(f"Tissu : (+{quantite} 🟩)")


    def cook_food(self):

        if not self.structures["campfire"]:
            print("Pas de feu de camp.")
            return
            
        try:
            quantite = int(input("Quantité : "))

            if quantite <= 0:
                print("Quantité invalide.")
                return

        except ValueError:
            print("Entrée invalide.")
            return
        
        if self.food["🥩"] < quantite:
            print("Pas assez d'aliments à cuire.")
            return

        self.food["🥩"] -= quantite
        self.food["🍖"] += quantite

        print(f"Nourriture cuite : (+{quantite} 🍖)")


    def cheese_making(self):

        if not self.structures["dairy"]:
            print("Pas de fromagerie.")
            return
            
        try:
            quantite = int(input("Quantité : "))

            if quantite <= 0:
                print("Quantité invalide.")
                return

        except ValueError:
            print("Entrée invalide.")
            return
        
        if self.food["🥛"] < quantite:
            print("Pas assez de lait.")
            return

        self.food["🥛"] -= quantite
        self.food["🧀"] += quantite

        print(f"Fromage : (+{quantite} 🧀)")