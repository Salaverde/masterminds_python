import PySimpleGUI as sg

button_size = (7, 3)
PLAYER_ONE = "X"
PLAYER_TWO = "O"
deck = [0, 0, 0,
        0, 0, 0,
        0, 0, 0]
winning_plays = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
current_player = PLAYER_ONE
layout = [[
            sg.Button("", key="-0-", size=button_size),
            sg.Button("", key="-1-", size=button_size),
            sg.Button("", key="-2-", size=button_size)],
          [
            sg.Button("", key="-3-", size=button_size),
            sg.Button("", key="-4-", size=button_size),
            sg.Button("", key="-5-", size=button_size)],
          [
            sg.Button("", key="-6-", size=button_size),
            sg.Button("", key="-7-", size=button_size),
            sg.Button("", key="-8-", size=button_size)],
          [sg.Button("Reiniciar", key="-R-", size=(7, 2))]

          ]

window = sg.Window("Demo", layout)
game_end = False


def main(game_end, current_player):
    current_player = PLAYER_ONE
    while not game_end:

        event = window.read()[0]

        if event == sg.WIN_CLOSED:
            break

        fill_in_cell(event, game_end, current_player)

        if current_player == PLAYER_ONE:
            current_player = PLAYER_TWO
        else:
            current_player = PLAYER_ONE



def fill_in_cell(event, game_end, current_player):
    if window.Element(event).ButtonText == "" and not game_end:
        index = int(event.replace("-", ""))
        deck[index] = current_player
        window.Element(event).update(current_player)


        if 0 not in deck:
            print("JUEGO TERMINADO!")
            game_end = True

def check_victory():

    for winner_play in winning_plays:
        if deck[winner_play[0]] == deck[winner_play[1]] == deck[winner_play[2]] != 0:
            if deck[winner_play[0]] == PLAYER_ONE:
                print("El jugador 1 ha ganado!")
                game_end = True
            else:
                print("El jugador 2 ha ganado!")
                game_end = True


if __name__ == "__main__":
    main(game_end, current_player)
