from datetime import datetime  
from datei_kontrollieren.datei_pruefen import *     #importiert die funktion zur Überprüfung/Erstellung der CSV-Datei
from datum_eingabe.datum_eingabe import *           #importiert funktion datum eingabe mit kontrolle
import csv
from kategorie_auswahl.kategorieauswahl import *    #Importiert Auswahl für Kategorie



def ausgaben_hinzufuegen():
    '''Funktion, um ausgaben hinzuzufügen'''
    datei_pruefen()                                         #Geht zurück zur Funktion Datei überprüfen und checkt 
                                                            #ob es die Datei schon gibt und ansonsten erstellt sie eine neue
    print('\n====Ausgabe Hinzufügen====')

    print('x) Zurück zum Hauptmenu')

    while True:                                             #Betrag abfragen
        eingabe = input("Betrag (CHF): ").strip()           #Fragt den nutzer nach dem Betrag und strip entfernt die Leerzeichen am Anfang und Ende

        if eingabe.lower() == 'x':                          #schaut ob der User x oder X eingegeben hat, um zurückzukehren
            return                                          #zurück zum Hauptmenu

        try:                                                #versucht die eingabe in ein float umzuwandeln
            betrag = float(eingabe)
            
            if betrag < 0:                                  #überprüft ob die eingabe eine negative zahl ist
                print('Bitte positiven Betrag eingeben.')   #gibt diese Rückmeldung bei negativer Zahl und kehrt dann zur Betrag Abfrage zurück
                continue
            
            break                                           #wenn umwandlung in float und postiver betrag dann wird die schleife beendet
        except ValueError:                                  #wird ausgelöst wenn die eingabe nicht in eine float umgewnadelt werden kann
            print("Bitte gültigen Betrag eingeben!")

    datum = datum_eingabe()                                 #Datum eingabe Funktion wird aufgerufen

    kategorie = kategorieauswahl_ausgabe()                  #ruft die kategorien zum typ ausgabe ab und verlangt eingabe vom user

                                                            #abschnitt zum in der csv datei speichern
    '''In CSV Datei speichern'''
                                                            #öffnet die datei (DATEI) im Anhänge Modus (a, append), newline= verhindert leere Zeichen
    with open(DATEI, 'a', newline='') as file:              #with open damit die datei am schluss automatisch geschlossen wird
        writer = csv.writer(file)                           #erstellt eine csv-wirter objekt für die geöffnete datei
        writer.writerow([datum, betrag, 'Ausgabe',kategorie]) #schreibt eine neue zeile mit den erfassten date: datum, betrag, ausgabe, kateogire

    print(f'\nAusgabe von {betrag:.2f} CHF {kategorie} wurde gespeichert. \n') #der Betrag wird auf 2 dezimalen formatiert und user erhält bestätigung von kategorie und betrag


