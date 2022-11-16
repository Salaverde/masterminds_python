import readchar
import os
import random

POS_X = 0
POS_Y = 1

player_position = [1, 1]
pikachu_max_hp = 200
pikachu_hp = 350

enemy_distribution = []
pikachu_attacks = [["Placatge", 8], ["Onda Trueno", 11], ["Golpe cola", 5], ["Megarrayo", 14]]
enemy_details = [["Bernat", 80], ["Marc", 120], ["Carla", 90], ["Mireia", 110]]
bernat_attacks = [["Attack 1", 10], ["Attack 1", 13], ["Attack 3", 15], ["Attack 4", 11]]
marc_attacks = [["Attack 1", 11], ["Attack 2", 16], ["Attack 3", 8], ["Attack 4",12]]
carla_attacks = [["Attack 1", 10], ["Attack 2", 12], ["Attack 3", 9], ["Attack 4", 13]]
mireia_attacks = [["Attack 1", 15], ["Attack 2", 12], ["Attack 3", 5], ["Attack 4", 13]]


starting_enemies = 4
defeated_enemies = 0
end_game = False
combat = None

# MAP DESIGN
object_distribution = """\
###   #####    #####
##      ###  #######
###      #     #####
##   ##     ########
###         ########
######            ##
#        ###########
####   #############
####         #######
###  #####    ######
##    ####       ###
###          #######
#     ###     ######
###   ######    ####
####################\
"""

object_distribution = [list(row) for row in object_distribution.split("\n")]
MAP_WIDTH = len(object_distribution[0])
MAP_HEIGHT = len(object_distribution)

# DRAW ENEMIES
while len(enemy_distribution) < starting_enemies:

    new_enemy = [random.randint(1, MAP_WIDTH - 1), random.randint(1, MAP_HEIGHT - 1)]

    if new_enemy not in enemy_distribution and new_enemy != player_position and \
            object_distribution[new_enemy[POS_Y]][new_enemy[POS_X]] != "#":
        enemy_distribution.append(new_enemy)


