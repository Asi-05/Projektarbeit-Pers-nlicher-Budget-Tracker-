from datetime import datetime  
from datei_pruefen import *
from datum_eingabe import *
import csv 



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

    '''Kategorie wählen'''
    print('\nKategorie wählen:') 
    print('1) Transport')
    print('2) Einkäufe')
    print('3) Versicherungen')
    print('4) Miete')
    print('5) Steuern')
    print('6) Freizeit')
    print('7) Sparen')
    print('8) Well being')
    print('9) Sonstiges')
    print('x) Zurück zum Hauptmenu')
    
    while True: 
        kategorie_auswahl = input('Bitte wähle eine Kategorie: ')
        if kategorie_auswahl == '1':
            kategorie = 'Transport'
            break
        elif kategorie_auswahl == '2':
            kategorie = 'Einkäufe'
            break
        elif kategorie_auswahl == '3':
            kategorie = 'Versicherungen'
            break
        elif kategorie_auswahl == '4':
            kategorie = 'Miete'
            break
        elif kategorie_auswahl == '5':
            kategorie = 'Steuern'
            break
        elif kategorie_auswahl == '6':
            kategorie = 'Freizeit'
            break
        elif kategorie_auswahl == '7':
            kategorie = 'Sparen'
            break
        elif kategorie_auswahl == '8':
            kategorie = 'Well being'
            break
        elif kategorie_auswahl == '9':
            kategorie = 'Sonstiges'
            break
        elif kategorie_auswahl == 'x':
            return
        else:
            print('Ungültige Eingabe, bitte wähle eine gültige Kategorie')

    '''In CSV Datei speichern'''
    with open(DATEI, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datum, betrag, 'Ausgabe',kategorie])

    print(f'\n Ausgabe von {betrag:.2f} CHF {kategorie} wurde gespeichert. \n')


