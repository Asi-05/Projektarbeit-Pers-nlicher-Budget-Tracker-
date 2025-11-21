def kategorieauswahl_ausgabe():
    print('\nWähle eine Kategorie:')

    print('1) Transport')
    print('2) Einkäufe')
    print('3) Versicherungen')
    print('4) Miete')
    print('5) Steuern')
    print('6) Freizeit')
    print('7) Sparen')
    print('8) Well being')
    print('9) Sonstiges')
    print('x) zurück')

    kategorien = {
        '1': 'Transport',
        '2': 'Einkäufe',
        '3': 'Versicherungen',
        '4': 'Miete',
        '5': 'Steuern',
        '6': 'Freizeit',
        '7': 'Sparen',
        '8': 'Well being',
        '9': 'Sonstiges',
        'x': 'zurück'
    }

    print('\nWähle eine Kategorie:')
    for key, name in kategorien.items():
        print(f'{key}) {name}')

    while True:
        kategorie_auswahl = input('\nBitte wähle eine Kategorie von 1–9: ').strip()

        if kategorie_auswahl in kategorien:
            kategorie = kategorien[kategorie_auswahl]
            break
        elif kategorie_auswahl == 'x':
            return
        else:
            print('Ungültige Eingabe. Bitte nur Zahlen von 1 bis 9 eingeben.')

    print(f'\nKategorie gewählt: {kategorie}')
    return kategorie


def kategorieauswahl_einnahme():
    while True:

        print('\nWähle eine Kategorie:')

        print('\n1) Lohn')
        print('2) Sonstiges')

        print('x) zurück')
        kategorie_auswahl = input('\nBitte wähle eine Kategorie (1/2): ').strip()



        if kategorie_auswahl == '1':
            return 'Lohn'

        elif kategorie_auswahl == '2':
            return 'Sonstiges'

        elif kategorie_auswahl == 'x':
            return

        else:
            print('Ungültige Eingabe, bitte 1 oder 2 wählen.')

def kategorieauswahl_gesamt():
    print('\nWähle eine Kategorie:')

    print('\n1) Lohn')
    print('2) Transport')
    print('3) Einkäufe')
    print('4) Versicherungen')
    print('5) Miete')
    print('6) Steuern')
    print('7) Freizeit')
    print('8) Sparen')
    print('9) Well being')
    print('10) Sonstiges')
    print('x) zurück')

    kategorien = {
        '1': 'Lohn',
        '2': 'Transport',
        '3': 'Einkäufe',
        '4': 'Versicherungen',
        '5': 'Miete',
        '6': 'Steuern',
        '7': 'Freizeit',
        '8': 'Sparen',
        '9': 'Well being',
        '10': 'Sonstiges',
        'x': 'zurück'
    }

    print('\nWähle eine Kategorie:')
    for key, name in kategorien.items():
        print(f'{key}) {name}')

    while True:
        kategorie_auswahl = input('\nBitte wähle eine Kategorie von 1–9: ').strip()

        if kategorie_auswahl in kategorien:
            kategorie = kategorien[kategorie_auswahl]
            break
        elif kategorie_auswahl == 'x':
            return
        else:
            print('Ungültige Eingabe. Bitte nur Zahlen von 1 bis 9 eingeben.')

    print(f'\nKategorie gewählt: {kategorie}')
    return kategorie

