import random, os
from pokeload import get_all_pokemons


def get_player_profile(pokemon_list):
    return {
        "player_name": input("¿Cuál es tu nombre?\n"),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)],
        "combats": 0,
        "pokeballs": 0,
        "health_potion": 0
    }


def any_player_pokemon_lives(player_profile):
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0


def get_pokemon_info(pokemon):
    return "{} | lvl {} | HP {} / {}".format(pokemon["name"], pokemon["level"], pokemon["current_health"], pokemon["base_health"])


def choose_pokemon(player_profile):
    choosen_pokemon = None
    while not choosen_pokemon:
        print("Qué pokemon de tu equipo quieres que luche?")
        index = 1
        for pokemon in player_profile["pokemon_inventory"]:
            if pokemon["current_health"] == 0:
                player_profile["pokemon_inventory"].remove(pokemon)
            else:
                print(index, get_pokemon_info(pokemon))
                index += 1
        try:
            choosen_pokemon = player_profile["pokemon_inventory"][int(input()) - 1]
        except (ValueError, IndexError):
            print("Elección no vàlida. Intentalo de nuevo.")
    return choosen_pokemon


def choose_player_attack(player_pokemon, enemy_pokemon):
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
    available_enemy_attacks = []
    for attack in enemy_pokemon["attacks"]:
        if int(attack["min_level"]) >= enemy_pokemon["level"] != 0:
            available_enemy_attacks.append(attack)
    return available_enemy_attacks


def player_turn(player_pokemon, player_attack, enemy_pokemon):
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
    captured = None
    capturing_prob = (enemy_pokemon["current_health"] / enemy_pokemon["base_health"]) * 100
    if capturing_prob > random.randint(1, 100):
        captured = True
    return captured


def decide_type_effect(attack_type, pokemon_type):
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


def fortune_loot():
    fortune = random.randint(1, 5)
    if fortune == 1:
        return "potion"
    elif fortune == 2:
        return "pokeball"
    else:
        return None


def fight(player_profile, enemy_pokemon):
    print("Que empiece el combate número {}!\n\nTe vas a enfrentar a {}.".format(player_profile["combats"] + 1,
                                                                                 enemy_pokemon["name"]))
    player_pokemon = choose_pokemon(player_profile)
    captured_pokemon = None
    while any_player_pokemon_lives(player_profile) and enemy_pokemon["current_health"] > 0 and not captured_pokemon:
        missed_turn = None
        action = None
        while action not in ["A", "P", "V", "C"]:
            action = input("Qué quieres hacer? [A]tacar, usar una [P]okeball, usar una Poción de [V]ida o [C]ambiar de Pokemon?")
        if action == "A":
            player_attack = choose_player_attack(player_pokemon, enemy_pokemon)
            enemy_pokemon["current_health"] = player_turn(player_pokemon, player_attack, enemy_pokemon)
        elif action == "P":
            if player_profile["pokeballs"] > 0:
                print("Usaste una pokeball.")
                if capture_pokemon(enemy_pokemon):
                    player_profile["pokemon_inventory"].append(enemy_pokemon)
                    print("{} capturado!".format(enemy_pokemon["name"]))
                    captured_pokemon = True
                player_profile["pokeballs"] -= 1
            else:
                print("No tienes pokeballs!")
                missed_turn = True
        elif action == "V":
            if player_profile["health_potion"] > 0:
                player_pokemon["current_health"] += 50
                if player_pokemon["current_health"] > player_pokemon["base_health"]:
                    player_pokemon["current_health"] = player_pokemon["base_health"]
            else:
                print("No tienes pociones de vida!")
                missed_turn = True
        elif action == "C":
            player_pokemon = choose_pokemon(player_profile)

        if player_pokemon["current_health"] > 0 and enemy_pokemon["current_health"] > 0 and not missed_turn and not captured_pokemon:
            enemy_attack = random.choice(choose_enemy_attack(enemy_pokemon))
            player_pokemon["current_health"] = enemy_turn(player_pokemon, enemy_attack, enemy_pokemon)

        if player_pokemon["current_health"] == 0 and any_player_pokemon_lives(player_profile):
            print("Tu {} se ha debilitado!".format(player_pokemon["name"]))
            player_pokemon = choose_pokemon(player_profile)

    if enemy_pokemon["current_health"] == 0:
        print("El {} enemigo se ha debilitado! Has ganado!".format(enemy_pokemon["name"]))

    enemy_pokemon["current_health"] = enemy_pokemon["base_health"]


def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)

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
    print("Todos tus pokemon se han debilitado!\n Has sobrevivido {} combates.".format(player_profile["combats"]))


if __name__ == "__main__":
    main()

