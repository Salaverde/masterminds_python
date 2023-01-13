euro_dolar = 1.04
dolar_euro = 0.96

lliura_euro = 1.14
euro_lliura = 0.88

ent = "-- Introdueix la quantitat en {}. --"
sor = "-- L'equivalent en {} és {}. --"

m = str(
    input(
        "Benvingut al conversor de lliures i dòlars a euros."
              "\nSiusplau, escull la conversió que vols fer:"
              "\n1. € --> $           3. € --> £"
              "\n2. $ --> €           4. £ --> €\n"
        )
    )
if m == "1":
    en = float(input(ent.format("euros")))
    print(
        sor.format("dòlars", en * euro_dolar)
    )
    exit ()
elif m == "2":
    en = float(input(ent.format("dòlars")))
    print(sor.format("euros", en * dolar_euro))
    exit ()
elif m == "3":
    en = float(
        input(en.format("euros"))
    )
    print(
        sor.format("lliures", en * euro_lliura)
    )
    exit ()

elif m == "4":
    en = float(
        input(ent.format("lliures"))
    )
    print(
        sor.format("euros", en * euro_lliura)
    )
    exit ()
else:
    print(
        "Número no vàlid (1-4)."
    )
    exit()

