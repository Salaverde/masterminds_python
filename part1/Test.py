input("Benvingut al test per veure si t'agrada el foramtge.\n Pren enter per a continuar.")
punts = 0
r1 = input("""\
    Pregunta 1-  Què fas quan veus una taula de formatges?
    A - Surto corrents.
    B - Provo una mica de formatge.
    C - M'els mengo tots.
    """)
if r1 == "A" :
    punts += 0
elif r1 == "B":
    punts += 5
elif r1 == "C":
    punts += 10
else:
    print("Les úniques resposter vàlides són A, B, o C.")
    exit()

if r2 == "A" :
    punts += 0
elif r2 == "B":
    punts += 5
elif r2 == "C":
    punts += 10
else:
    print("Les úniques resposter vàlides són A, B, o C.")
    exit()
r3 = input("""\
    Pregunta 2 - Ets intolerant a la lactosa?
    A - Si.
    B - De vegades.
    C - No.
    """)
if r2 == "A":
    punts += 0
elif r2 == "B":
    punts += 5
elif r2 == "C":
    punts += 10
else:
    print("Les úniques resposter vàlides són A, B, o C.")
    exit()

if punts < 15:
    print ("Odies el formatge.")
elif punts < 25:
        print("Toleres el formatge.")
elif punts >= 25:
        print("T'encanta el formatge.")