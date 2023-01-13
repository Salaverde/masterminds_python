
print ("Ves a la cuina i obre la nevera.")
llet = input("Hi ha llet? (S/N)")
colacao = input("Hi ha colacao? (S/N)")
if colacao == "S" and llet == "S":
    print("Agafa un got, tira la llet i el colacao i remena.\n Bon profit! ;)")
elif llet == "N" and colacao == "N":
    print ("Apunta a la nevera que cal comprar llet i colacao.")
elif llet == "S" and colacao == "N":
    print("Apunta a la nevera que cal comprar colacao.")
elif llet == "N" and colacao == "S":
    print("Apunta a la nevera que cal comprar llet.")