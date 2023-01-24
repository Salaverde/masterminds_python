import random
import os
import time
from pokeload import get_all_pokemons


def get_player_profile(pokemon_list):
    # Returns a dictionary with the player's profile after asking for its name and choosing random Pokemon from
    # pokefile.pkl.
    os.system("cls")
    return {
        "player_name": input("¿Cuál es tu nombre?\n"),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)],
        "combats": 0,
        "pokeballs": 5,
        "health_potion": 0
    }


def any_player_pokemon_lives(player_profile):
    # Returns a boolean value depending on wether the player has any living Pokemon in his inventory.
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0


def get_pokemon_info(pokemon):
    # Receives the data of a certain pokemon and returns a string with the relevant details for the player.
    return "{} | lvl {} | HP {} / {}".format(pokemon["name"], pokemon["level"], pokemon["current_health"],
                                             pokemon["base_health"])


def choose_pokemon(player_profile):
    # We ask the player to choose a Pokemon from his team.
    chosen_pokemon = None
    while not chosen_pokemon:
        print("Qué pokemon de tu equipo quieres que luche?")
        index = 1
        for pokemon in player_profile["pokemon_inventory"]:
            if pokemon["current_health"] == 0:
                player_profile["pokemon_inventory"].remove(pokemon)
        for pokemon in player_profile["pokemon_inventory"]:
            print(index, get_pokemon_info(pokemon))
            index += 1
        try:
            chosen_pokemon = player_profile["pokemon_inventory"][int(input()) - 1]
        except (ValueError, IndexError):
            print("Elección no vàlida. Intentalo de nuevo.")
    return chosen_pokemon


def choose_player_attack(player_pokemon, enemy_pokemon):
    # This will print all the available attacks to the player's fighting Pokemon based on its level and ask him to
    # choose one.
    choosen_attack = None
    os.system("cls")
    print(get_pokemon_info(player_pokemon))
    print(get_pokemon_info(enemy_pokemon))
    while not choosen_attack:
        index = 1
        available_attacks = []
        print("Que movimiento quieres que use {}?".format(player_pokemon["name"]))
        for attack in player_pokemon["attacks"]:
            if int(attack["min_level"]) <= player_pokemon["level"] != 0:
                print(index, attack["name"], attack["damage"])
                available_attacks.append(attack)
                index += 1
        try:
            choosen_attack = available_attacks[int(input()) - 1]
        except (ValueError, IndexError):
            print("Elección no vàlida. Intentalo de nuevo.")
    return choosen_attack


def choose_enemy_attack(enemy_pokemon):
    # Will return a random attack from the ones available to the enemy pokemon based on its level.
    available_enemy_attacks = []
    for attack in enemy_pokemon["attacks"]:
        if int(attack["min_level"]) <= enemy_pokemon["level"] != 0:
            available_enemy_attacks.append(attack)
    return available_enemy_attacks


def player_turn(player_pokemon, player_attack, enemy_pokemon):
    # Returns the damage of the player's attack to the enemy Pokemon after applying the corresponding
    # multiplier.
    damage = player_attack["damage"] * decide_type_effect(player_attack["type"], enemy_pokemon["type"])
    print("Tu {} ha usado {} y le ha inflingido {} de daño al {} enemigo.".format(player_pokemon["name"],
                                                                                  player_attack["name"],
                                                                                  damage,
                                                                                  enemy_pokemon["name"]))
    if decide_type_effect(player_attack["type"], enemy_pokemon["type"]) == 0.5:
        print("No es muy efectivo...")
    elif decide_type_effect(player_attack["type"], enemy_pokemon["type"]) == 1.25:
        print("Es muy efectivo!")
    enemy_pokemon["current_health"] -= damage
    if enemy_pokemon["current_health"] < 0:
        enemy_pokemon["current_health"] = 0
    return enemy_pokemon["current_health"]


