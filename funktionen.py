import csv
from datetime import datetime
from doctest import register_optionflag
from tkinter.constants import BROWSE

DATEI = 'budget.csv'


def datei_pruefen(): #prüfen, ob die CSV Datei exestiert, ansonsten wird diese erstellt
    try:
        with open (DATEI, 'x', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(['datum', 'kategorie', 'betrag', 'typ'])
    except: FileExistsError
    pass
    
def einnahmen_hinzufuegen():
    datei_pruefen() #funktion dateiprüfen wird abgeruft

    print('\n ===== Einnahme hinzufügen =====')

    while True: #Betrag abfragen
        try:
            betrag = float(input("Betrag (CHF): "))
            break
        except ValueError:
            print("Bitte gültigen Betrag eingeben!")

    while True:
        datum_eingabe = input('Datum (DD. MM. YYYY): ').strip()
        try:#prüfen ob eingabe Format korrekt ist
            datum_obj = datetime.strptime(datum_eingabe, '%d.%m.%Y')#% Format für CSV Datei zum Datum lesen
            datum = datum_obj.strftime('%d.%m.%Y')
            break
        except ValueError:
            print('Ungültiges Datum! Bitte im Format TT.MM.YYYY eingeben.')

    '''Kategorie wählen'''
    print('\nKategorie wählen:') 
    print('1) Lohn')
    print('2) Sonstiges')
    
    while True:

        kategorie_auswahl = input('Bitte wähle 1 oder 2: ')
        if kategorie_auswahl == '1':
            kategorie = 'Lohn'
            break
        elif kategorie_auswahl == '2':
            kategorie = 'Sonstiges'
            break
        else:
            print('Ungültige Eingabe, bitte 1 oder 2 wählen')

    '''In CSV Datei speichern'''
    with open(DATEI, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datum, kategorie, betrag, 'Einnahme'])

    print(f'\n Einnahme von {betrag:.2f} CHF {kategorie} wurde gespeichert. \n')


def ausgaben_hinzufuegen():


    print(">>> Ausgaben hinzufügen")

def datum_eingabe(prompt):
    while True:
        eingabe = input(prompt).strip()
        try:
            return datetime.strptime(eingabe, '%d.%m.%Y')
        except ValueError:
            print('Ungültiges Datum! Bitte im Format TT.MM.JJJJ eingeben.')

def uebersicht_anzeigen():
    datei_pruefen() #funktion dateiprüfen wird abgeruft

    counter = 0

    print('\n1) Kategorieübersicht')
    print('2) Bilanz einer bestimmten Periode')

    optionauswahl = input("\nBitte wähle 1 oder 2:")

    if optionauswahl == '1':

        print('\nWähle eine Kategorie')

        print('\n1) Lohn')
        print('2) Sonstiges')

        while True:
            kategorie_auswahl = input('\nBitte wähle 1 oder 2: ')
            if kategorie_auswahl == '1':
                kategorie = 'Lohn'
                break
            elif kategorie_auswahl == '2':
                kategorie = 'Sonstiges'
                break
            else:
                print('Ungültige Eingabe, bitte 1 oder 2 wählen')


        with open(DATEI, 'r', newline='') as file:  # öffnet datei im lesemodus und verhindert zusätzliche Lesezeilen

            reader = csv.DictReader(file) # erstellt CSV-Reader, der jede Zeile als ein Wörterbuch einliest, man kann aud die werte direkt zugreifen

            print(f'\nKategorie: {kategorie}')

            print(f"\n{'Counter':<10} {'Datum':<12} {'Betrag':<12} {'Typ':<10}")  # geht jede Zeile durch
            print("-" * 70)
            for row in reader:

                if row['kategorie'] == kategorie:

                    counter += 1

                    print(f"{counter:<10} {row['datum']:<12} {row['betrag']:<12} {row['typ']:<10} ")   # printet die werte mit den gleichem abstand wie die namen der Spalten

        print(">>> Übersicht wird angezeigt")


    elif optionauswahl == '2':


        datum_von = datum_eingabe('\nDatum von (TT.MM.JJJJ): ')
        datum_bis = datum_eingabe('Datum bis (TT.MM.JJJJ): ')
        while datum_bis < datum_von:
            print(' \nDas Enddatum darf nicht vor dem Startdatum liegen.')
            datum_bis = datum_eingabe('\nDatum bis (TT.MM.JJJJ): ')

        # CSV-Datei auswerten
        gesamt_einnahmen = 0
        gesamt_ausgaben = 0
        bilanz_lohn = 0
        bilanz_sonstiges = 0

        with open(DATEI, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row_datum = datetime.strptime(row['datum'], '%d.%m.%Y')
                if datum_von <= row_datum <= datum_bis:
                    betrag = float(row['betrag'])
                    if row['kategorie'] == 'Lohn':

                        # Gesamtbilanz
                        if row['typ'] == 'Einnahme':
                            gesamt_einnahmen += betrag
                        else:
                            gesamt_ausgaben += betrag

                        # Kategorie-spezifische Bilanz
                        if row['kategorie'] == 'Lohn':
                            bilanz_lohn += betrag if row['typ'] == 'Einnahme' else -betrag
                        elif row['kategorie'] == 'Sonstiges':
                            bilanz_sonstiges += betrag if row['typ'] == 'Einnahme' else -betrag

        print(f'\nBilanz vom {datum_von.strftime("%d.%m.%Y")} bis {datum_bis.strftime("%d.%m.%Y")}:')
        print(f'\nLohn: {bilanz_lohn:.2f} CHF')
        print(f'Sonstiges: {bilanz_sonstiges:.2f} CHF')
        print(f'\nEinnahmen: {gesamt_einnahmen:.2f} CHF')
        print(f'Ausgaben: {gesamt_ausgaben:.2f} CHF')
        print(f'\nGesamtbilanz: {gesamt_einnahmen - gesamt_ausgaben:.2f} CHF')



def editieren():
    print(">>> editieren hinzufügen")

def abbruch():
    print(">>> Funktion abbruch, back to main menu")



#csv datei einbauen