# Main Loop
while not end_game and not combat:

    # DRAW MAP
    os.system("cls")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            enemy_in_cell = None

            # DRAW ENEMIES
            for enemy in enemy_distribution:
                if coordinate_y == enemy[POS_Y] and coordinate_x == enemy[POS_X]:
                    char_to_draw = "*"
                    enemy_in_cell = enemy
            # DRAW PLAYER
            if player_position[POS_Y] == coordinate_y and player_position[POS_X] == coordinate_x:
                char_to_draw = "0"
            # AN ENEMY IS CONFRONTED
                if enemy_in_cell:
                    combat = True
                    fighting_enemy = enemy_in_cell
            # DRAW OBSTACLE
            if object_distribution[coordinate_y][coordinate_x] == "#":
                char_to_draw = "#"
            print(" {} ".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    print("ENEMIES DEFEATED: {}".format(defeated_enemies))
    print("ENTER Q TO EXIT")
    if end_game:
        break
    if defeated_enemies == 4:
        break

    # Where does the player want to move?
    direction = readchar.readchar()
    new_position = None
    if direction == "w":
        new_position = [player_position[POS_X], (player_position[POS_Y] - 1) % MAP_HEIGHT]
        if object_distribution[new_position[POS_Y]][new_position[POS_X]] != "#":
            player_position = new_position

    elif direction == "s":
        new_position = [player_position[POS_X], (player_position[POS_Y] + 1) % MAP_HEIGHT]
        if object_distribution[new_position[POS_Y]][new_position[POS_X]] != "#":
            player_position = new_position


    elif direction == "a":
        new_position = [(player_position[POS_X] -1) % MAP_WIDTH, player_position[POS_Y]]
        if object_distribution[new_position[POS_Y]][new_position[POS_X]] != "#":
            player_position = new_position


    elif direction == "d":
        new_position = [(player_position[POS_X] + 1) % MAP_WIDTH, player_position[POS_Y]]
        if object_distribution[new_position[POS_Y]][new_position[POS_X]] != "#":
            player_position = new_position


    elif direction == "q":
        end_game = True

    while combat == True and end_game == False:
        os.system("cls")
        current_enemy = enemy_details[defeated_enemies]
        enemy_hp = int(current_enemy[1])
        enemy_hp_bars = int(enemy_hp // 10)
        pikachu_hp_bars = int(pikachu_hp // 10)
        pikachu_action = 0
        pikachu_paction = ["1", "2", "3", "4", 1, 2, 3, 4]
        enemy_action = []
        if enemy_hp <= 0:
            enemy_hp = 0
            enemy_distribution.remove(fighting_enemy)
            defeated_enemies += 1
            combat = False
            break
        if pikachu_hp <= 0:
            pikachu_hp = 0
            end_game = True
            break
        print("You have to fight {}".format(current_enemy[0]))
        while pikachu_action not in pikachu_paction:
            os.system("cls")
            print ("You are in a fight against {}".format(current_enemy[0]))
            pikachu_action = input(""
            "\nYour HP:  [{}] ({})"
            "\n{}'s HP: [{}] ({})"
            "\nWhat attack do you want your Pikachu to use?"
            "\n1. Placatge"
            "\n2. Onda trueno"
            "\n3. Golpe cola"
            "\n4. Megarrayo\n"
            .format(("#" * pikachu_hp_bars) + " " * (10 - pikachu_hp_bars), pikachu_hp,
            current_enemy[0], "#" * enemy_hp_bars + " " * (10 - enemy_hp_bars), current_enemy [1]))
            enemy_attack = (random.randint(1,4))
            if current_enemy[0] == "Bernat":
                current_attack = bernat_attacks[enemy_attack - 1]
            elif current_enemy[0] == "Marc":
                current_attack = marc_attacks[enemy_attack - 1]
            elif current_enemy[0] == "Carla":
                current_attack = carla_attacks[enemy_attack - 1]
            elif current_enemy[0] == "Mireia":
                current_attack = mireia_attacks[enemy_attack - 1]


    #PLAYER TURN
        pikachu_action = int(pikachu_action)
        print("Your Pikachu uses {}, which deals {} damageto the enemy {}."
            .format(pikachu_attacks[pikachu_action - 1][0],
            pikachu_attacks[pikachu_action - 1][1],
            current_enemy[0]))
        current_enemy[1] = current_enemy[1] - pikachu_attacks[pikachu_action - 1][1]
    #ENEMY TURN
        input("Enemy {} uses {}, which deals {} damage to your Pikachu.\n"
            .format(current_enemy[0], current_attack[0], current_attack[1]))
        pikachu_hp = pikachu_hp - current_attack[1]


os.system("cls")
if end_game == True:
    print("YOU DIED!")
    input("\nYOU DEFEATED {} ENEMIES.".format(defeated_enemies))
if defeated_enemies == 4:
    print("YOU HAVE DEFEATED ALL THE ENEMIES!!")
    print("""                                               .--.
                                               `.  \ 
                                                 \  \ 
                                                  .  \ 
                                                  :   .
                                                  |    .
                                                  |    :
                                                  |    |
  ..._  ___                                       |    |
 `."".`''''""--..___                              |    |
 ,-\  \             ""-...__         _____________/    |
 / ` " '                    `""""""""                  .
 \                                                      L
 (>                                                      \ 
/                                                         \ 
\_    ___..---.                                            L
  `--'         '.                                           \ 
                 .                                           \_
                _/`.                                           `.._
             .'     -.                                             `.
            /     __.-Y     /''''''-...___,...--------.._            |
           /   _."    |    /                ' .      \   '---..._    |
          /   /      /    /                _,. '    ,/           |   |
          \_,'     _.'   /              /''     _,-'            _|   |
                  '     /               `-----''               /     |
                  `...-'                                       `...-'""")
os.system("cls")
