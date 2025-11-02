import csv
from datetime import datetime

DATEI = 'budget.csv'
bro=0

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

#Filmon
def ausgaben_hinzufuegen():
    datei_pruefen() #Geht zurück zur Funktion Datei überprüfen und checkt 
    #ob es die Datei schon gibt und ansonsten erstellt sie eine neue
    print('\n====Ausgabe Hinzufügen====')
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
    print('1) Transport')
    print('2) Einkäufe')
    print('3) Versicherungen')
    print('4) Miete')
    print('5) Steuern')
    print('6) Freizeit')
    print('7) Sparen')
    print('8) Well being')
    print('9) Sonstiges')
    
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
        else:
            print('Ungültige Eingabe, bitte wähle eine gültige Kategorie')

    '''In CSV Datei speichern'''
    with open(DATEI, 'a', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow([datum, kategorie,'', betrag, 'Ausgabe']) '' nur gemacht weil oben noch beschreibung steht

    print(f'\n Ausgabe von {betrag:.2f} CHF {kategorie} wurde gespeichert. \n')

    
#Janath
def uebersicht_anzeigen():
    print(">>> Übersicht wird angezeigt")

def editieren():
    print(">>> editieren hinzufügen")

def abbruch():
    print(">>> Funktion abbruch, back to main menu")



#csv datei einbauen



