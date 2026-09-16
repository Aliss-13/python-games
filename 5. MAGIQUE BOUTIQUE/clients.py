import random
from clients_queue import WaitingClient
from clients_choices import CHOICES
from clients_results import RESULTS
from progression import level_up, gain_rewards, register_sale
import time


class Client:

    def __init__(self, id, name, dialogue, choices, level_required=1, patience=0):
        self.id = id
        self.name = name
        self.dialogue = dialogue
        self.choices = choices
        self.level_required = level_required
        self.patience = patience
        self.arrival_time = None
        self.requested_items = []

    def display(self):
        print(f"{self.name} entre.")
        print(f'"{self.dialogue}"')


    def display_choices(self):
        for i, choice in enumerate(self.choices, 1):
            print(f"[{i}] {choice.text}")


# ========================================== DATA =======================================================

CLIENTS = {

    "tax_specialist_goblin": Client(
        id="tax_specialist_goblin",
        name="Gobelin fiscaliste",
        dialogue="Bonjour. Je souhaiterais frauder légalement.",
        choices=[
            CHOICES["choice_tax_specialist_goblin.tax_audit"],
            CHOICES["choice_tax_specialist_goblin.tax_haven"],
            CHOICES["choice_tax_specialist_goblin.shop_closed"]
        ],
        level_required=7,
        patience=300
    ),

    "romantic_demon": Client(
        id="romantic_demon",
        name="Démon romantique",
        dialogue="Bonjour, charmante sorcière. Je voudrais séduire une succube.",
        choices=[
            CHOICES["choice_romantic_demon.bbl"],
            CHOICES["choice_romantic_demon.love_potion"],
            CHOICES["choice_romantic_demon.bbl_love_potion"]
        ],
        level_required=8,
        patience=600
    ),

    "gourmet_wizard": Client(
        id="gourmet_wizard",
        name="Sorcier Gourmand",
        dialogue="Bonjour, pourriez vous me conseiller de bonnes recettes de cuisine ?.",
        choices=[
            CHOICES["choice_gourmet_wizard.cakes_and_politics"],
            CHOICES["choice_gourmet_wizard.devils_breakfast"],
            CHOICES["choice_gourmet_wizard.top_chef"]
        ],
        level_required=9,
        patience=800
    ),

    "corinne_hr": Client(
        id="corinne_hr",
        name="Corinne, responsable des ressources humaines chez Aspirabrooms - Le meilleur pour tous vos déplacements !",
        dialogue="Bonjour, je voudrais avoir une promotion cette année, il me faudrait un petit coup de pouce.",
        choices=[
            CHOICES["choice_corinne_hr.agile"],
            CHOICES["choice_corinne_hr.empowerment"],
            CHOICES["choice_corinne_hr.megapack"]
        ],
        level_required=10,
        patience=900
    ),

    "the_serious_researcher": Client(
        id="the_serious_researcher",
        name="Le Chercheur Sérieux",
        dialogue="Bonjour, j'écris une thèse sur la poisse et autres emmerdes, quels ouvrages me conseilleriez-vous pour approfondir mon sujet ?",
        choices=[
            CHOICES["choice_the_serious_researcher.murphys_laws"],
            CHOICES["choice_the_serious_researcher.knock_pinky_ass_worms"],
            CHOICES["choice_the_serious_researcher.pebble_in_shoe"]
        ],
        level_required=6,
        patience=800
    ),

    "the_feminist_witch": Client(
        id="the_feminist_witch",
        name="La sorcière féministe",
        dialogue="Bonjour, j'ai entendu que les nouvelles spécialités orientales étaient disponibles ?",
        choices=[
            CHOICES["choice_the_feminist_witch.sexy_djinns"],
            CHOICES["choice_the_feminist_witch.flatulences"],
            CHOICES["choice_the_feminist_witch.harissa"]
        ],
        level_required=7,
        patience=600
    ),

    "poltergeist": Client(
        id="poltergeist",
        name="Esprit frappeur",
        dialogue="Salutations. J'ai besoin de nouvelles idées pour emmerder les humains qui visitent mon château.",
        choices=[
            CHOICES["choice_poltergeist.tax_audit"],
            CHOICES["choice_poltergeist.knock_pinky_flatulences"],
            CHOICES["choice_poltergeist.banana_boat"]
        ],
        level_required=10,
        patience=600
    ),

}

