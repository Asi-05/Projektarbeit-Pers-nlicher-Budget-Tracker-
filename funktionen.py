import csv                              #importiert das CSV-Modul, um mit CSV Dateien zu arbeiten
from datetime import datetime           #importiert die datetime-Klasse, um Datumsangaben zu verarbeiten

DATEI = 'budget.csv'                    #definiert den Dateinamen, in dem die Budgetdaten gespeichert werden


def datei_pruefen():    #prüfen, ob die CSV Datei exestiert, ansonsten wird diese erstellt
    try:
        with open (DATEI, 'x', newline = '') as file:       #öffnet die Datei im x Modus (erstellt neue Datei, wenn sie nicht existiert)
            writer = csv.writer(file)                       #erstellt ein CSV Schreibobjekt
            writer.writerow(['datum', 'betrag', 'typ', 'kategorie'])    #schreibt die spalten überschriften
    except: FileExistsError             #falls die Datei schon existiert, tritt dieser Fehler auf
    pass                                #Dann wird einfach nichts gemacht (Datei bleibt bestehen)
    
def einnahmen_hinzufuegen():        #funktion, um eine neue einnahme hinzuzufügen
    datei_pruefen()                 #ruft zuerst datei_pruefen() auf, um sicherzustellen, dass die CSV-Datei existiert

    print('\n ===== Einnahme hinzufügen =====')

    print('x) Zurück zum Hauptmenu')



    while True:                     #Wiederhole bis eine gültige zahl eingegeben wurde

        eingabe = input("Betrag (CHF): ").strip()

        if eingabe.lower() == 'x':
            return # zurück ins hauptmenu

        try:
            betrag = float(eingabe) #fragt den betrag ab und wandelt ihn in ein float um
            break                                   #beendet die schleife, wenn erfolgreich
        except ValueError:                          #wenn keine gültige zahl eingegeben wurde
            print("Bitte gültigen Betrag eingeben!")#fehlermeldug zeigen

    while True:
        datum_eingabe = input('Datum (DD. MM. YYYY): ').strip()   #fragt das Datum ab und entfernt die leerzeichen

        if eingabe.lower() == 'x':
            return  # zurück zum Hauptmenü

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
        writer.writerow([datum, betrag, 'Einnahme', kategorie])     #schreibt die neue einnahme als neue zeile in die Datei

    print(f'\nEinnahme von {betrag:.2f} CHF {kategorie} wurde gespeichert.\n')     #bestätigungsausgabe für den user

#Filmon
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

    

def datum_eingabe(prompt): #JANATH WAS IST DAS?
    while True:
        eingabe = input(prompt).strip()
        try:
            return datetime.strptime(eingabe, '%d.%m.%Y')
        except ValueError:
            print('Ungültiges Datum! Bitte im Format TT.MM.JJJJ eingeben.')

    '''In CSV Datei speichern'''
    with open(DATEI, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datum, betrag, 'Ausgabe', kategorie,])

    print(f'\n Ausgabe von {betrag:.2f} CHF {kategorie} wurde gespeichert. \n')

    
#Janath
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



