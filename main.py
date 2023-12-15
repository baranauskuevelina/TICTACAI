# TIC TAC TOE

# LENTA
zaidimo_lenta = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

def display_board():
    for eile in zaidimo_lenta:
        print('|'.join(eile))
        print('-----')

def zaidejo_ivedimas(zaidejas):
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

# loopas
while True:

    display_board()
    zaidejo_ivedimas(1)