# ========================================== VERIFIER OBJETS =======================================================

def has_items(witch, items):

    for item in items:

        shelf_quantity = witch.shop_shelves.get(item, {}).get("quantity", 0)
        stock_quantity = witch.shop_stock.get(item, {}).get("quantity", 0)

        if shelf_quantity + stock_quantity <= 0:
            return False

    return True


def remove_items(witch, items):

    for item in items:

        if witch.shop_shelves.get(item, {}).get("quantity", 0) > 0:
            witch.shop_shelves[item]["quantity"] -= 1

        elif witch.shop_stock.get(item, {}).get("quantity", 0) > 0:
            witch.shop_stock[item]["quantity"] -= 1


# ========================================== VERIFIER SI CLIENTS SONT POSSIBLES =======================================================

def check_client_event(witch, garden):

    # seulement les clients débloqués
    available_clients = [
        c for c in CLIENTS.values()
        if witch.level >= c.level_required
    ]

    if not available_clients:
        return

    # chance d'apparition
    if random.random() < 0.1:
        client(witch, garden)


# ========================================== FONCTION PPALE =======================================================

def client(witch, garden):

    available_clients = [
        client for client in CLIENTS.values()
        if witch.level >= client.level_required
    ]

    client = random.choice(available_clients)

    client.arrival_time = time.time()

    print("\n🔔 La clochette de la boutique tinte...\n")

    client.display()

    client.display_choices()


    while True:

        answer = input("\nVotre choix : ")

        if answer.isdigit():
            answer = int(answer)

        if 1 <= answer <= len(client.choices):
            break

        print("Choix invalide.")


    choice_index = answer - 1

    choice = client.choices[choice_index]


    if choice.items:

        if not has_items(witch, choice.items):

            print("Vous n'avez pas tous les objets nécessaires.")

            if client.patience > 0:
                
                witch.waiting_clients.append(WaitingClient(client, choice))

                print(f"{client.name} accepte d'attendre.")

            else:
                print(f"{client.name} repart déçu.")

            return


        remove_items(witch, choice.items)


    result_id = choice.result

    give_client_reward(witch, garden, result_id, choice.items)


# ========================================== RECOMPENSE =======================================================

def give_client_reward(witch, garden, result_id, sold_items):

    result = RESULTS[result_id]

    print(result.text)

    if result.title:
        print(result.title)

    register_sale(witch, sold_items)

    gain_rewards(witch, garden, result)

# ========================================== WAITING CLIENTS =======================================================

def display_waiting_clients(witch):

    print("\n=== CLIENTS EN ATTENTE ===")

    if not witch.waiting_clients:
        print("Personne n'attend.")

    for waiting in witch.waiting_clients:
        print(
            f"- {waiting.client.name}"
        )


def check_waiting_clients(witch):

    current_time = time.time()

    display_waiting_clients(witch)

    for waiting in witch.waiting_clients[:]:

        if current_time - waiting.arrival_time >= waiting.patience:

            print(f"{waiting.client.name} est reparti, un peu déçu.")

            witch.waiting_clients.remove(waiting)



def serve_waiting_clients(witch, garden, item_name):

    for waiting in witch.waiting_clients[:]:

        if not waiting.is_waiting_for(item_name):
            continue

        if not has_items(witch, waiting.choice.items):
            continue

        print(f"\n🔔 {waiting.client.name} revient récupérer sa commande !")

        remove_items(witch, waiting.choice.items)
        give_client_reward(witch, garden, waiting.choice.result, waiting.choice.items)

        witch.waiting_clients.remove(waiting)