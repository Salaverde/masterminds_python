import os

def llista(compra):
    os.system("cls")
    print(compra)
    nou_item = input("Introdueix un nou producte a la llista.\n")
    if nou_item in compra:
        input("Aquest producte ja és a la compra!")
        os.system("cls")
    else:
        compra.append(nou_item)
    llista(compra)
def main():
    llista(["Pa", "Ous", "Llet"])

if __name__ == "__main__":
    main()