import PySimpleGUI as Sg

button_size = (7, 3)
PLAYER_ONE = "X"
PLAYER_TWO = "O"
deck = [0, 0, 0,
        0, 0, 0,
        0, 0, 0]
winning_plays = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
current_player = PLAYER_ONE
layout = [[
    Sg.Button("", key="-0-", size=button_size),
    Sg.Button("", key="-1-", size=button_size),
    Sg.Button("", key="-2-", size=button_size)],
    [
        Sg.Button("", key="-3-", size=button_size),
        Sg.Button("", key="-4-", size=button_size),
        Sg.Button("", key="-5-", size=button_size)],
    [
        Sg.Button("", key="-6-", size=button_size),
        Sg.Button("", key="-7-", size=button_size),
        Sg.Button("", key="-8-", size=button_size)],
        [Sg.Text("", key="-WINNER-")],
        [Sg.Button("Reiniciar", key="-R-", size=(7, 2))]

]
window = Sg.Window("Tres en raya", layout)
game_end = False


def main():
    global current_player
    while True:

        event = window.read()[0]

        if event == Sg.WIN_CLOSED:
            break

        fill_in_cell(event)
        check_victory()

        if event == "-R-":
            reset_game()


def fill_in_cell(event):
    global game_end, current_player
    if 0 not in deck:
        window.Element("-WINNER-").update("JUEGO TERMINADO!")
        game_end = True
    if window.Element(event).ButtonText == "" and not game_end:
        index = int(event.replace("-", ""))
        deck[index] = current_player
        window.Element(event).update(current_player)

    if current_player == PLAYER_ONE:
        current_player = PLAYER_TWO
    else:
        current_player = PLAYER_ONE


def check_victory():
    global game_end
    for winner_play in winning_plays:
        if deck[winner_play[0]] == deck[winner_play[1]] == deck[winner_play[2]] != 0:
            if deck[winner_play[0]] == PLAYER_ONE:
                window.Element("-WINNER-").update("El jugador 1 ha ganado!")
            else:
                window.Element("-WINNER-").update("El jugador 2 ha ganado!")
            game_end = True


def reset_game():
    global deck, current_player, game_end
    current_player = PLAYER_ONE
    for button_number in range(9):
        reset_button = "-" + str(button_number) + "-"
        window.Element(reset_button).update("")
        deck = [0, 0, 0,
                0, 0, 0,
                0, 0, 0]
    window.Element("-WINNER-").update("")
    game_end = False


if __name__ == "__main__":
    main()
