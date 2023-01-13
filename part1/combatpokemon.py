import random
import os

VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90
vida_pikachu = 80
vida_squirtle = 90

while vida_squirtle > 0 and vida_pikachu > 0:
    # Es desenvolupa el combat.

    # Torn de pikachu
    print("Torn de pikachu.\n")
    atac_pikachu = random.randint(1, 2)
    if atac_pikachu == 1:
        natac_pikachu = "bola voltio"
        perdua_vida_squirtle = 10
    elif atac_pikachu == 2:
        natac_pikachu = "onda trueno"
        perdua_vida_squirtle = 11
    print("El Pikachu fa servir {} i perds {} de vida.".format(natac_pikachu, perdua_vida_squirtle))
    vida_squirtle = vida_squirtle - perdua_vida_squirtle
    if vida_squirtle < 0:
        vida_squirtle = 0
    if vida_pikachu < 0:
        vida_pikachu = 0
    barres_vida_squirtle = int((vida_squirtle * 10 ) // VIDA_INICIAL_SQUIRTLE)
    barres_vida_pikachu = int((vida_pikachu * 10 ) // VIDA_INICIAL_PIKACHU)
    print("SQUIRTLE: [{}] ({}/{})\nPIKACHU: [{}] ({}/{})".format("#" * barres_vida_squirtle + " " * (10 - barres_vida_squirtle) , vida_squirtle,VIDA_INICIAL_SQUIRTLE,
    "#" * barres_vida_pikachu + " " * (10 - barres_vida_pikachu), vida_pikachu, VIDA_INICIAL_PIKACHU))
    print("El Pikachu fa servir {} i perds {} de vida.".format(natac_pikachu, perdua_vida_squirtle))
    # Torn d'Squirtle
    atac_squirtle = None
    while atac_squirtle != "1" and atac_squirtle != "2" and atac_squirtle != "3" and atac_squirtle != "4":
        barres_vida_squirtle = int((vida_squirtle * 10) // VIDA_INICIAL_SQUIRTLE)
        barres_vida_pikachu = int((vida_pikachu * 10) // VIDA_INICIAL_PIKACHU)
        print("SQUIRTLE: [{}] ({}/{})\nPIKACHU: [{}] ({}/{})".format(
            "#" * barres_vida_squirtle + " " * (10 - barres_vida_squirtle), vida_squirtle, VIDA_INICIAL_SQUIRTLE,
            "#" * barres_vida_pikachu + " " * (10 - barres_vida_pikachu), vida_pikachu, VIDA_INICIAL_PIKACHU))
        atac_squirtle = input("Quin atac vols que fagi el teu squirtle?"
                          "\n 1. Placatge."
                          "\n 2. Pistola aigua."
                          "\n 3. Bombolla."
                          "\n 4. No fer res.\n")
        os.system("cls")
        if atac_squirtle == "1":
            natac_squirtle = "Placatge"
            perdua_vida_pikachu = 10
        elif atac_squirtle == "2":
            natac_squirtle = "Pistola aigua"
            perdua_vida_pikachu =12
        elif atac_squirtle == "3":
            natac_squirtle = "Bombolla"
            perdua_vida_pikachu = 9
    if vida_squirtle < 0:
        vida_squirtle = 0
    if vida_pikachu < 0:
        vida_pikachu = 0
    if atac_squirtle == "4":
        input("Passes el torn...")
        os.system("cls")
    else:
        print("L'Squirtle fa servir {} i el Pikachu enemic perd {} de vida.".format(natac_squirtle, perdua_vida_pikachu))
    vida_pikachu = vida_pikachu - perdua_vida_pikachu
    input("Prem enter per a continuar...\n\n")
    os.system("cls")
print ("El combat s'ha acabat.")
if vida_squirtle > 0:
    print ("Has guanyat el combat!")
else:
    print("Mala sort, ha guanyat el pikachu!")
