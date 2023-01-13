frase = input("Introdueix un text:")
vocals = ["a", "e", "i", "o", "u"]
vocals_trobades = 0
for lletra in frase:
    if lletra in vocals:
        vocals_trobades += 1
        print(lletra)
print("Hi ha {} vocals.".format(vocals_trobades))

