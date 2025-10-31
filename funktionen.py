import csv
from datetime import datetime
from doctest import register_optionflag
from tkinter.constants import BROWSE

DATEI = 'budget.csv'


def datei_pruefen(): #prüfen, ob die CSV Datei exestiert, ansonsten wird diese erstellt
    try:
        with open (DATEI, 'x', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(['datum', 'kategorie', 'beschreibung', 'betrag', 'typ'])
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

def uebersicht_anzeigen():
    datei_pruefen() #funktion dateiprüfen wird abgeruft

    counter = 0

    with open(DATEI, 'r', newline = '') as file:    #öffnet datei im lesemodus und verhindert zusätzliche Lesezeilen


        reader = csv.DictReader(file)         #erstellt CSV-Reader, der jede Zeile als ein Wörterbuch einliest, man kann aud die werte direkt zugreifen

        print(f"\n{'Counter':<3} {'Datum':<12} {'Kategorie':<15} {'Betrag':<12} {'Typ':<10}") # geht jede Zeile durch
        print("-" * 70)

        for row in reader:
            counter += 1

            print(f"{counter:<12} {row['datum']:<12} {row['kategorie']:<15} {row['betrag']:<12} {row['typ']:<10}")      # printet die werte mit den gleichem abstand wie die namen der Spalten

    print(">>> Übersicht wird angezeigt")


def editieren():
    print(">>> editieren hinzufügen")

def abbruch():
    print(">>> Funktion abbruch, back to main menu")



#csv datei einbauen



