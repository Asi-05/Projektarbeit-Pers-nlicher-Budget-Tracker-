
from datetime import datetime  
from datei_pruefen import *
from datum_eingabe import *
import csv 


def uebersicht_anzeigen():
    datei_pruefen() #funktion dateiprüfen wird abgeruft

    counter = 0

    print('\n1) Kategorieübersicht')
    print('2) Bilanz einer bestimmten Periode')

    print('x) Zurück zum Hauptmenu')



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

            reader = csv.DictReader(file) # erstellt CSV-Reader, der jede Zeile als ein Wörterbuch einliest, man kann aud die werte direkt zugreifen.

            print(f'\nKategorie: {kategorie}')

            print(f"\n{'Counter':<10} {'Datum':<12} {'Betrag':<12} {'Typ':<10}")  # geht jede Zeile durch #EVTL. SUMME HINZUFÜGEN
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

    elif optionauswahl == 'x':
        return