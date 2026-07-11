import random

SALE_DIALOGUES = [
    "La jolie sorcière repart ravie, laissant derrière elle les effluves d'un parfum agréable.",
    "Le centaure glisse quelques pièces sur le comptoir et récupère {item}.",
    "« Je reviendrai ! » promet le gobelin en rabattant son capuchon.",
    "Le cyclope récupère précautionneusement {item} et prend congé avec délicatesse.",
    "La transaction se déroule sans accroc.",
    "Une affaire rondement menée !",
    "Vous gagnez des thunes (ouais) 🎶 Vous êtes à l'aise financièrement... 🎵",
    "Le gnome vous félicite pour l'excellent rapport qualité-prix de {item}.",
    "L'elfe repart avec {item} et un grand sourire.",
    "L'enchanteur, satisfait, range {item} dans sa besace.",
    "Vous emballez soigneusement {item}.",
    "Vous ne vous plaignez pas (non) 🎶 Les affaires marchent en ce moment... 🎵",
    "La vieille voyante vous salue. Affaire conclue !",
    "La clochette tinte tandis que le démon s'en va avec un petit signe de la main.",
    "Le djinn vous fait un clin d'oeil et disparaît dans un nuage de fumée.",
    "L'esprit part en traversant joyeusement la porte en chêne.",
    "Une vente de plus ! Les affaires tournent bien.",
    "La dame blanche glisse {item} dans sa robe. « A bientôt... » souffle-t-elle.",
    "Le croquemitaine regarde {item} avec intensité. C'est tout à fait ce dont il avait besoin !",
    "Le chef de guilde est paré pour sa prochaine quête avec {item} !",
    "Le cavalier sans tête met {item} dans son heaume. Au moins il lui a trouvé une utilité...",
    "La goule se frotte les mains. {item} : c'est exactement ce qui lui fallait !",
    "Le druide emporte {item}, soulagé. Il a bien besoin de cet article pour le rassemblement du Corbeau !",
    "Le magicien prend son paquet avec empressement.",
    "La fée, souriante, récupère son sac de courses : « C'est bien pratique, les commerces de proximité ! »",

]

def random_sale_dialogue(item):
    text = random.choice(SALE_DIALOGUES)
    return text.format(item=item)