def enemy_turn(player_pokemon, enemy_attack, enemy_pokemon):
    # Returns the damage of the enemy's attack to the player's fighting Pokemon after applying the corresponding
    # multiplier based on types.
    damage = enemy_attack["damage"] * decide_type_effect(enemy_attack["type"], player_pokemon["type"])
    print("\nEl {} enemigo ha usado {} y ha inflingido {} de daño a tu {}.".format(enemy_pokemon["name"],
                                                                                   enemy_attack["name"],
                                                                                   enemy_attack["damage"],
                                                                                   player_pokemon["name"]))
    if decide_type_effect(enemy_attack["type"], player_pokemon["type"]) == 0.5:
        print("No es muy efectivo...")
    elif decide_type_effect(enemy_attack["type"], player_pokemon["type"]) == 1.25:
        print("Es muy efectivo!")
    player_pokemon["current_health"] -= enemy_attack["damage"]
    if player_pokemon["current_health"] < 0:
        player_pokemon["current_health"] = 0
    return player_pokemon["current_health"]


def capture_pokemon(enemy_pokemon):
    # After using a pokeball, the player will have a chance to capture a pokemon based on its current health.
    captured = None
    capturing_prob = (enemy_pokemon["current_health"] / enemy_pokemon["base_health"]) * 100
    if capturing_prob < random.randint(1, 100):
        captured = True
    return captured


def decide_type_effect(attack_type, pokemon_type):
    # We determine if a certain attack is strong, normal or weak against a Pokemon based in both types. We return a
    # multiplier (1.25, 1 or 0.5) to apply to the final damage.
    weakness = {
        "normal": ["lucha"],
        "fuego": ["agua", "tierra", "roca"],
        "agua": ["planta", "electrico"],
        "planta": ["fuego", "hielo", "veneno", "volador", "bicho"],
        "electrico": ["tierra"],
        "hielo": ["fuego", "lucha", "roca", "acero"],
        "lucha": ["volador", "psiquico", "hada"],
        "veneno": ["tierra", "psiquico"],
        "tierra": ["agua", "planta", "hielo"],
        "volador": ["electrico", "hielo", "roca"],
        "psiquico": ["bicho", "fantasma", "siniestro"],
        "bicho": ["volador", "roca", "fuego"],
        "roca": ["agua", "planta", "lucha", "tierra", "acero"],
        "fantasma": ["fantasma", "siniestro"],
        "dragon": ["hielo", "dragon", "hada"],
        "siniestro": ["lucha", "bicho", "hada"],
        "acero": ["fuego", "lucha", "tierra"],
        "hada": ["veneno", "acero"]

    }
    try:
        if attack_type in weakness[pokemon_type[0]]:
            return 1.25
        elif pokemon_type in weakness[attack_type]:
            return 0.5
        else:
            return 1
    except KeyError:
        return 1


def assign_experience(attack_history):
    # We randomly assign 1 to 5 experience points to each pokemon that attacked during the last combat. A Pokemon
    # will level up every 20 exp points.
    for pokemon in attack_history:
        points = random.randint(1, 5)
        pokemon["current_exp"] += points

        while pokemon["current_exp"] > 20:
            pokemon["current_exp"] -= 20
            pokemon["level"] += 1
            pokemon["current_health"] = pokemon["base_health"]
            print("Tu pokemon ha subido de nivel".format(get_pokemon_info(pokemon)))


def fortune_loot():
    # We determine if the player gets an object after a fight and return a string containing the name of the object.
    fortune = random.randint(1, 3)
    if fortune == 1:
        return "potion"
    elif fortune == 2:
        return "pokeballs"
    else:
        return None


