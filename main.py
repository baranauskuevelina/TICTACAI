import random

# TICTACTOE Lenta
board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]


def display_board():
    for row in board:
        print('|'.join(row))
        print('-----')


def reset_board():
    global board
    board = [['', '', ''], ['', '', ''], ['', '', '']]


def reset_game():
    reset_board()
    display_board()


def update_board(row, col, symbol):
    if board[row][col] == '':
        board[row][col] = symbol
        return True
    else:
        return False


def get_player_symbol():
    while True:
        symbol = input("Pasirinkite savo simboli (X ar O): ").upper()
        if symbol in ['X', 'O']:
            return symbol
        else:
            print("Neteisingas pasirinkimas. Pasirinkite X arba O.")


def computer_move():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 'O'
    else:
        print("Nebera ejimu.")


def check_win(symbol):
    # kas laimejo
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False


def check_tie():
    return all(all(cell != '' for cell in row) for row in board)


# loopas
while True:
    reset_game()

    player_symbol = get_player_symbol()
    computer_symbol = 'O' if player_symbol == 'X' else 'X'

    round_count = 1
    while True:
        print(f"\nPartija {round_count}")
        display_board()

        try:
            row = int(input('Pasirinkite eile (0-2): '))
            col = int(input('Pasirinkite stulpeli (0-2): '))
            if 0 <= row < 3 and 0 <= col < 3:
                if update_board(row, col, player_symbol):
                    display_board()
                else:
                    print('Negalimas variantas, bandyk dar karta')
                    continue
            else:
                print('Neteisingas pasirinkimas, pasirink nuo 0 iki 2')
                continue
        except ValueError:
            print('Netinkamas pasirinkimas.')
            continue

        if check_win(player_symbol):
            print("Tu laimejai!")
            break
        elif check_tie():
            print("Lygiosios. Bandom is naujo!")
            break

        computer_move()
        print("Antras zaidejas pasirinko:")
        display_board()

        if check_win(computer_symbol):
            print("Kompiuteris laimejo. Bandyk is naujo!")
            break
        elif check_tie():
            print("Lygiosios. Bandom is naujo!")
            break

        round_count += 1

    # ... (previous code)

    round_count = 1
    while True:
        print(f"\nPartija {round_count}")
        display_board()

        # Player's move
        try:
            row = int(input('Pasirinkite eile (0-2): '))
            col = int(input('Pasirinkite stulpeli (0-2): '))
            if 0 <= row < 3 and 0 <= col < 3:
                if update_board(row, col, player_symbol):
                    display_board()
                else:
                    print('Negalimas variantas, bandyk dar karta')
                    continue
            else:
                print('Neteisingas pasirinkimas, pasirink nuo 0 iki 2')
                continue
        except ValueError:
            print('Netinkamas pasirinkimas, bandykite dar karta')
            continue

        # Check for a win or a tie after player's move
        if check_win(player_symbol):
            print("Tu laimejai!")
            break
        elif check_tie():
            print("Lygiosios. Bandom is naujo!")
            break

        computer_move()
        print("Antras zaidejas pasirinko:")
        display_board()

        if check_win(computer_symbol):
            print("Pralaimejai, Bandyk is naujo!")
            break
        elif check_tie():
            print("Lygiosios. Bandom is naujo!")
            break

        round_count += 1

    zaisti_dar_karta = input('Ar zaisi dar karta? (Taip/Ne): ').strip().lower()
    if zaisti_dar_karta != 'taip':
        print('Aciu uz zaidima! Viso gero!')
        break

    reset_game()
