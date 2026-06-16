import random


class World:

    def __init__(self):
        self.time_of_day = "jour"  # jour / nuit
        self.day_count = 1
        self.season = "printemps"
        self.season_day = 1
        self.actions_remaining = 7
        self.day_actions = 7
        self.night_actions = 3
        self.in_winter = False
        self.first_winter_survived = False
        self.areas = {
                    "forêt": {"🪵": 90, "🥩": 80, "🌿": 80},
                    "montagne": {"🪨": 90, "💰": 70, "🪵": 60,  "🥩": 40},
                    "plaine": {"🥩": 90, "🌿": 80, "🪨": 40, "🪵": 40},
                    "désert" : {"🪨": 60, "🥩": 40, "💰": 40}, 
                    "rivière" : {"🥩": 90, "🪨": 60, "💰": 40}, 
                    "jungle" : {"🪵": 90, "🌿": 80, "🥩": 80},
                    "grotte" : {"🪨": 90, "💰": 70}
                    }
        self.connections = {
                    "forêt": ["plaine", "rivière", "montagne", "jungle"],
                    "plaine": ["forêt", "désert"],
                    "rivière": ["forêt", "jungle", "désert"],
                    "montagne": ["forêt", "grotte"],
                    "grotte": ["montagne"],
                    "jungle": ["forêt", "rivière"],
                    "désert": ["plaine", "rivière"]
                    }
        self.flying_dutchman_parts = {
                    "forêt": "⚙️ Engrenage étrange",
                    "montagne": "🔩 Hélice en acier trempé",
                    "grotte": "💎 Cristal énergétique",
                    "rivière": "⛓️ Turbine hydraulique",
                    "désert": "☀️ Voile solaire",
                    "jungle": "🧭 Boussole ancestrale",
                    "plaine": "📜 Plans du Hollandais Volant"
                    }
        self.current_area = "plaine"
        self.explored_areas = set()
        self.explored_areas.add(self.current_area)

    def to_dict(self):

        return {
            "time_of_day": self.time_of_day,
            "day_count": self.day_count,
            "season": self.season,
            "season_day": self.season_day,
            "actions_remaining": self.actions_remaining,
            "current_area" : self.current_area,
            "explored_areas" : list(self.explored_areas)
        }

    def from_dict(self, data):

        self.time_of_day = data["time_of_day"]
        self.day_count = data["day_count"]
        self.season = data["season"]
        self.season_day = data["season_day"]
        self.actions_remaining = data["actions_remaining"]
        self.current_area = data["current_area"]
        self.explored_areas = set(data.get("explored_areas", []))
        if not self.explored_areas:
            self.explored_areas.add(self.current_area)


#============================ Actions ===========================================
    def spend_action(self, cost=1):
        if self.actions_remaining < cost:
            print("Pas assez d'actions.")
            return False

        self.actions_remaining -= cost
        return True


    def check_cycle(self, player):
        if self.actions_remaining > 0:
            return

        self.next_cycle(player)

        if self.time_of_day == "jour":
            self.actions_remaining = self.day_actions
        else:
            self.actions_remaining = self.night_actions


#============================ Cycle jour/nuit et cycle des saisons ===========================================
    def next_cycle(self, player):
      
        self.update_cycle_durations()

        if self.time_of_day == "jour":
            self.time_of_day = "nuit"
            print("🌙 La nuit tombe...")

        else:
            self.time_of_day = "jour"
            self.day_count += 1
            self.season_progress()
            self.check_events()
            print(f"🌞 Jour {self.day_count} commence ({self.season})")

        player.apply_climate_conditions(self)
        player.produce_resources(self)


    def update_cycle_durations(self):

        if self.season == "été":
            self.day_actions = 8
            self.night_actions = 2

        elif self.season == "automne":
            self.day_actions = 6
            self.night_actions = 4

        elif self.season == "hiver":
            self.day_actions = 4
            self.night_actions = 6

        elif self.season == "printemps":
            self.day_actions = 7
            self.night_actions = 3


    def season_progress(self):

        self.season_day += 1

        if self.season == "été" and self.season_day > 10:
            self.season = "automne"
            self.season_day = 1
            print("🍂  L'automne chasse l'été...")

        elif self.season == "automne" and self.season_day > 10:
            self.season = "hiver"
            self.season_day = 1
            self.in_winter = True
            print("❄️  L'hiver est là !")

        elif self.in_winter and self.season == "printemps":
            self.first_winter_survived = True
            self.in_winter = False
            print("🌸  Le printemps pointe son nez...")

        elif self.season == "printemps" and self.season_day > 10:
            self.season = "été"
            self.season_day = 1
            print("☀️  L'été fait son entrée !")


    def get_season_modifier(self, resource):
    
        if self.season == "hiver":
            if resource in ["🥩"]:
                return 0.2   # 80% de réduction viande
            if resource in ["🌿"]:
                return 0.5
            return 1.0

        return 1.0

