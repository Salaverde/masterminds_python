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


def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)
    while any_player_pokemon_lives(player_profile):
        fight()
    print("Todos tus pokemon se han debilitado!\n Has sobrevivido {} combates.".format(player_profile["combats"]))

def any_player_pokemon_lives:


def fight():




if __name__ == "__main__":
    main()

