
resposta_invalida = "\nResposta no vàlida. {}"
compra = "\nCompra't {}."
OS = input("Benvingut a l'assistent per escollir model de telèfon."
                "\nPer ajudar-te t'hem de fer algunes preguntes."
                "\nTria el sistema operatiu:"
                "\n1. Android"
                "\n2. iOS\n")
if OS == "1":
    diners = input("Tens diners? (S/N)")
    if diners == "S":
        camara = input("T'importa tenir una bona càmera? (S/N)")
        if camara == "S":
            print (compra.format("Google Pixel"))
            exit()
        elif camara == "N":
            print (compra.format("el millor qualitat preu"))
            exit ()
        else:
            print(resposta_invalida.format("(S/N)"))
            exit ()
    elif diners == "N":
        print (compra.format("l'Android chino de 100€"))
        exit()
    else:
        print(resposta_invalida.format("(S/N)"))
        exit()

elif OS == "2":
    diners = input("Tens diners? (S/N)")
    if diners == "S":
            print(compra.format("l'Iphone Ultra Pro Max"))
            exit()
    elif diners == "N":
        print(compra.format("Un Iphone de segona mà"))
        exit()
    else:
        print(resposta_invalida.format("(S/N)"))
        exit()
else:
    print (resposta_invalida.format("(1/2)"))
    exit()