#============================ Evènements ===========================================
    def check_events(self):

        self.attaque_monstres()

        self.tempête_neige()


    def attaque_monstres(self):
        if self.day_count == 15 and random.randint(1, 100) < 25:
            print("👹  Des créatures rôdent dans la nuit...")
            attack_damage = 20
            mentalhealth_damage = 10

            if self.structures["faraday_cage"]:
                attack_damage -= 7
                mentalhealth_damage -=5


                self.stamina -= attack_damage
                self_mentalhealth -= mentalhealth_damage
                print(f"Attaque de monstres (-{attack_damage} endurance - {mentalhealth_damage} santé mentale) !")
                
                if not self.is_alive():
                    return False
                
                return True
            

    def tempête_neige(self):
        if self.season == "hiver" and random.randint(1, 100) < 20:
            print("❄️  Une tempête de neige frappe le camp !")
            snow_damage = 30

            if self.stuff["tête"] == "chapeau":
                snow_damage -= 8

            if self.stuff["corps"] == "manteau":
                snow_damage -= 15

            snow_damage = max(0, snow_damage)

            self.stamina -= snow_damage
            print(f"🌙 La tempête de neige te gèle (-{snow_damage} endurance).")
           
            if not self.is_alive():
                return False
                        
            return True

#============================ Exploration et déplacements ===========================================
    

    #============================ Flying Dutchman - Hollandais Volant ===========================================
    def find_flying_dutchman_parts(self, player):

        area = self.current_area

        if area in self.flying_dutchman_parts:
            part = self.flying_dutchman_parts[area]

        if part not in player.flying_dutchman_parts:
            player.flying_dutchman_parts.append(part)
            print("⚓ Une énergie étrange flotte dans l'air...Le Hollandais Volant semble plus proche !")
            print(f"🎉Tu trouves : {part}")
            return part

        else:
            return None
    

    def search_flying_dutchman_parts(self, player):

        print("Tu explores les environs... Peut être que tu y trouveras quelque chose de spécial !")

        cost_satiety = 5
        cost_stamina = 5
        
        # vérification AVANT de modifier
        if player.stamina < cost_stamina: 
            print("Pas assez d'énergie pour partir en exploration.")
            return False
        
        if player.satiety < cost_satiety:
            print("Trop faim pour pour partir en exploration.")
            return False
        
        player.satiety -= cost_satiety
        player.stamina -= cost_stamina
        
        if random.randint(1, 100) <= 25:
            self.find_flying_dutchman_parts(player)

        else:
            print("Tu rentres broucouille.")


    def explore_area(self, player):
        
        cost = 4

        if not self.spend_action(cost):
            return
        
        self.check_cycle(player)

        nearby_unknown = [
            area
            for area in self.connections[self.current_area]
            if area not in self.explored_areas
        ]

        if not nearby_unknown:
            print("Aucune nouvelle zone à découvrir depuis ici.")
            return

        new_area = random.choice(nearby_unknown)
        
        cost_satiety = 30
        cost_stamina = 30
        
        # vérification AVANT de modifier
        if player.stamina < cost_stamina: 
            print("Pas assez d'énergie pour partir en exploration.")
            return False
        
        if player.satiety < cost_satiety:
            print("Trop faim pour pour partir en exploration.")
            return False
        
        player.satiety -= cost_satiety
        player.stamina -= cost_stamina

        self.explored_areas.add(new_area)
            
        print(f"🔓 Nouvelle zone découverte : {new_area}")


    def move_player(self, player, new_area):
        
        cost = 2

        if not self.spend_action(cost):
            return
        
        self.check_cycle(player)

        if new_area not in self.explored_areas:
            print("❌ Zone non explorée.")
            return False

        if new_area not in self.connections[self.current_area]:
            print("❌ Zone non accessible depuis ici.")
            return False

        cost_satiety = 30
        cost_stamina = 30
        
        # vérification AVANT de modifier
        if player.stamina < cost_stamina: 
            print("Pas assez d'énergie pour partir en exploration.")
            return False
        
        if player.satiety < cost_satiety:
            print("Trop faim pour pour partir en exploration.")
            return False
        
        player.satiety -= cost_satiety
        player.stamina -= cost_stamina
        
        self.current_area = new_area
        
        print(f"🌍 Tu te déplaces vers {new_area}")
        return True
    

    