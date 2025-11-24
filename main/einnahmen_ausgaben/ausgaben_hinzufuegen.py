from datetime import datetime  
from datei_kontrollieren.datei_pruefen import *
from datum_eingabe.datum_eingabe import *
import csv
from kategorie_auswahl.kategorieauswahl import *



def ausgaben_hinzufuegen():
    datei_pruefen() #Geht zurück zur Funktion Datei überprüfen und checkt 
    #ob es die Datei schon gibt und ansonsten erstellt sie eine neue
    print('\n====Ausgabe Hinzufügen====')

    print('x) Zurück zum Hauptmenu')

    while True: #Betrag abfragen
        eingabe = input("Betrag (CHF): ").strip()

        if eingabe.lower() == 'x':
            return # zurück zum Hauptmenu

        try:
            betrag = float(eingabe)
            break
        except ValueError:
            print("Bitte gültigen Betrag eingeben!")

    datum = datum_eingabe()      #Datum eingabe Funktion wird aufgerufen

    kategorie = kategorieauswahl_ausgabe()

    '''In CSV Datei speichern'''
    with open(DATEI, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datum, betrag, 'Ausgabe',kategorie])

    print(f'\nAusgabe von {betrag:.2f} CHF {kategorie} wurde gespeichert. \n')


