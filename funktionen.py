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

def uebersicht_anzeigen():
    print(">>> Übersicht wird angezeigt")

def editieren():
    print(">>> editieren hinzufügen")

def abbruch():
    print(">>> Funktion abbruch, back to main menu")



#csv datei einbauen