def fight(player_profile, enemy_pokemon):
    # We start every combat by printing the name of the enemy Pokemon and letting the player choose a Pokemon from his
    # team to combat.
    os.system("cls")
    print("Que empiece el combate número {}!\nTe vas a enfrentar a {}.".format(player_profile["combats"] + 1,
                                                                               enemy_pokemon["name"]))
    player_pokemon = choose_pokemon(player_profile)
    captured_pokemon = None
    attack_history = []

    # Unless the enemy pokemon is beaten or captured with a pokeball or player's team is defeated the fight will go on.
    while any_player_pokemon_lives(player_profile) and enemy_pokemon["current_health"] > 0 and not captured_pokemon:
        missed_turn = None
        action = None
    # Player can choose to attack, use a potion or a pokeball or change pokemon. In the latter case enemy pokemon will
    # attack anyway. The variable missed_turn is used to make sure the player doesn't loose his turn when trying to
    # use an object while not having any in his inventory.
        while action not in ["A", "P", "V", "C"]:
            os.system("cls")
            print(get_pokemon_info(player_pokemon))
            print(get_pokemon_info(enemy_pokemon))
            action = input("Qué quieres hacer? [A]tacar, usar una [P]okeball ({}), "
                           "usar una Poción de [V]ida ({}) o [C]ambiar de Pokemon?".format(player_profile["pokeballs"],
                                                                                           player_profile["health_potion"]))
            os.system("cls")
        if action == "A":
            player_attack = choose_player_attack(player_pokemon, enemy_pokemon)
            os.system("cls")
            enemy_pokemon["current_health"] = player_turn(player_pokemon, player_attack, enemy_pokemon)
            attack_history.append(player_pokemon)
        elif action == "P":
            if player_profile["pokeballs"] > 0:
                print("Usaste una pokeball.")
                if capture_pokemon(enemy_pokemon):
                    player_profile["pokemon_inventory"].append(enemy_pokemon)
                    print("{} capturado!".format(enemy_pokemon["name"]))
                    time.sleep(2)
                    captured_pokemon = True
                else:
                    print("Oh, no! El {} enemigo se ha escapado!".format(enemy_pokemon["name"]))
                    time.sleep(2)
                player_profile["pokeballs"] -= 1
            else:
                print("No tienes pokeballs!")
                missed_turn = True
        elif action == "V":
            if player_profile["health_potion"] > 0:
                player_pokemon["current_health"] += 50
                if player_pokemon["current_health"] > player_pokemon["base_health"]:
                    player_pokemon["current_health"] = player_pokemon["base_health"]
                print("{} Ha restaurado 50 PS.".format(enemy_pokemon["name"]))
            else:
                print("No tienes pociones de vida!")
                missed_turn = True
        elif action == "C":
            player_pokemon = choose_pokemon(player_profile)

        if player_pokemon["current_health"] > 0 and enemy_pokemon["current_health"] > 0 and not missed_turn and not captured_pokemon:
            enemy_attack = random.choice(choose_enemy_attack(enemy_pokemon))
            player_pokemon["current_health"] = enemy_turn(player_pokemon, enemy_attack, enemy_pokemon)
            time.sleep(3)

        if player_pokemon["current_health"] == 0 and any_player_pokemon_lives(player_profile):
            print("Tu {} se ha debilitado!".format(player_pokemon["name"]))
            player_pokemon = choose_pokemon(player_profile)

    if enemy_pokemon["current_health"] == 0:
        print("El {} enemigo se ha debilitado! Has ganado!".format(enemy_pokemon["name"]))
        assign_experience(attack_history)
        time.sleep(2)
    if not captured_pokemon:
        enemy_pokemon["current_health"] = enemy_pokemon["base_health"]


def main():
    # This function will initialize the game by collecting all Pokemons' data and creating a player's profile.
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)
    # We will make the player fight until all the Pokemons in his team are dead. When that happens we print a message
    # with the amount of combats he survived. After every combat we will randomly give a pokeball or a health potion.
    # Both player's team and enemy Pokemon are randomly choosen from pokefile.pkl.
    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(pokemon_list)
        fight(player_profile, enemy_pokemon)
        player_profile["combats"] += 1
        if fortune_loot() == "potion":
            player_profile["health_potion"] += 1
            print("Has recibido una poción de vida!")
        elif fortune_loot() == "pokeballs":
            player_profile["pokeballs"] += 1
            print("Has recibido una pokeball!")
    print("Todos tus pokemon se han debilitado!\nFelicidades, {}.\nHas sobrevivido {} combates.".format(player_profile["player_name"],
                                                                                                         player_profile["combats"]))


if __name__ == "__main__":
    main()

