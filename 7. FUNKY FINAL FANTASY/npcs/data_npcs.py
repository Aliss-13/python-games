from npcs.class_npc import NPC


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
        zone="dark_forest",


        dialogue_states={
            "the_seamstress": {
                "name": "Lia la couturière",
                "description": "Spécialiste couture mystique et énergétique.",
                "dialogues": "« Ma boutique a énormément de succès depuis que j'ai réussi mon examen ! "
                "\nJe reçois des enchanteurs, druides et énergéticiens du pays entier ! "
                "\nVous serez toujours les bienvenus ici et je vous ferai les meilleurs prix sur toutes mes pièces ! »"
                "\nElle vous fait un sourire radieux.",
                "unlock_shop": "magic_seamstress"
            }
        }
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
        zone="dark_forest",

        dialogue_states={
            "black_phillip": {
                "name": "the_twins",
                "description": "Ils discutent ensemble. Le petit garçon sourit à sa sœur.",
                "dialogues": "« Viens, je vais te montrer comment construire une cabane. "
	            "\n-C'est vrai Ben ? Trop chouette ! "
	            "\n-Mais oui, c'est facile ! Tu seras le charpentier et moi je monterai les murs. "
	            "\n-Je pourrai emmener ma poupée ? "
	            "\n-Bien sûr ! Elle supervisera le chantier ! »"
            }
        }
    ),


    "magda_the_fortune_teller": NPC(
        id="magda_the_fortune_teller",
        name="Magda la voyante",
        description="Elle a le troisième oeil.",
        dialogues="« Enrick ! C'est lui le loup-garou... Je suis pas folle hein ! Pas Ezra ! Enriiiiiiiiiick !!!! »",
        zone="dark_forest",

        dialogue_states={
            "kill_the_werewolf": {
                "description": "Elle a le troisième œil, mais aussi une couronne de fleurs sur la tête",
                "dialogues": "« Depuis que mon mari Enrick est parti avec cette femme prétentieuse, mes énergies se sont transformées... » "
 	            "\nElle se penche vers vous et vous chuchote : "
	            "\n« J'ai trouvé l'amour ! La barbe et le chapeau pointu, c'est magnétique ! »"
            }
        }
    ),


    "matthew_the_priest": NPC(
        id="matthew_the_priest",
        name="Matthew le prêtre",
        description="Soutane grise, croix en bois, Bible à la main.",
        dialogues="« Bonjour mes enfants, je suis navré mais je suis très occupé en ce moment... "
        "\nNous vivons des temps étranges. »",
        zone="dark_forest",

        dialogue_states={
            "the_vvitch": {
                "dialogues": "« Bonjour mes enfants, quelle magnifique journée ! Que la forêt sent bon ! "
                "\nLes oiseaux chantent... Je n'avais pas ressenti une telle sérénité depuis des mois. »"
            }
        }
    ),

    "rupaul_the_fool": NPC(
        id="rupaul_the_fool",
        name="Rupaul l'excentrique",
        description="Il a l'air complètement allumé.",
        dialogues="« Si t'y mélanges deul' patates et deul' pommes t'y gagnes des PATAPOMMES ! »"
        "\nIl vous attrape au collet en vous postillonnant dessus :"
        "\n« Faut t'y pas bouffer eul' pommes d'la forêt hein ? T'y jures ? C'pas bon ! »",
        zone="dark_forest",

        dialogue_states={
            "the_apple_pie": {
                "description": "Il a l'air complètement hagard.",
                "dialogues": "« J't'y avais prév'nu pour eul' pommes ! Maint'nant gentil Sire l'est parti pour toujours. "
	            "\nTout ça t'cause d'sa sournoise ! Qui qu'va s'occuper d'Rupaul maint'nant ? »"
            }
        }
    ),

    "frocque": NPC(
        id="frocque",
        name="Frocque",
        description="Il vous regarde intensément avec la bouche légèrement entrouverte.",
        dialogues="« Tatan, elle dit que pour savoir le temps qu'il va faire demain, il faut mettre son doigt dans le cul du coq. »",
        zone="dark_forest",

        dialogue_states={
            "black_phillip": {"dialogues": "« Tatan, elle fait des flans ! »"}
        }
    ),

    "lady_lisse": NPC(
        id="lady_lisse",
        name="Dame Lisse",
        description="Sa robe travaillée et son port de tête montrent qu'elle est d'ascendance noble.",
        dialogues="« Mon mari m'a dit l'autre jour que la seule différence entre des briques et mes tartes c'est l'appellation... " \
        "\nIl m'a promis d'un ton moqueur que si je parvenais à lui cuisiner une tarte aux pommes comestible, "
        "\nil me fera cadeau d'une pomme d'or pur. »",
        quests=["the_apple_pie"],
        zone="dark_forest",

        dialogue_states={
            "the_apple_pie": {
                "dialogues": "« Mon mari a adoré ma tarte ! Dommage qu'il n'ait pas eu le temps de la finir...»"
            }
        }
    ),

    "thomas_the_carpenter": NPC(
        id="thomas_the_carpenter",
        name="Thomas, le charpentier",
        description="Son pantalon est plein de sciure, ses cheveux aussi.",
        dialogues="« Il me manque du bois pour terminer la charpente de la grande salle du village. "
        "\nEn ces temps troublés, nous aurions bien besoin d'un endroit où nous réunir... »",
        quests=["help_build_the_community_hall"],
        zone="dark_forest",

        dialogue_states={
            "help_build_the_community_hall": {
                "dialogues": "« Merci infiniment pour votre aide, cette salle a redonné un cœur au village  !"
                "\nJe n'attends qu'une chose à présent, c'est que les mauvaises ondes quittent notre belle forêt... »"
            }
        }
    ),

    "melin_the_alpha_drood": NPC(
        id="melin_the_alpha_drood",
        name="Melin, le druide alpha",
        description="Grand chapeau pointu, tournesols dans sa longue barbe.",
        dialogues="« Yo les frérots ! Ça dit quoi ? J'ai un date Tinder avec une go qui s'appelle Mélulu..."
        "\nJ'espère que c'est carré, ça fait longtemps que j'ai pas ken. »",
        zone="dark_forest",

        dialogue_states={
            "kill_the_werewolf": {
                "dialogues": "« Bon les gonzes... Mélulu était délulu, j'ai swipe left. "
	            "\nMais j'ai rencontré une go avec une aura... super chill, un max de flow, rizz de fou. "
                "\nOn va faire une commu flower power. Madga, mon O2 ! »"
            }
        }
    ),

    "sophy_the_midwife": NPC(
        id="sophy_the_midwife",
        name="Sophy, la sage-femme",
        description="Une dame rondelette à l'air pincé.",
        dialogues="« Mes derniers accouchements ? Oulà... On est vraiment obligés d'en parler ?"
        "\nIl doit y avoir quelque chose dans l'eau, c'est la seule explication... »"
        "\nElle s'éloigne en soupirant.",
        zone="dark_forest",

        dialogue_states={
            "forest_mysteries": {
                "description": "Une dame rondelette à l'air jovial.",
                "dialogues": "« La forêt est à nouveau féconde ! Avec la bénédiction de Gaïa, nous allons avoir plein de beaux bébés. »"
            }
        }
    ),

    "gregoire_the_old_man": NPC(
        id="gregoire_the_old_man",
        name="Grégoire, le vieil homme",
        description="Il a l'air d'attendre quelque chose.",
        dialogues="« Pssst ! Hey ! Tu veux de la bonne ? »",
        zone="dark_forest",

        dialogue_states={
            "forest_mysteries": {
                "dialogues": "« Sophy m'a acheté tout mon stock, elle crée un nouveau remède pour soulager les douleurs. "
	            "\nBon ben c'est pas tout ça les jeunes, mais moi j'ai une récolte à faire... Repassez demain ! »"
	            "\nIl vous fait un clin d'oeil complice."
            }
        }
    ),


    "the_purple_cat": NPC(
        id="the_purple_cat",
        name="Le chat violet",
        description="Il fait sa toilette consciencieusement.",
        dialogues="« On est tous fous ici... Si tu me comprends tu l'es aussi... »",
        zone="dark_forest",

        dialogue_states={
            "the_vvitch": {
                "description": "Il fait la sieste au soleil.",
                "dialogues": "« Ronron, ronron… »"
            }
        }
    ),


    "mayor_paulson": NPC(
        id="mayor_paulson",
        name="Maire Paulson",
        description="Sa tenue est soignée mais il a l'air anxieux.",
        dialogues="« Un loup-garou tue l'un de nos villageois à chaque pleine lune... "
        "\nNous avons déjà brûlé les corps de Mary la boulangère, Jeremiah le berger et le petit Ezra...  »"
        "\nIl met sa tête dans ses mains un instant, puis se reprend : "
        "\n« Si vous tuez ce monstre, vous aurez notre éternelle gratitude ! »",
        quests=["kill_the_werewolf"],
        zone="dark_forest",

        dialogue_states={
            "kill_the_werewolf": {
                "description": "Il a rajeuni de dix ans.",
                "dialogues": "« Notre village vous sera éternellement reconnaissant. Nous allons enfin pouvoir reconstruire ! »"
            }
        }
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
        zone="dark_forest",

        dialogue_states={
            "free_baby_samuel": {
                "description": "L'épitaphe sur sa tombe dit : « Une femme et mère extraordinaire. »",
                "dialogues": "« Catharine a rejoint Samuel et Ezra dans la lumière. Ils sont enfin en paix. »"
            }
        }
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
        zone="dark_forest",

        dialogue_states={
            "the_vvitch": {
                "description": "Il contemple la forêt avec fierté.",
                "dialogues": "« La corruption est partie ! Les oiseaux sont revenus... C'est un jour heureux ! »",
            }
        }
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
        zone="dark_forest",

        dialogue_states={
            "the_vvitch": {
                "dialogues": "« Les animaux sont redevenus fertiles ! Je n'ai pas revu de traces d'araignées géantes. "
                "\nQuel soulagement ! Les troupeaux vont pouvoir s'agrandir. »",
            }
        }
    ),

}
