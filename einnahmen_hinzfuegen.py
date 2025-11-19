from datetime import datetime  
from datei_pruefen import *
from datum_eingabe import *
import csv 

DATEI = 'budget.csv' 

def einnahmen_hinzufuegen():        #funktion, um eine neue einnahme hinzuzufügen
    datei_pruefen()                 #ruft zuerst datei_pruefen() auf, um sicherzustellen, dass die CSV-Datei existiert

    print('\n ===== Einnahme hinzufügen =====')

    print('x) Zurück zum Hauptmenu')



    while True:                     #Wiederhole bis eine gültige zahl eingegeben wurde

        eingabe = input("Betrag (CHF): ").strip()

        if eingabe.lower() == 'x':
            return # zurück ins hauptmenu

        try:
            betrag = float(eingabe)                 #fragt den betrag ab und wandelt ihn in ein float um
            break                                   #beendet die schleife, wenn erfolgreich
        except ValueError:                          #wenn keine gültige zahl eingegeben wurde
            print("Bitte gültigen Betrag eingeben!")#fehlermeldug zeigen

    datum = datum_eingabe()                 #Datum eingabe Funktion wird aufgerufen

    '''Kategorie wählen'''
    print('\nKategorie wählen:')        #zeigt dem benutzer die möglichen kategorien an
    print('1) Lohn')                    #option 1 Lohn
    print('2) Sonstiges')               #option 2 Sonstiges

    print('x) Zurück zum Hauptmenu')

    while True:     #wiederhole bis eine gültige kategorie gewählt wurde
        kategorie_auswahl = input('Bitte wähle 1 oder 2: ')         #fragt nach der auswahl
        if kategorie_auswahl == '1':                                #wenn 1 eingegeben wird
            kategorie = 'Lohn'                                      #kategorie auf lohn setzen
            break                                                       #schleife beenden
        elif kategorie_auswahl == '2':                              #wenn 2 eingegeben wird                              
            kategorie = 'Sonstiges'                                 #kategorie auf sonstiges setzen
            break                                                       #schleife beenden
        elif kategorie_auswahl == 'x':                               #zurück zum Hauptmenü
            return
        else:
            print('Ungültige Eingabe, bitte 1 oder 2 wählen')           #Fehlermeldung bei falscher Eingabe

    '''In CSV Datei speichern'''
    with open(DATEI, 'a', newline='') as file:          #öffnet die datei im appendmodus ('a'), um daten hinzuzufügen
        writer = csv.writer(file)                       #erstellt ein CSV-Schreibobjekt
        writer.writerow([datum, betrag, 'Einnahme', kategorie])   #schreibt die neue einnahme als neue zeile in die Datei

    print(f'\nEinnahme von {betrag:.2f} CHF {kategorie} wurde gespeichert.\n')     #bestätigungsausgabe für den user
