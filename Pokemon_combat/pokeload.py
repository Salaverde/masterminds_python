import pickle
from requests_html import HTMLSession

pokemon_base = {
    "name": "",
    "base_health": 100,
    "current_health": 100,
    "level": 1,
    "type": None,
    "current_exp": 0
}
URL_BASE = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk="


def get_pokemon(index):
    url = "{}{}".format(URL_BASE, index)
    session = HTMLSession()

    new_pokemon = pokemon_base.copy()
    pokemon_page = session.get(url)

    new_pokemon["name"] = pokemon_page.html.find(".mini", first=True).text.split("\n",)[0]

    new_pokemon["type"] = []
    for img in pokemon_page.html.find(".pkmain", first=True).find(".bordeambos", first=True).find("img"):
        new_pokemon["type"].append(img.attrs["alt"])

    new_pokemon["attacks"] = []
    for attack_item in pokemon_page.html.find(".pkmain")[-1].find("tr .check3"):
        attack = {
            "name": attack_item.find("td", first=True).find("a", first=True).text,
            "type": attack_item.find("td")[1].find("img", first=True).attrs["alt"],
            "min_level": attack_item.find("th")[1].text,
            "damage": int(attack_item.find("td")[3].text.replace("--", "0"))
        }
        if attack["min_level"] == "":
            attack["min_level"] = 1
        attack["min_level"] = int(attack["min_level"])
        new_pokemon["attacks"].append(attack)

    return new_pokemon


def get_all_pokemons():
    try:
        print("Cargando lista de pokemons...")
        with open("pokefile.pkl", "rb") as pokefile:
            all_pokemons = pickle.load(pokefile)
    except FileNotFoundError:
        all_pokemons = []
        print("\nLista de pokemons no encontrada!\n Descargando de internet...")
        for index in range(151):
            all_pokemons.append(get_pokemon(index + 1))
            print("*", end="")
        with open("pokefile.pkl", "wb") as pokefile:
            pickle.dump(all_pokemons, pokefile)
    print("¡Lista de pokemons cargada!")
    return all_pokemons