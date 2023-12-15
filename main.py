# TIC TAC TOE

# LENTA
zaidimo_lenta = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
zaidejas = 1
def display_board():
    for eile in zaidimo_lenta:
        print('|'.join(eile))
        print('-----')

print(f'Zaidejas {zaidejas}, pasirinkite savo simboli (X ar O):')

while True:
    try:
        eile = int(input(f'Zaidejas, pasirinkite eile (0-2): '))
        stulpelis = int(input(f'Zaidejas {zaidejas}, pasirinkite stulpeli (0-2): '))

        if 0 <= eile < 3 and 0 <= stulpelis < 3 and zaidimo_lenta[eile][stulpelis] == '':

            zaidimo_lenta[eile][stulpelis] = 'X' if zaidejas == 1 else 'O'
            break
        else:
            print('Bandyk dar karta')

        display_board()
    except ValueError:
        print('Praleimejai, zaisk is naujo')

# while True:
    display_board()
    player_move()

# kas laimejo
    if laimetojas('X'):
        print("Tu laimejai!")
        reset_game()
        break

    if check_win('O'):
        print("Pralaimejai, bandyk is naujo")
        reset_game()
        break

    elif lygiosios():
        print("Lygiosios", "Bandyk is naujo")
        reset_game()
        break

    display_board()
    reset_game()

