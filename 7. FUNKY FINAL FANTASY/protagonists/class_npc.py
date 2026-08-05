from quests.quests import start_quest

class NPC:

    def __init__(
        self,
        id,
        name,
        description,
        dialogues=None,
        quests=None, 
        zone=None
    ):
        self.id = id
        self.name = name
        self.description = description

        self.dialogues = dialogues or []
        self.quests = quests or []
        self.zone = zone


FOREST_NPCS = {

    "lia_young_seamstress": NPC(
        id="lia_young_seamstress",
        name="Lia l'apprentie couturière",
        description="Se spécialise actuellement en couture mystique et énergétique, option vibrations quantiques.",
        dialogues="« Mon examen est dans 10 jours... " \
        "\nJe ne peux plus aller récolter ce dont j'ai besoin dans la forêt pour réaliser mon chef d'oeuvre, "
        "\nc'est devenu trop dangereux... »"
        "\nSa voix se remplit soudainement d'espoir :"
        "\n« Si vous me rapportez ce dont j'ai besoin, je vous confectionnerai une belle pièce d'équipement ! »",
        quests=["the_seamstress"],
        zone="dark_forest"
    ),

    "the_twins": NPC(
        id="the_twins",
        name="Les jumeaux",
        description="Flippants, ces gosses.",
        dialogues="« 🎶 Black Phillip, Black Phillip "
        "\nUne couronne pousse sur sa tête, "
        "\nBlack Phillip, Black Phillip "
        "\nÀ la reine nounou est marié. "
        "\nSaute sur le poteau de la clôture, "
        "\nCourant dans l'écurie. "
        "\nBlack Phillip, Black Phillip "
        "\nRoi de tous. "
        "\nBlack Phillip, Black Phillip "
        "\nRoi du ciel et de la terre, "
        "\nBlack Phillip, Black Phillip "
        "\nRoi de la mer et du sable. "
        "\nNous sommes vos serviteurs, "
        "\nNous sommes vos hommes. "
        "\nBlack Phillip mange les lions "
        "\nDe la tanière des lions. 🎶 »",
        zone="dark_forest"
    ),


    "magda_the_fortune_teller": NPC(
        id="magda_the_fortune_teller",
        name="Magda la voyante",
        description="Elle a le troisième oeil.",
        dialogues="« Patrick ! C'est lui le loup-garou... Je suis pas folle hein ! Patriiiiiiiiiick !!!! »",
        zone="dark_forest"
    ),


    "matthew_the_priest": NPC(
        id="matthew_the_priest",
        name="Matthew le prêtre",
        description="Soutane grise, croix en bois, Bible à la main.",
        dialogues="« Bonjour mes enfants, je suis navré mais je suis très occupé en ce moment... "
        "\nNous vivons des temps étranges. »",
        zone="dark_forest"
    ),

    "rupaul_the_fool": NPC(
        id="rupaul_the_fool",
        name="Rupaul l'excentrique",
        description="Il a l'air complètement allumé.",
        dialogues="« Si tu mélanges des patates et des pommes tu obtiens des PATAPOMMES ! »"
        "\nIl vous attrape au collet en vous postillonnant dessus :"
        "\n« Faut pas bouffer les pommes de la forêt hein ? Tu jures ? C'pas bon ! »",
        zone="dark_forest"
    ),

    "frocque": NPC(
        id="frocque",
        name="Frocque",
        description="Il vous regarde intensément avec la bouche légèrement entrouverte.",
        dialogues="« Tatan, elle dit que pour savoir le temps qu'il va faire demain, il faut mettre son doigt dans le cul du coq. »",
        zone="dark_forest"
        ),

    "lady_lisse": NPC(
        id="lady_lisse",
        name="Dame Lisse",
        description="Sa robe travaillée et son port de tête montrent qu'elle est d'ascendance noble.",
        dialogues="« Mon mari m'a dit l'autre jour que la seule différence entre des briques et mes tartes c'est l'appellation... " \
        "\nIl m'a promis d'un ton moqueur que si je parvenais à lui cuisiner une tarte aux pommes comestible, "
        "\nil me fera cadeau d'une pomme d'or pur. »",
        quests=["the_apple_pie"],
        zone="dark_forest"
    ),

    "thomas_the_carpenter": NPC(
        id="thomas_the_carpenter",
        name="Thomas, le charpentier",
        description="Son pantalon est plein de sciure, ses cheveux aussi.",
        dialogues="« Il me manque du bois pour terminer la charpente de la grande salle du village. "
        "\nEn ces temps troublés, nous aurions bien besoin d'un endroit où nous réunir... »",
        quests=["help_build_the_community_hall"],
        zone="dark_forest"
    ),

    "merlin_the_alpha_drood": NPC(
        id="merlin_the_alpha_drood",
        name="Merlin, le druide alpha",
        description="Grand chapeau pointu, tournesols dans sa longue barbe.",
        dialogues="« Yo les frérots ! Ça dit quoi ? J'ai un date Tinder avec une go qui s'appelle Mélulu..."
        "\nJ'espère que c'est carré, ça fait longtemps que j'ai pas ken. »",
        zone="dark_forest"
    ),

    "sophy_the_midwife": NPC(
        id="sophy_the_midwife",
        name="Sophy, la sage-femme",
        description="Une dame respectable à l'air pincé.",
        dialogues="« Mes derniers accouchements ? Oulà... On est vraiment obligés d'en parler ?"
        "\nIl doit y avoir quelque chose dans l'eau, c'est la seule explication... »"
        "\nElle s'éloigne en soupirant.",
        zone="dark_forest"
    ),

    "gregoire_the_old_man": NPC(
        id="gregoire_the_old_man",
        name="Grégoire, le vieil homme",
        description="Il a l'air d'attendre quelque chose.",
        dialogues="« Pssst ! Hey ! Tu veux de la bonne ? »",
        zone="dark_forest"
    ),


    "the_purple_cat": NPC(
        id="the_purple_cat",
        name="Le chat violet",
        description="Il fait sa toilette consciencieusement.",
        dialogues="« On est tous fous ici... Si tu me comprends tu l'es aussi... »",
        zone="dark_forest"
    ),


    "mayor_paulson": NPC(
        id="mayor_paulson",
        name="Maire Paulson",
        description="Sa tenue est soignée mais il a l'air anxieux.",
        dialogues="« Un loup-garou tue l'un de nos villageois à chaque pleine lune... "
        "\nNous avons déjà brûlé les corps de Mary la boulangère, Enric le berger et le petit Ezra...  »"
        "\nIl met sa tête dans ses mains un instant, puis se reprend : "
        "\n« Si vous tuez ce monstre, vous aurez notre éternelle gratitude ! »",
        quests=["kill_the_werewolf"],
        zone="dark_forest"
    ),


    "catharine_baby_samuels_mother": NPC(
        id="catharine_baby_samuels_mother",
        name="Catharine, mère de Bébé Samuel",
        description="Elle est amaigrie et a l'air malade.",
        dialogues="« Mon fils... Samuel... Il a été enlevé par la force maléfique qui habite cette forêt maudite ! "
        "\nCe n'est qu'un bébé. Il ne mérite pas la damnation éternelle ! »"
        "\nSon visage est déformé par des sanglots irrépressibles : "
        "\n« Apportez-lui la lumière et la délivrance... »",
        quests=["free_baby_samuel"],
        zone="dark_forest"
    ),

    "cockhitch_keeper": NPC(
        id="cockhitch_keeper",
        name="Cockhitch le garde-chasse",
        description="Il observe la forêt d'un air soucieux.",
        dialogues="« Les corbeaux sont très agressifs depuis quelques temps... "
        "\nJe ne vois plus les autres oiseaux. Les corbeaux les attaquent. J'ai ramassé beaucoup de spécimens morts, ou à l'agonie. »"
        "\nIl fronce les sourcils : "
        "\n« Si vous me rameniez les cadavres de ces corbeaux, je pourrai peut-être déterminer l'origine du mal qui les ronge... »",
        quests=["raven_hunt"],
        zone="dark_forest"
    ),

    "ronald_farmer": NPC(
        id="ronald_farmer",
        name="Ronald le fermier",
        description="Il s'affaire autour de ses bêtes.",
        dialogues="« J'ai eu pas mal de pertes de bétail ces dernières semaines... "
        "\nJe retrouve mes bêtes mortes empoisonnées le matin, et couvertes de toiles collantes. "
        "\nÀ ce rythme nous n'aurons plus rien à manger cet hiver. »"
        "\nIl hoche la tête et pousse un soupir."
        "\n« Ces araignées ne nidifient pas si près du village d'habitude. Il faudrait les forcer à retourner là d'où elles viennent. »",
        quests=["spider_hunt"],
        zone="dark_forest"
    ),

}

def get_available_npcs(game, zone):

    available = []

    for npc in FOREST_NPCS.values():

        if npc.zone != zone.id:
            continue

        if npc.id in game.met_npcs:
            continue

        available.append(npc)

    return available


def talk_to_npc(game, npc):

    print("")
    print(npc.name)

    dialogue = npc.dialogues

    print(dialogue)

    for id in npc.quests:

        if id not in [
            quest.id for quest in game.active_quests + game.completed_quests
        ]:
            start_quest(game, id)