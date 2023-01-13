import random
r1 = input(
    "Et despertes en una habitació, estirat al llit."
    "\nEstàs desorientat i et mareges a l'aixecar-te."
    "\nMires al teu voltant i veus una finestra i una porta."
    "\nLa porta està tancada amb clau."
    "\nQuè vols fer?"
    "\nA. Mirar per la finestra."
    "\nB. Mirar sota el llit.\n")
if r1 == "A":
     print("Obres la finestra i treus el cap."
           "\nNotes un moviment darrera teu i de sobte estàs en caiguda llire."
           "\nUna caiguda lliure de més de 70 metres t'esclafa contra el terra."
           "\nESTÀS MORT!")
     exit()
elif r1 == "B":
    print ("Mires sota el llit. Veus que hi ha una clau al terra."
           "\nL'agafes i te la guardes a la butxaca.")
else:
    print ("No has respost correctament. HAS PERDUT!")
    exit()
r2 = input("Què vols fer?"
         "\nA. Mirar per la finestra."
         "\nB. Obrir la porta amb la clau.\n")
if r2 == "A":
    print("Obres la finestra i treus el cap."
          "\nNotes un moviment darrera teu i de sobte estàs en caiguda llire."
          "\nUna caiguda lliure de més de 70 metres t'esclafa contra el terra."
          "\nESTÀS MORT!")
    exit()
elif r2 == "B":
    r3 = input("Obres la porta i et trobes en un passadís."
               "\nVols anar cap a l'esquerra o cap la dreta?"
               "\nA. Esquerra"
               "\nB. Dreta\n")
    if r3 == "A":
        basto_agafatstr = input("Veus un bastó arrepejat en una cantonada. Vols agafar-lo? S/N)")
        if basto_agafatstr == "S":
            basto_agafat = True
        elif basto_agafatstr == "N":
            basto_agafat = False
        else:
            print("No has respost correctament. HAS PERDUT!")
            exit()
        nr = random.randint (1, 100)
        print ("De sobte tot es cobrex de fum i et desorientes."
               "\nComences a tossir i de sobte veus alguna cosa que brilla entre el fum."
               "\nT'hi acostes i veus una mena de geni."
               "\nEt diu que et pot desvelar si la fortuna et somriurà o no.")
        resposta = int(input("\n Per a saber-ho, et demana que li diguis quin número obtens al fer la següen operació:"
                         "\n 12 * {}\n".format (nr)))
        if resposta == 12 * nr:
            print ("El geni es rasca el cap. Sembla sorprès. Et diu que la fortuna et somriurà i et deixa passar.")
        else:
            print("El geni es posa seriós. Diu que la fortuna se t'ha firat en contra."
                  "\nFa petar els dits i et converteix en una granota."
                  "\nHAS PERDUT!")
            exit()
        print("Seguiu el passadís fins a una sala enorme."
              "\nDe sobte, sents una veu que ve del fons de la sala."
              "\nVEU GREU:Qui gosa venir a enfrontar-se a mi al meu propi palau?"
              "\nTot seguit, veus una figura vermella lliscar àgilment en la teva direcció"
              "\nMentre s'acosta li mires la cara. "
              "\nTé la cara vermella, amb banyes, uns ulls grocs brillants i una cua ben llarga."
              "\nEl dimoni en persona!")
        if basto_agafat:
            print("\nEs llença cap a tu, però tu li pegues un cop de bastó."
                  "\nEs desequilibra i tu aprofites per fugir."
                  "\nHAS ESCAPAT AMB ÈXIT!")
        else:
            print("Abans que puguis fer-hi res ve cap a tu i t'arrenca el cor com si res."
                  "\nESTÀS MORTª")
            exit()
    elif r3 == "B":
        numero_random_follet = bool(random.getrandbits(1)) #La resposta és indiferent, es decideix aleatòriament.
        print ("Segueixer el passadís cap a l'esquerra."
               "\nAssegut en una cadira al mig del passadís hi ha un follet força petit però armat fins les dents."
               "\nEt pregunta si ets partidari de la casa Borbó o la dels Àustria."
               "\nLa veritat és que no tens ni idea de què parla, però no sembla bona idea ignorar-lo.")
        r4 = input("Què li dius?"
                   "\nA. Borbó."
                   "\nB. Àustria.\n")
        if numero_random_follet:
            print("De sobte el seu posat canvia."
                  "\nEt somriu i s'ofereix a acompanyar-te cap a la sortida."
                  "\nNo saps com dir-li que no i acceptes.")
            print("Seguiu el passadís fins a una sala enorme."
                  "\nDe sobte, sents una veu que ve del fons de la sala."
                  "\nVEU GREU:Qui gosa venir a enfrontar-se a mi al meu propi palau?"
                  "\nTot seguit, veus una figura vermella lliscar àgilment en la teva direcció"
                  "\nMentre s'acosta li mires la cara. "
                  "\nTé la cara vermella, amb banyes, uns ulls grocs brillants i una cua ben llarga."
                  "\nEl dimoni en persona!"
                  "\nEs llença cap a tu, però el follet s'interporsa entre vosaltres. Comencen a lluitar i aprofites per fugir."
                  "\nHAS ESCAPAT AMB ÈXIT!")
            exit()
        elif not numero_random_follet:
            print("En sentir la teva resposta, el follet es comença a posar vermell i et salta al damunt."
                  "\nEt cus a ganivetades sense que puguis defensar-te i caus al terra mort."
                  "\nHAS MORT!")
        else:
            print("No has respost correctament. HAS PERDUT!")
            exit()

    else:
        print("No has respost correctament. HAS PERDUT!")
        exit()
else:
    print ("No has respost correctament. HAS PERDUT!")
    exit()