def editieren():
    
    datei_pruefen()
    daten = []
    print('\n1) Eintrag löschen')
    print('2) Eintrag bearbeiten')

    optionauswahl = input("\nBitte wähle 1 oder 2:")

    if optionauswahl == '1':

        while True:
            datum_eingabe = input('Bitte Datum eingeben (DD. MM. YYYY): ').strip()         #fragt das Datum ab und entfernt die leerzeichen
            try:                                                            
                datum_obj = datetime.strptime(datum_eingabe, '%d.%m.%Y')    #prüft, ob das datum im richtigen format ist    
                datum = datum_obj.strftime('%d.%m.%Y')                      #formatiert das datum einheitlich für die csv datei                      
                break                                                       #beendet die schleife, wenn true
            except ValueError:                                              #falls das datum ungültig ist
                print('Ungültiges Datum! Bitte im Format TT.MM.YYYY eingeben.')
        
        while True: #Betrag abfragen
            try:
                betrag_suche = float(input("Gesuchter Betrag(CHF): "))
                break
            except ValueError:
                print("Bitte gültigen Betrag eingeben!")
            
        print('Einnahme oder Ausgabe')
        
        while True:
            AoE_auswahl = input('\nBitte Einnahme oder Ausgabe angeben:').strip()
            if AoE_auswahl == 'Einnahme':
                print('\nWähle eine Kategorie')

                print('\n1) Lohn')
                print('2) Sonstiges')

                while True:
                    kategorie_auswahl = input('\nBitte wähle eine Kategorie (1/2):')
                    if kategorie_auswahl == '1':
                        kategorie = 'Lohn'
                        break
                    elif kategorie_auswahl == '2':
                        kategorie = 'Sonstiges'
                        break
                    else:
                        print('Ungültige Eingabe, bitte 1 oder 2 wählen')
                break

            elif AoE_auswahl == 'Ausgabe':
                print('\nWähle eine Kategorie:')

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
                    kategorie_auswahl = input('\nBitte wähle eine Kategorie von 1-9: ')
                  
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
                        print('Ungültige Eingabe, bitte eine Kategorie von 1-9 wählen')
            break
   

        with open(DATEI, 'r', newline='') as file:
            reader = csv.DictReader(file)
            daten= list(reader)
        
        neue_daten = []

        geloescht= False
        for row in daten:
            if (float(row['betrag']) == betrag_suche and
                row['typ']== AoE_auswahl and
                row['kategorie']== kategorie and
                row ['datum']== datum):
                print(f'\nGefundener Eintrag: {row['datum']} | {row['betrag']} | {row['typ']} | {row['kategorie']}')
                bestaetigung = input('Diesen Eintrag löschen? (ja/nein):').lower()
                if bestaetigung=='ja':
                    geloescht=True
                    continue
            neue_daten.append(row)

        with open(DATEI, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames= ['datum', 'betrag','typ', 'kategorie'])
            writer.writeheader()
            writer.writerows(neue_daten)
        
        if geloescht:
            print('\n Eintrag wurde gelöscht')
        else:
            print('\n Kein Eintrag wurde gelöscht oder gefunden')


    elif optionauswahl == '2':
        while True:
            datum_eingabe = input('Bitte Datum eingeben (DD. MM. YYYY): ').strip()         #fragt das Datum ab und entfernt die leerzeichen
            try:                                                            
                datum_obj = datetime.strptime(datum_eingabe, '%d.%m.%Y')    #prüft, ob das datum im richtigen format ist    
                datum = datum_obj.strftime('%d.%m.%Y')                      #formatiert das datum einheitlich für die csv datei                      
                break                                                       #beendet die schleife, wenn true
            except ValueError:                                              #falls das datum ungültig ist
                print('Ungültiges Datum! Bitte im Format TT.MM.YYYY eingeben.')
        
        while True: #Betrag abfragen
            try:
                betrag_suche = float(input("Gesuchter Betrag (CHF): "))
                break
            except ValueError:
                print("Bitte gültigen Betrag eingeben!")
            
        print(' Einnahme oder Ausgabe')
        
        while True:
            AoE_auswahl = input('\nBitte Einnahme oder Ausgabe angeben:').strip()
            if AoE_auswahl == 'Einnahme':
                print('\nWähle eine Kategorie')

                print('\n1) Lohn')
                print('2) Sonstiges')

                while True:
                    kategorie_auswahl = input('\nBitte wähle eine Kategorie 1/2:')
                    if kategorie_auswahl == '1':
                        kategorie = 'Lohn'
                        break
                    elif kategorie_auswahl == '2':
                        kategorie = 'Sonstiges'
                        break
                    else:
                        print('Ungültige Eingabe, bitte 1 oder 2 wählen')
                break

            elif AoE_auswahl == 'Ausgabe':
                print('\nWähle eine Kategorie')

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
                    kategorie_auswahl = input('\nBitte wähle eine Kategorie von 1-9: ')
                  
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
                        print('Ungültige Eingabe, bitte eine Kategorie von 1-9 wählen')
            break
            

        with open(DATEI, 'r', newline='') as file:
            reader = csv.DictReader(file)
            daten= list(reader)   
        neue_daten = []
        bearbeitet= False

        for row in daten:
            if (
                round(float(row['betrag']),2)== round(betrag_suche,2) and
                row['typ']==AoE_auswahl.strip() and
                row['kategorie']== kategorie and
                row ['datum']== datum
            ):
                print(f'\nGefundener Eintrag: {row['datum']} | {row['betrag']} | {row['typ']} | {row['kategorie']}')
                bestaetigung = input('Diesen Eintrag bearbeiten? (ja/nein):').lower()
                if bestaetigung=='ja':
                    neuer_typ= input('Einnahme oder Ausgabe:')
                    neuer_betrag= input('Neuer Betrag: ')
                    neues_datum= input('Neues Datum (TT.MM.JJJ):')
                    ziel_typ= neuer_typ if neuer_typ else row['typ']
                    neue_kategorie= row['kategorie']
                    
                 
                    while True:
                        if ziel_typ =='Einnahme':
                            print('\n1)Lohn')
                            print('2) Sonstiges')
                            neue_kategorie_auswahl= input('Neue Kategorie (1/2) wählen:').strip()
                            if neue_kategorie_auswahl=='':
                                break
                            elif neue_kategorie_auswahl=='1':
                                neue_kategorie= 'Lohn'
                                break
                            elif neue_kategorie_auswahl=='2':
                                neue_kategorie='Sonstiges'
                                break
                            else:
                                print('Ungültige Eingabe, bitte 1 oder 2 wählen.')
                        elif ziel_typ== 'Ausgabe':
                                print('1) Transport')
                                print('2) Einkäufe')
                                print('3) Versicherungen')
                                print('4) Miete')
                                print('5) Steuern')
                                print('6) Freizeit')
                                print('7) Sparen')
                                print('8) Well being')
                                print('9) Sonstiges')
                                
                                neue_kategorie_auswahl= input('Neue Kategorie:').strip()
                                if neue_kategorie_auswahl=='':
                                    neue_kategorie=row['kategorie']
                                    break
                                elif neue_kategorie_auswahl == '1':
                                    neue_kategorie = 'Transport'
                                    break
                                elif neue_kategorie_auswahl == '2':
                                    neue_kategorie = 'Einkäufe'
                                    break
                                elif neue_kategorie_auswahl == '3':
                                    neue_kategorie = 'Versicherungen'
                                    break
                                elif neue_kategorie_auswahl == '4':
                                    neue_kategorie = 'Miete'
                                    break
                                elif neue_kategorie_auswahl == '5':
                                    neue_kategorie = 'Steuern'
                                    break
                                elif neue_kategorie_auswahl == '6':                                                                                                                                                                                                                                             
                                    neue_kategorie = 'Freizeit'
                                    break
                                elif neue_kategorie_auswahl == '7':
                                    neue_kategorie = 'Sparen'
                                    break
                                elif neue_kategorie_auswahl == '8':
                                    neue_kategorie = 'Well being'
                                    break
                                elif neue_kategorie_auswahl == '9':
                                    neue_kategorie = 'Sonstiges'
                                    break
                                else:
                                    print('Ungültige Eingabe, bitte eine Kategorie von 1-9 wählen')
                        else:
                            print('Ungültiger Typ angegeben. Bitte zuerst Einnahme oder Ausgabe eingeben')
                            break
                    if neuer_typ.strip()=='':
                        neuer_typ=row['typ']
                    if neues_datum.strip()=='':
                        neues_datum=row['datum']
                    if neuer_betrag.strip()=='':
                        neuer_betrag= row['betrag']
                          

                    neue_daten.append({
                        'datum': neues_datum,
                        'betrag': neuer_betrag,
                        'typ': neuer_typ,
                        'kategorie': neue_kategorie
                    })
                    bearbeitet= True
                    continue
            neue_daten.append(row)

        with open(DATEI, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames= ['datum', 'betrag','typ', 'kategorie'])
            writer.writeheader()
            writer.writerows(neue_daten)
                    
        if bearbeitet:
            print('\n Eintrag wurde bearbeitet')
        else:
            print('\n Kein Eintrag wurde bearbeitet oder gefunden')

            
                

def abbruch(): #Janath
    print(">>> Funktion abbruch, back to main menu")







