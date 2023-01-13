import os

numeros = []
entrada = 0
numero_gran = numeros[0]
numero_petit = numeros[0]

while True:
    if entrada == "Q":
        os.system("cls")
        print("A REVEURE!")
        break
    elif type(entrada) != "class<float>" or type(entrada) != "class<int>":
        os.system("cls")
        entrada = input("{}"
                        "\nNúmero més gran:{}"
                        "\nNúmero més petit:{}"
                        "\n\n\nIntrodueix un número (Q per sortir):".format(numeros, numero_gran, numero_petit))
        numeros.append(entrada)
        for n in numeros[1:]:
            if numero_gran < n:
                numero_gran = n
            if numero_petit > n:
                numero_petit = n
        numero_petit = numeros[0]
        numero_gran = numeros[len(numeros) - 1]
    elif type(entrada) != "class<int>":
        print("Això no és un número!")