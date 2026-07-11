class Result:
     def __init__(
        self,
        text,
        title="",
        xp=0,
        money=0,
        items=None,
        recipes=None,
        achievements=None,
        unlocks=None
    ):

        self.text = text
        self.title = title
        self.xp = xp
        self.money = money
        self.items = items or []
        self.recipes = recipes or []
        self.achievements = achievements or []
        self.unlocks = unlocks or []


RESULTS = {

    # Gobelin fiscaliste
    "result_tax_specialist_goblin.tax_audit": Result(
        text="Le gobelin est ravi !",
        title="Récompense : 80 XP",
        xp=80
    ),

    "result_tax_specialist_goblin.tax_haven": Result(
        text="Le gobelin applaudit votre sens des affaires.",
        title="Récompense : 100 pièces.",
        money=100
    ),

    "result_tax_specialist_goblin.shop_closed": Result(
        text="Le gobelin repart vexé. Aucun gain."
    ),



    # Démon romantique
    "result_romantic_demon.bbl": Result(
        text="Le démon est aux anges : c'est en rupture de stock partout et sa belle en veut une désespérément !",
        title="Récompense : 150 XP et 100 pièces.",
        xp=150,
        money=100
    ),

    "result_romantic_demon.love_potion": Result(
        text="Le démon n'est pas convaincu par votre proposition : « Les succubes sont immunisées contre les philtres d'amour... »."
    ),

    "result_romantic_demon.bbl_love_potion": Result(
        text="Le démon est ravi, ses yeux s'attardent sur le flacon du Brazilian Butt Lift...",
        title="Récompense : 80 XP et 100 pièces.",
        xp=80,
        money=100
    ),



    # Sorcier gourmand
    "result_gourmet_wizard.cakes_and_politics": Result(
        text="Le sorcier s'exclame « Je ne l'avais pas celui ci ! »",
        title="Récompense : 80 XP et 80 pièces.",
        xp=80,
        money=80
    ),

    "result_gourmet_wizard.devils_breakfast": Result(
        text="Le sorcier s'exclame « Ca fait des années que je recherche un exemplaire de cet ouvrage ! »", 
        title="Récompense : 180 XP et 150 pièces.",
        xp=180,
        money=150
    ),

    "result_gourmet_wizard.top_chef": Result(
        text="Le sorcier s'exclame « Excellente suggestion ! » et part sans rien acheter. Vous vous sentez un peu bête."
    ),



    # Corinne Ressources Humaines
    "result_corinne_hr.agile": Result(
        text="Corinne feuillette l'ouvrage avec attention et ses yeux s'illuminent.",
        title="Récompense : 180 XP et 150 pièces.",
        xp=180,
        money=150
    ),

    "result_corinne_hr.empowerment": Result(
        text="Corinne voudrait quelque chose de plus... de moins... Elle reviendra."
    ),

    "result_corinne_hr.megapack": Result(
        text="Corinne regarde à gauche, à droite et derrière et vous chuchote « Ca peut s'arranger...»",
        title="🎁 Objet obtenu !",
        items=["broom_o_matik"]
    ),



    # Le chercheur sérieux
    "result_the_serious_researcher.murphys_laws": Result(
        text="Le Chercheur sérieux examine le livre. Il l'a déjà, évidemment. Il ira voir sur WizardZone."
    ),

    "result_the_serious_researcher.knock_pinky_ass_worms": Result(
        text="Le Chercheur sérieux vous donne un rouleau usé !",
        title="📜 Nouvelle recette !",
        recipes=["no_handy_no_candy"]
    ),

    "result_the_serious_researcher.pebble_in_shoe": Result(
        text="Le Chercheur sérieux pousse un gémissement de plaisir. Vous vous posez des questions sur les motivations derrière sa thèse... ",
        title="Récompense : 100 XP et 50 pièces.",
        xp=100,
        money=50,
    ),



    # La sorcière féministe
    "result_the_feminist_witch.sexy_djinns": Result(
        text="La sorcière féministe est ravie.",
        title="Récompense : 100 XP et 150 pièces",
        xp=100,
        money=150,
    ),

    "result_the_feminist_witch.flatulences": Result(
        text="La sorcière féministe a l'air très déçue. Elle repart sans rien acheter."
    ),

    "result_the_feminist_witch.harissa": Result(
        text="""La sorcière féministe vous remercie chaleureusement pour cette bonne adresse : elle ne venait pas pour ça """ 
             """mais elle adore la cuisine algérienne !""",
        title="📜 Nouvelle recette !",
        recipes=["harissa_revenge"]
    ),

}