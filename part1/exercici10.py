import os

ARXIU_LLISTA = "llista_compra.txt"

def carregar_crear_llista():
    if input("Vols carregar la última llista de la compra? [S/N]") == "S":
        try:
            with open(ARXIU_LLISTA, "r") as a:
                llista_compra = a.read().split("\n")
        except FileNotFoundError:
            input("No hi ha cap llista guardada!")
        os.system("cls")
        return (llista_compra)
    else:
        llista_compra = []
        return llista_compra



def exportar(export):
    with open(ARXIU_LLISTA, "w") as el_meu_arxiu:
        el_meu_arxiu.write("\n".join(export))


def afegir_nou(llista_compra):
    return(input("[Escriu Q per a sortir.]\n"
            "Introdueix el nom d'un producte:\n"))


def mostrar_llista(llista_compra):
    print("\n".join(llista_compra))

def guardar(llista_compra, item):
    if item.lower() in [a.lower() for a in llista_compra]:
        os.system("cls")
        input("Aquest producte ja està a la llista!")
        os.system("cls")
    else:
        llista_compra.append(item)

def main():
    os.system("cls")
    llista_compra = carregar_crear_llista()
    mostrar_llista(llista_compra)
    input_usuari = afegir_nou(llista_compra)
    os.system("cls")
    while input_usuari != "Q":
        guardar(llista_compra, input_usuari)
        mostrar_llista(llista_compra)
        input_usuari = afegir_nou(llista_compra)
        os.system("cls")
    if input("Vols guardar la llista? [S/N]") == "S":
        exportar(llista_compra)


if __name__ == "__main__":
    main()