import random

from pokeload import get_all_pokemons


def get_player_profile(pokemon_list):
    return {
        "player_name": input("¿Cuál es tu nombre?"),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)],
        "combats": 0,
        "pokeballs": 0,
        "health_potion": 0
    }


def any_player_pokemon_lives(player_profile):
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0


def choose_pokemon(player_profile):
    index = 1
    print("\nQué pokemon de tu equipo quieres que luche?")
    for pokemon in player_profile["pokemon_inventory"]:
        print(index, pokemon["name"])
        index += 1
    choosen_pokemon = player_profile["pokemon_inventory"][int(input()) - 1]
    return choosen_pokemon


def choose_player_attack(player_pokemon):
    index = 1
    for attack in player_pokemon["attacks"]:
        if int(attack["min_level"]) <= player_pokemon["level"] != 0:
            print(index, attack["name"])

    #return input()


def choose_enemy_attack(enemy_pokemon):
    for attack in enemy_pokemon["attacks"]:
        if int(attack["min_level"]) >= enemy_pokemon["level"]:
            return attack


def fight(player_profile, enemy_pokemon):
    print("Que empiece el combate!\n Te vas a enfrentar a {}.".format(enemy_pokemon["name"]))
    player_pokemon = choose_pokemon(player_profile)
    player_attack = choose_player_attack(player_pokemon)
    enemy_attack = random.choice(choose_enemy_attack(enemy_pokemon))


def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)
    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(pokemon_list)
        fight(player_profile, enemy_pokemon)
    print("Todos tus pokemon se han debilitado!\n Has sobrevivido {} combates.".format(player_profile["combats"]))


if __name__ == "__main__":
    main()

