from class_savemanager import SaveManager

# Création d'une nouvelle partie
player_team, inv, enemies = SaveManager.new_game()


# Modification volontaire pour tester la sauvegarde
player_team[1].level = 10


enemies[4].defeated = True

inv.append({
    "id": "mana_potion",
    "quantity": 3
})


# Sauvegarde
SaveManager.save(player_team, inv, enemies)


# Chargement
loaded_team, loaded_inv, loaded_enemies = SaveManager.load()


# Vérification
print(loaded_team)
print(loaded_enemies[4])
print(loaded_enemies[4].defeated)
print(loaded_inv)