import csv                              #importiert das CSV-Modul, um mit CSV Dateien zu arbeiten
from datetime import datetime           #importiert die datetime-Klasse, um Datumsangaben zu verarbeiten

DATEI = 'budget.csv'                    #definiert den Dateinamen, in dem die Budgetdaten gespeichert werden


def datei_pruefen():    #prüfen, ob die CSV Datei exestiert, ansonsten wird diese erstellt
    try:
        with open (DATEI, 'x', newline = '') as file:       #öffnet die Datei im x Modus (erstellt neue Datei, wenn sie nicht existiert)
            writer = csv.writer(file)                       #erstellt ein CSV Schreibobjekt
            writer.writerow(['datum', 'kategorie', 'betrag', 'typ'])    #schreibt die spalten überschriften
    except: FileExistsError             #falls die Datei schon existiert, tritt dieser Fehler auf
    pass                                #Dann wird einfach nichts gemacht (Datei bleibt bestehen)
    
def einnahmen_hinzufuegen():        #funktion, um eine neue einnahme hinzuzufügen
    datei_pruefen()                 #ruft zuerst datei_pruefen() auf, um sicherzustellen, dass die CSV-Datei existiert

    print('\n ===== Einnahme hinzufügen =====')

    while True:                     #Wiederhole bis eine gültige zahl eingegeben wurde
        try:
            betrag = float(input("Betrag (CHF): ")) #fragt den betrag ab und wandelt ihn in ein float um
            break                                   #beendet die schleife, wenn erfolgreich
        except ValueError:                          #wenn keine gültige zahl eingegeben wurde
            print("Bitte gültigen Betrag eingeben!")#fehlermeldug zeigen

    while True:
        datum_eingabe = input('Datum (DD. MM. YYYY): ').strip()         #fragt das Datum ab und entfernt die leerzeichen
        try:                                                            
            datum_obj = datetime.strptime(datum_eingabe, '%d.%m.%Y')    #prüft, ob das datum im richtigen format ist    
            datum = datum_obj.strftime('%d.%m.%Y')                      #formatiert das datum einheitlich für die csv datei                      
            break                                                       #beendet die schleife, wenn true
        except ValueError:                                              #falls das datum ungültig ist
            print('Ungültiges Datum! Bitte im Format TT.MM.YYYY eingeben.') #fehlermeldung

    '''Kategorie wählen'''
    print('\nKategorie wählen:')        #zeigt dem benutzer die möglichen kategorien an
    print('1) Lohn')                    #option 1 Lohn
    print('2) Sonstiges')               #option 2 Sonstiges

    while True:     #wiederhole bis eine gültige kategorie gewählt wurde
        kategorie_auswahl = input('Bitte wähle 1 oder 2: ')         #fragt nach der auswahl
        if kategorie_auswahl == '1':                                #wenn 1 eingegeben wird
            kategorie = 'Lohn'                                      #kategorie auf lohn setzen
            break                                                       #schleife beenden
        elif kategorie_auswahl == '2':                              #wenn 2 eingegeben wird                              
            kategorie = 'Sonstiges'                                 #kategorie auf sonstiges setzen
            break                                                       #schleife beenden
        else:
            print('Ungültige Eingabe, bitte 1 oder 2 wählen')           #Fehlermeldung bei falscher Eingabe

    '''In CSV Datei speichern'''
    with open(DATEI, 'a', newline='') as file:          #öffnet die datei im appendmodus ('a'), um daten hinzuzufügen
        writer = csv.writer(file)                       #erstellt ein CSV-Schreibobjekt
        writer.writerow([datum, kategorie, betrag, 'Einnahme'])     #schreibt die neue einnahme als neue zeile in die Datei

    print(f'\nEinnahme von {betrag:.2f} CHF {kategorie} wurde gespeichert.\n')     #bestätigungsausgabe für den user


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



