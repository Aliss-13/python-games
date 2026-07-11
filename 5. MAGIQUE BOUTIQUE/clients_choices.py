class Choice:

    def __init__(self, text, result, items):
        self.text = text
        self.result = result
        self.items = items or []



CHOICES = {

    # Gobelin fiscaliste
    "choice_tax_specialist_goblin.tax_audit": Choice(
        text="Vendre Contrôle fiscal - pour prendre soin de la concurrence.",
        result="result_tax_specialist_goblin.tax_audit",
        items=["tax_audit"]
    ),

    "choice_tax_specialist_goblin.tax_haven": Choice(
        text="Vendre Paradis fiscal : de l'enfer au nirvana - une référence !",
        result="result_tax_specialist_goblin.tax_haven",
        items=["tax_haven_from_hell_to_hell_yeah"]
    ),

    "choice_tax_specialist_goblin.shop_closed": Choice(
        text="Répondre que la boutique est en inventaire.",
        result="result_tax_specialist_goblin.shop_closed",
        items=None
    ),



    # Démon romantique
    "choice_romantic_demon.bbl": Choice(
        text="Vendre Brazilian Butt Lift.",
        result="result_romantic_demon.bbl",
        items=["bbl"]
    ),

    "choice_romantic_demon.love_potion": Choice(
        text="Vendre Philtre d'amour - vous lui dites que son charme naturel "
            "devrait suffire *wink wink*. Vous finissez à 18h et vous le "
            "rembourserez si son achat ne fonctionne pas.",
        result="result_romantic_demon.love_potion",
        items=["love_potion"]
    ),

    "choice_romantic_demon.bbl_love_potion": Choice(
        text="Vendre les 2 avec une petite réduction - vous adorez les compliments.",
        result="result_romantic_demon.bbl_love_potion",
        items=["bbl", "love_potion"]
    ),



    # Sorcier gourmand
    "choice_gourmet_wizard.cakes_and_politics": Choice(
        text="Vendre Cakes et politique.",
        result="result_gourmet_wizard.cakes_and_politics",
        items=["cakes_and_politics"]
    ),

    "choice_gourmet_wizard.devils_breakfast": Choice(
        text="Vendre Les petits déj d'enfer du Diable.", 
        result="result_gourmet_wizard.devils_breakfast",
        items=["the_devils_best_breakfast_recipes"]
    ),

    "choice_gourmet_wizard.top_chef": Choice(
        text="Lui proposer de regarder l'intégrale de Top Chef - Edition sorcier.",
        result="result_gourmet_wizard.top_chef",
        items=None
    ),



    # Corinne Ressources Humaines
    "choice_corinne_hr.agile": Choice(
        text="Vendre La Méthode à Gilles.",
        result="result_corinne_hr.agile",
        items=["agile"]
    ),

    "choice_corinne_hr.empowerment": Choice(
        text="Vendre Empouvoirment.",
        result="result_corinne_hr.empowerment",
        items=["empowerment"]
    ),

    "choice_corinne_hr.megapack": Choice(
        text="Lui proposer de lui offrir La Méthode à Gilles, Empouvoirment et Optimisation des ressources humaines en "
            "échange d'une grosse cylindrée à vil prix.",
        result="result_corinne_hr.megapack",
        items=["agile", "empowerment", "hr_optimization"]
    ),



    # Le chercheur sérieux
    "choice_the_serious_researcher.murphys_laws": Choice(
        text="Vendre Les Lois de Murphy - La Bible incontestée !",
        result="result_the_serious_researcher.murphys_laws",
        items=["murphys_laws"]
    ),

    "choice_the_serious_researcher.knock_pinky_ass_worms": Choice(
        text="Vendre Pan le petit orteil et Gratte-cul. Dommage, vous ne savez pas encore réaliser le sortilège Pas de "
             "bras, pas de chocolat. Vous lui dites avec regret que ça aurait été l'alchimie parfaite avec votre Gratte-cul.",
        result="result_the_serious_researcher.knock_pinky_ass_worms",
        items=["knock_pinky", "ass_worms"]
    ),

    "choice_the_serious_researcher.pebble_in_shoe": Choice(
        text="Vendre le pack « Petit caillou dans chaussure & pélerinage à Saint Jacques de Compostelle - départ de Paris ». " 
             "A utiliser concomitamment.",
        result="result_the_serious_researcher.pebble_in_shoe",
        items=["pebble_in_shoe"]
    ),



    # La sorcière féministe
    "choice_the_feminist_witch.sexy_djinns": Choice(
        text="Vendre Djinns sexy et pentagrammes avec un sourire de connivence.",
        result="result_the_feminist_witch.sexy_djinns",
        items=["sexy_djinns_and_pentagrams"]
    ),

    "choice_the_feminist_witch.flatulences": Choice(
        text="Vendre Flatulences - la vengeance à la harissa c'est assez original, pourquoi pas... ",
        result="result_the_feminist_witch.flatulences",
        items=["flatulences"]
    ),

    "choice_the_feminist_witch.harissa": Choice(
        text="Lui dire avec un soupir que le traiteur algérien, c'est au 15 et pas au 15bis, ca arrive tout le temps.",
        result="result_the_feminist_witch.harissa",
        items=None
    ),
}