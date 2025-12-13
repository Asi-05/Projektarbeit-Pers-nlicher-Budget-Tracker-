from datetime import datetime  
from datei_kontrollieren.datei_pruefen import *
from datum_eingabe.datum_eingabe import *
from kategorie_auswahl.kategorieauswahl import *
import csv 

DATEI = 'budget.csv' 

def einnahmen_hinzufuegen():                                                        #funktion, um eine neue einnahme hinzuzufügen
    """Funktion, um eine neue einnahme hinzuzufügen"""
    datei_pruefen()                                                                 #ruft zuerst datei_pruefen() auf, um sicherzustellen, dass die CSV-Datei existiert

    print('\n ===== Einnahme hinzufügen =====')

    print('x) Zurück zum Hauptmenu')



    while True:                                                                     #Wiederhole bis eine gültige zahl eingegeben wurde

        eingabe = input("Betrag (CHF): ").strip()

        if eingabe.lower() == 'x':
            return                                                                  #zurück ins hauptmenu

        try:
            betrag = float(eingabe)                                                 #fragt den betrag ab und wandelt ihn in ein float um
            
            if betrag < 0:
                print('Bitte Positiven Betrag eingeben.')
                continue
            
            break                                                                   #beendet die schleife, wenn erfolgreich
        except ValueError:                                                          #wenn keine gültige zahl eingegeben wurde
            print("Bitte gültigen Betrag eingeben!")                                #fehlermeldung zeigen

    datum = datum_eingabe()                                                         #Datum eingabe Funktion wird aufgerufen

    kategorie = kategorieauswahl_einnahme()

    '''In CSV Datei speichern'''
    with open(DATEI, 'a', newline='') as file:                                      #öffnet die datei im appendmodus ('a'), um daten hinzuzufügen
        writer = csv.writer(file)                                                   #erstellt ein CSV-Schreibobjekt
        writer.writerow([datum, betrag, 'Einnahme', kategorie])                     #schreibt die neue einnahme als neue zeile in die Datei

    print(f'\nEinnahme von {betrag:.2f} CHF {kategorie} wurde gespeichert.\n')      #bestätigungsausgabe für den user
