from datetime import datetime  
from datei_pruefen import *
from datum_eingabe import *
import csv 

def editieren():
    
    datei_pruefen() #Stellt sicher, dass die CSV existiert und erstellt sie gegebenfalls mit den Spaltenüberschriften
    daten = [] #Erstellt die Variabel Daten als leere Liste, um spätere Fehlermeldungen zu vermeiden
    AoE_auswahl=''
    while True:
        print('\n1) Eintrag löschen')
        print('2) Eintrag bearbeiten')

        optionauswahl = input("\nBitte wähle 1 oder 2:") #Speichert die Benutzerwahl als Variabel Optionsauswahl

        if optionauswahl == '1': #Startet diesen Block nur wenn 1 gewählt wurde

            datum = datum_eingabe() #Ruft die Funkiton Datum_eingabe und speichert es als Datum ab
            
            while True: #Beginnt eine Schleife und zwingt den User für eine gültige Betrag Eingabe
                try:
                    betrag_suche = float(input("Gesuchter Betrag(CHF): ")) #Verlangt Input vom User und wandelt es in ein Float um
                    break #Beendet die Schleife wenn der User eine gültige Eingabe macht
                except ValueError: #Fängt Fehler ab, wenn der Benutzer keinen gültigen Betrag eingegeben hat
                    print("Bitte gültigen Betrag eingeben!")
                
            print('Einnahme oder Ausgabe')
            
            while True: #Beginnt eine neue Schleife für die Einnahme oder Ausgabe
                AoE = input('\nBitte Einnahme(1) oder Ausgabe(2) angeben (1/2):').strip() #Fordert den User aus Einnahme oder Ausgabe einzugeben und das .strip entfernt Leerzeichen
                if AoE == '1': #Wird ausgeführt wenn der User Einnahmen eingibt
                    AoE_auswahl='Einnahme'
                    print('\nWähle eine Kategorie')

                    print('\n1) Lohn')
                    print('2) Sonstiges')

                    while True: #Beginnt eine neue schleife um einen gültige Eingabe zur Kategorieauswahl zu erhalten
                        kategorie_auswahl = input('\nBitte wähle eine Kategorie (1/2):')
                        if kategorie_auswahl == '1':
                            kategorie = 'Lohn'
                            break #Beendet die Schleife wenn der User eine gültige Eingabe macht
                        elif kategorie_auswahl == '2':
                            kategorie = 'Sonstiges'
                            break #Beendet die Schleife wenn der User eine gültige Eingabe macht
                        else:
                            print('Ungültige Eingabe, bitte 1 oder 2 wählen')
                    break
            
                elif AoE == '2':
                    AoE_auswahl='Ausgabe'
                    
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
                    while True: #Beginnt eine neue schleife um einen gültige Eingabe zur Kategorieauswahl zu erhalten
                        kategorie_auswahl = input('\nBitte wähle eine Kategorie von 1-9: ')
                    
                        if kategorie_auswahl == '1':
                            kategorie = 'Transport'
                            break #Beendet die Schleife wenn der User eine gültige Eingabe macht
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
                            break #Beendet die Schleife wenn der User eine gültige Eingabe macht
                        else:
                            print('Ungültige Eingabe, bitte eine Kategorie von 1-9 wählen')
                    break
                else:
                    print('Ungültige Eingabe, gib bitte 1/2 an!')
                
    

            with open(DATEI, 'r', newline='') as file: #Öffnet die CSV Datei im Lesemodus (r)
                reader = csv.DictReader(file) #Erstellt ein CSV-Reader-Objekt, das Zeilen als Dictionaries liest
                daten= list(reader) #Liest alle vorhandenen Daten aus der Datei in die Liste daten
            
            neue_daten = [] #Erstellt eine leere Liste, die alle zu behaltenden Einträge aufnehmen wird

            geloescht= False #Setzt ein Flag auf False, um zu verfolgen, ob ein Eintrag gelöscht wurde
            for row in daten: #Beginnt eine Schleife, die jede Zeile (jeden Eintrag), in der Liste daten durchläuft
                if (float(row['betrag']) == betrag_suche and #Prüft ob Betrag der akutellen Zeile mit dem gesuchten übereinstimmt
                    row['typ']== AoE_auswahl and #überprüft Typ
                    row['kategorie']== kategorie and #überprüft Kategorie
                    row ['datum']== datum): #überprüft Datum 
                    print(f'\nGefundener Eintrag: {row['datum']} | {row['betrag']} | {row['typ']} | {row['kategorie']}') #Gibt den gefunden Eintrag aus
                    bestaetigung = input('1=ja,2=nein\n''Diesen Eintrag löschen?(1/2):') #fragt den User ab und wertet es als Kleinschreibung
                    if bestaetigung=='1':
                        geloescht=True #Setzt gelöscht auf True
                        continue #springt zur nächsten for-schleife und überspringt die folgende append Zeile
                neue_daten.append(row) #Fügt die aktuelle Zeile zur Liste neue_daten hinzu, wenn sie nicht gelöscht wurde

            with open(DATEI, 'w', newline='') as file:  #öffnet CSV im Schreibmodus, was den Inhalt löscht
                writer = csv.DictWriter(file, fieldnames= ['datum', 'betrag','typ', 'kategorie']) #Erstellt ein CSv Schreibobjekt mit definierten Spaltennamen
                writer.writeheader() #Schreibt die Spaltenüberschriften in die Datei
                writer.writerows(neue_daten) #Schreibt alle Zeilen aus der Liste neue daten in die datei
            
            if geloescht: #falls geloescht=true dann:
                print('\n Eintrag wurde gelöscht')
            else:
                print('\nKein Eintrag wurde gelöscht oder gefunden')
            break  

        elif optionauswahl == '2':
            
            datum = datum_eingabe() #Ruft die Funkiton Datum_eingabe und speichert es als Datum ab
            
            while True: #Beginnt eine Schleife und zwingt den User für eine gültige Betrag Eingabe
                try:
                    betrag_suche = float(input("Gesuchter Betrag (CHF): ")) #Verlangt Input vom User und wandelt es in ein Float um
                    break #Beendet die Schleife wenn der User eine gültige Eingabe macht
                except ValueError: #Fängt Fehler ab, wenn der Benutzer keinen gültigen Betrag eingegeben hat
                    print("Bitte gültigen Betrag eingeben!")
                
            print('Einnahme oder Ausgabe')
            
            while True: #Beginnt eine neue Schleife für die Einnahme oder Ausgabe
                AoE = input('\nBitte Einnahme(1) oder Ausgabe(2) angeben (1/2):').strip() #Fordert den User aus Einnahme oder Ausgabe einzugeben und das .strip entfernt Leerzeichen
                if AoE == '1': #Wird ausgeführt wenn der User Einnahmen eingibt
                    AoE_auswahl = 'Einnahme'
                    print('\nWähle eine Kategorie')

                    print('\n1) Lohn')
                    print('2) Sonstiges')

                    while True: #Beginnt eine neue Schleife für die Einnahme oder Ausgabe
                        kategorie_auswahl = input('\nBitte wähle eine Kategorie 1/2:')
                        if kategorie_auswahl == '1':
                            kategorie = 'Lohn'
                            break #Beendet die Schleife wenn der User eine gültige Eingabe macht
                        elif kategorie_auswahl == '2':
                            kategorie = 'Sonstiges'
                            break
                        else:
                            print('Ungültige Eingabe, bitte 1 oder 2 wählen')
                    break #Beendet die Schleife 

                elif AoE == '2': 
                    AoE_auswahl = 'Ausgabe'
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
                    while True: #Beginnt eine neue schleife um einen gültige Eingabe zur Kategorieauswahl zu erhalten
                        kategorie_auswahl = input('\nBitte wähle eine Kategorie von 1-9: ')
                    
                        if kategorie_auswahl == '1':
                            kategorie = 'Transport'
                            break
                        elif kategorie_auswahl == '2':
                            kategorie = 'Einkäufe'
                            break
                        elif kategorie_auswahl == '3':
                            kategorie = 'Versicherungen'
                            break #Beendet die Schleife wenn der User eine gültige Eingabe macht
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
                            break #Beendet die Schleife wenn der User eine gültige Eingabe macht
                        else:
                            print('Ungültige Eingabe, bitte eine Kategorie von 1-9 wählen')
                    break #Beendet die Schleife 
                else:
                    print('Ungültige Eingabe, gib bitte 1/2 an!')
                

            with open(DATEI, 'r', newline='') as file: #Öffnet die CSV Datei im Lesemodus (r)
                reader = csv.DictReader(file) #Erstellt ein CSV-Reader-Objekt, das Zeilen als Dictionaries liest
                daten= list(reader)   #Liest alle vorhandenen Daten aus der Datei in die Liste daten
            neue_daten = [] #Liste zur Aufnahme aller Einträge (geändert und unverändert)
            bearbeitet= False #Flag, das True wird wenn ein Eintrag erfolgreich bearbeitet wurde

            for row in daten: #Durchläuft jeden Eintrag
                if ( #Prüft ob der eintrag mit allen Suchkriterien übereinstimmt
                    round(float(row['betrag']),2)== round(betrag_suche,2) and
                    row['typ']==AoE_auswahl.strip() and
                    row['kategorie']== kategorie and
                    row ['datum']== datum
                    
                ):
                    print(f'\nGefundener Eintrag: {row['datum']} | {row['betrag']} | {row['typ']} | {row['kategorie']}') #Gibt den gefunden Eintrag aus
                    bestaetigung = input('1=ja | 2=nein\n''Diesen Eintrag bearbeiten?(1/2):') #fragt den User ab und wertet es als Kleinschreibung
                    if bestaetigung=='1':
                        while True:
                            AoE = input('\nBitte Einnahme(1) oder Ausgabe(2) angeben (1/2):').strip() #Fordert den User aus Einnahme oder Ausgabe einzugeben und das .strip entfernt Leerzeichen
                            if AoE=='1':
                                neuer_typ='Einnahme'
                                break
                            elif AoE=='2':
                                neuer_typ='Ausgabe'
                                break
                            elif AoE=='':
                                neuer_typ=''
                                break
                            else:
                                print('Ungültige Eingabe! Bitte 1/2 wählen')

                        neuer_betrag= input('Neuer Betrag: ') #Fragt nach Betrag
                        neues_datum= input('Neues Datum (TT.MM.YYYY):') #Fragt neues Datum
                        ziel_typ= neuer_typ if neuer_typ else row['typ'] #bestimmt ziel-typ für die Kategorie-Auswahl(neuer oder alter typ, wennneuer typ leer gelassen)
                        neue_kategorie= row['kategorie'] #Setzt die alte Kategorie als Standardwert
                        
                    
                        while True: #Beginnt Schleife für neue Kategorie
                            if ziel_typ =='Einnahme': #Falls Einnahme als typ definiert wurde:
                                print('\n1) Lohn')
                                print('2) Sonstiges')
                                neue_kategorie_auswahl= input('Neue Kategorie (1/2) wählen:').strip()
                                if neue_kategorie_auswahl=='':
                                    break #Beendet die Schleife wenn der User eine gültige Eingabe macht
                                elif neue_kategorie_auswahl=='1':
                                    neue_kategorie= 'Lohn'
                                    break
                                elif neue_kategorie_auswahl=='2':
                                    neue_kategorie='Sonstiges'
                                    break #Beendet die Schleife wenn der User eine gültige Eingabe macht
                                else:
                                    print('Ungültige Eingabe, bitte 1 oder 2 wählen.')
                            elif ziel_typ== 'Ausgabe': #Falls Ausgabe gewählt wurde
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
                                        break #Beendet die Schleife wenn der User eine gültige Eingabe macht
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
                                        break #Beendet die Schleife wenn der User eine gültige Eingabe macht
                                    elif neue_kategorie_auswahl == '7':
                                        neue_kategorie = 'Sparen'
                                        break
                                    elif neue_kategorie_auswahl == '8':
                                        neue_kategorie = 'Well being'
                                        break
                                    elif neue_kategorie_auswahl == '9':
                                        neue_kategorie = 'Sonstiges'
                                        break #Beendet die Schleife wenn der User eine gültige Eingabe macht
                                    else:
                                        print('Ungültige Eingabe, bitte eine Kategorie von 1-9 wählen')
                            else:
                                print('Ungültiger Typ angegeben. Bitte zuerst Einnahme oder Ausgabe eingeben')
                                break #Beendet die Schleife 
                        if neuer_typ.strip()=='':
                            neuer_typ=row['typ']
                        if neues_datum.strip()=='':
                            neues_datum=row['datum']
                        if neuer_betrag.strip()=='':
                            neuer_betrag= row['betrag']
                        #wenn der User nichts eingibt wird der alte wert übernommen    

                        neue_daten.append({ #fügt neue/bearbeiteten Eintrag zur Liste hinzu
                            'datum': neues_datum,
                            'betrag': neuer_betrag,
                            'typ': neuer_typ,
                            'kategorie': neue_kategorie
                        })
                        bearbeitet= True #setzt Flag auf True
                        continue #Springt zur nächsten Zeile im For-Loop und überspringt die unveränderten Zeile
                neue_daten.append(row) #Fügt die aktuelle Zeile zur Liste hinzu, wenn sie nciht bearbeitet wurde

            with open(DATEI, 'w', newline='') as file: #öffnet CSV im Schreibmodus
                writer = csv.DictWriter(file, fieldnames= ['datum', 'betrag','typ', 'kategorie']) #erstellt den Writer
                writer.writeheader() #schreibt die kopfzeile
                writer.writerows(neue_daten) #schreibt alle bearbeiteten und unveränderten Einträge
                        
            if bearbeitet: #Falls der Eintrag bearbeitet wurde:
                print('\nEintrag wurde bearbeitet')
            else: #Ansonsten:
                print('\n Kein Eintrag wurde bearbeitet oder gefunden')
            break
        else:
            print('Ungültige Eingabe, bitte 1/2 eingeben!')
