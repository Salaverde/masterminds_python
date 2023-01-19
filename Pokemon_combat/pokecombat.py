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


def fight(player_profile, enemy_pokemon):
    

def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)
    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(pokemon_list)
        fight(player_profile, enemy_pokemon)
    print("Todos tus pokemon se han debilitado!\n Has sobrevivido {} combates.".format(player_profile["combats"]))


if __name__ == "__main__":
    main()

