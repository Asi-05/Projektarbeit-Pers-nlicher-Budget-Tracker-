
from datetime import datetime  
from datei_kontrollieren.datei_pruefen import *
from datum_eingabe.datum_eingabe import *
from kategorie_auswahl.kategorieauswahl import *
import csv 


def uebersicht_anzeigen():
    '''Übersicht Anzeige Funktion'''
    datei_pruefen()                                                                                 #funktion dateiprüfen wird abgeruft

    counter = 0

    print('\n1) Kategorieübersicht')
    print('2) Bilanz einer bestimmten Periode')

    print('x) Zurück zum Hauptmenu')

    while True:

        optionauswahl = input("\nBitte wähle 1 oder 2:")

        if optionauswahl == '1':

            kategorie = kategorieauswahl_gesamt()


            with open(DATEI, 'r', newline='') as file:                                                  #öffnet datei im lesemodus und verhindert zusätzliche Lesezeilen

                reader = csv.DictReader(file)                                                           #erstellt CSV-Reader, der jede Zeile als ein Wörterbuch einliest, man kann aud die werte direkt zugreifen.

                print(f'\nKategorie: {kategorie}')

                print(f"\n{'Counter':<10} {'Datum':<12} {'Betrag':<12} {'Typ':<10}")                    #geht jede Zeile durch #EVTL. SUMME HINZUFÜGEN
                print("-" * 70)
                for row in reader:

                    if row['kategorie'] == kategorie:

                        counter += 1

                        print(f"{counter:<10} {row['datum']:<12} {row['betrag']:<12} {row['typ']:<10} ") #printet die werte mit den gleichem abstand wie die namen der Spalten
            break



        elif optionauswahl == '2':

            #verlangt beim User die Eingabe vom von Datum und bis Datum + es wird mit der Funktion datum_eingabe geprüft und speichert diese bei der jeweiligen Variable ein
            datum_von = datum_eingabe_uerbesichtanzeigen('\nDatum von (TT.MM.JJJJ): ')
            datum_bis = datum_eingabe_uerbesichtanzeigen('\nDatum bis (TT.MM.JJJJ): ')
            while datum_bis < datum_von:                                                            #Überprüfung ob datum_bis kleiner ist als datum_von
                print(' \nDas Enddatum darf nicht vor dem Startdatum liegen.')
                datum_bis = datum_eingabe_uerbesichtanzeigen('\nDatum bis (TT.MM.JJJJ): ')

            #CSV-Datei auswerten
            gesamt_einnahmen = 0
            gesamt_ausgaben = 0
            bilanz_lohn = 0
            bilanz_transport = 0
            bilanz_einkaeufe = 0
            bilanz_versicherungen = 0
            bilanz_miete = 0
            bilanz_steuern = 0
            bilanz_freizeit = 0
            bilanz_sparen = 0
            bilanz_wellbeing = 0
            bilanz_sonstiges = 0

            with open(DATEI, 'r', newline='') as file:                                              # öffnet die Datei im lesemodus als dile
                reader = csv.DictReader(file)                                                       # liest die csv.datei als dictionary

                # iteriert alle zeilen durch und wandelt das datum von einem string zu einem datetime objekt
                for row in reader:
                    row_datum = datetime.strptime(row['datum'], '%d.%m.%Y')
                    # überprüft ob das datum im gewünschten bereich drin ist
                    if datum_von <= row_datum <= datum_bis:
                        betrag = float(row['betrag'])                                               # wandelt den betrag von einem string zu einem float zum rechnen

                        #Gesamtbilanz (addiert zur einnahme oder ausgabe)
                        if row['typ'] == 'Einnahme':
                            gesamt_einnahmen += betrag
                        else:
                            gesamt_ausgaben += betrag

                            #Kategorie-spezifische Bilanz

                        #Kategorie-spezifische Bilanz (addiert zur jeweiligen kategorie)
                        if row['kategorie'] == 'Lohn':
                            bilanz_lohn += betrag if row['typ'] == 'Einnahme' else -betrag
                        elif row['kategorie'] == 'Transport':
                            bilanz_transport += betrag if row['typ'] == 'Einnahme' else -betrag
                        elif row['kategorie'] == 'Einkäufe':
                            bilanz_einkaeufe += betrag if row['typ'] == 'Einnahme' else -betrag
                        elif row['kategorie'] == 'Versicherungen':
                            bilanz_versicherungen += betrag if row['typ'] == 'Einnahme' else -betrag
                        elif row['kategorie'] == 'Miete':   
                            bilanz_miete += betrag if row['typ'] == 'Einnahme' else -betrag
                        elif row['kategorie'] == 'Steuern':
                            bilanz_steuern += betrag if row['typ'] == 'Einnahme' else -betrag
                        elif row['kategorie'] == 'Freizeit':
                            bilanz_freizeit += betrag if row['typ'] == 'Einnahme' else -betrag
                        elif row['kategorie'] == 'Sparen':
                            bilanz_sparen += betrag if row['typ'] == 'Einnahme' else -betrag
                        elif row['kategorie'] == 'Well being':
                            bilanz_wellbeing += betrag if row['typ'] == 'Einnahme' else -betrag
                        elif row['kategorie'] == 'Sonstiges':
                            bilanz_sonstiges += betrag if row['typ'] == 'Einnahme' else -betrag

            print(f'\nBilanz vom {datum_von.strftime("%d.%m.%Y")} bis {datum_bis.strftime("%d.%m.%Y")}:')
            print(f'\nLohn: \t\t\t\t{bilanz_lohn:.2f} CHF')
            print(f'\nTransport: \t\t\t{bilanz_transport:.2f} CHF')
            print(f'\nEinkäufe: \t\t\t{bilanz_einkaeufe:.2f} CHF')
            print(f'\nVersicherungen: \t\t{bilanz_versicherungen:.2f} CHF')
            print(f'\nMiete: \t\t\t\t{bilanz_miete:.2f} CHF')
            print(f'\nSteuern: \t\t\t{bilanz_steuern:.2f} CHF')
            print(f'\nFreizeiz: \t\t\t{bilanz_freizeit:.2f} CHF')
            print(f'\nSparen: \t\t\t{bilanz_sparen:.2f} CHF')
            print(f'\nWell being: \t\t\t{bilanz_wellbeing:.2f} CHF')
            print(f'\nSonstiges: \t\t\t{bilanz_sonstiges:.2f} CHF')

            print(f'\nEinnahmen: \t\t\t{gesamt_einnahmen:.2f} CHF')
            print(f'Ausgaben: \t\t\t{gesamt_ausgaben:.2f} CHF')

            print(f'\nGesamtbilanz: \t\t\t{gesamt_einnahmen - gesamt_ausgaben:.2f} CHF')
            break
        elif optionauswahl == 'x':
            return
        else:
            print('Ungültige Eingabe. Bitte nur 1,2 oder x angeben.')