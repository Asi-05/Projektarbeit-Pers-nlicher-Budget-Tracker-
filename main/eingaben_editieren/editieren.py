from datetime import datetime  
from datei_kontrollieren.datei_pruefen import * #importiert die funktion zur Überprüfung/Erstellung der CSV-Datei
from kategorie_auswahl.kategorieauswahl import * #Importiert Auswahl für Kategorie
from datum_eingabe.datum_eingabe import * #importiert funktion datum eingabe mit kontrolle
import csv 

def eintrag_loeschen(daten): #definiert die funktion zur direkten Löschung

        datum = datum_eingabe() #ruft funktion datum eingabe auf
        
        while True: #startet schleife für gültige eingabe
            try:
                betrag_suche = float(input("Gesuchter Betrag(CHF): "))
                break #beendet schleife wenn richtige eingabe
            except ValueError: #fängt fehler an, falls keine gültige Zahl eingegebn wurde
                print("Bitte gültigen Betrag eingeben!")

        print('Bitte Einnahme oder Ausgabe')

        while True: #beginnt neue schleife für gültige eingabe von typ
            AoE = input('\n1)Einnahme | 2)Ausgabe\n Bitte 1 oder 2 angeben: ').strip() #fordert auf typ auswahl mit zahl und strip entfernt Leerzeichen

            if AoE == '1': #wenn Benutzer 1 für einnahme wählt
                AoE_auswahl='Einnahme' #setzt einnahme für sie suche ein
                kategorie = kategorieauswahl_einnahme() #zeigt katogrien für einnahme und fordert eingabe auf und setzt eingabe für kategorie such ein
                break #beendet die schleife bei gültiger eingabe

            elif AoE == '2': #wenn benutzer 2 für ausgabe wählt
                AoE_auswahl='Ausgabe' #setzt Ausgabe als typ ein bei der suche
                kategorie = kategorieauswahl_ausgabe() #zeigt kategorien für ausgaben und verlangt eingabe kategorie und setzt es dann ein für suche
                break #beendet schleife bei gültiger eingabe

            else: #wenn weder 1 oder 2 gewählt wurde 
                print('Ungültige Eingabe. Bitte 1 oder 2 eingeben.')


        with open(DATEI, 'r', newline='') as file: #öffnet die csv datei im lesemodus
            reader = csv.DictReader(file) #erstellt ein reader objekt
            daten= list(reader) #liest ale daten in die liste daten
        
        neue_daten = [] #initialisiert liste für die zu behaltenden einträge

        geloescht= False #flag um zu verfolgen ob ein eintrag gelöscht wird
        for row in daten: #beginnt ein loop um jeden eintrag zu prüfen
            if (float(row['betrag']) == betrag_suche and
                row['typ']== AoE_auswahl and
                row['kategorie']== kategorie and
                row ['datum']== datum): #dieser blockt prüft betrag, typ, kategorie und datum 
                print(f'\nGefundener Eintrag: {row['datum']} | {row['betrag']} | {row['typ']} | {row['kategorie']}')
                print('\n1)Ja | 2)Nein')
                bestaetigung = input('Diesen Eintrag löschen? (1/2):').lower() #fordert bestätigung
                if bestaetigung=='1': #falls user 1 für ja eingibt
                    geloescht=True #setzt lösch frag
                    continue #springt zur nächsten zeile und der eintrag wird nicht zur liste neue_dten hinzugefügt
            neue_daten.append(row) #wenn zeile nicht gelöscht wird zeile zur liste hinzugefügt

        with open(DATEI, 'w', newline='') as file: #öffnet csv datei im schreibmodus
            writer = csv.DictWriter(file, fieldnames= ['datum', 'betrag','typ', 'kategorie']) #definiert spaltenname für writer
            writer.writeheader() #schreibt die spalten überschriften
            writer.writerows(neue_daten) #schreibt die behaltenen daten zurück in die datei
        
        if geloescht: #falls gelöscht
            print('\nEintrag wurde gelöscht')
        else: #wenn user nicht löscht oder eine andere eingabe macht
            print('\nKein Eintrag wurde gelöscht oder gefunden')



def editieren(): #definiert funktion editieren
    
    datei_pruefen() #stellt sicher dass die csv datei existiert
    daten = [] #für fehlervermeidung
    print('\n1) Eintrag löschen')
    print('2) Eintrag bearbeiten')

    print('x) zurück')

    optionauswahl = input("\nBitte wähle 1 oder 2:") #user wählt aus ob er löschen oder bearbeiten will

    if optionauswahl == '1': #falls user löschen wählt
        eintrag_loeschen(daten) #ruft funktion löschen auf
    elif optionauswahl == '2': #falls user beabreiten will
        
        datum = datum_eingabe() #verlangt datum eingabe, prüft eingabe und speichert es in datum für spätere suche
        
        while True: #startet abfrage nach betrag und fängt ungütlige beträge ab mit try und except
            try:
                betrag_suche = float(input("Gesuchter Betrag (CHF): "))
                break
            except ValueError:
                print("Bitte gültigen Betrag eingeben!")
            
        print('Einnahme oder Ausgabe')
        
        while True: #startet gültige eingabe für einnahme oder ausgabe
            AoE = input('\n1)Einnahme | 2)Ausgabe\n Bitte 1 oder 2 angeben: ').strip()

            if AoE == '1': #falls user einnahme wählt
                AoE_auswahl='Einnahme' #setzt einnahme als typ ein für die suche
                kategorie = kategorieauswahl_einnahme() #zeigt ihm alle kategorien für einnahmen verlangt eingabe vom user und speichert die gewählte kategorie für spätere suche
                break #beendet die schleife bei gültiger eingabe

            elif AoE == '2': #falls user ausgabe wählt
                AoE_auswahl='Ausgabe' #setzt augabe als typ ein und speichert es für spätere suche
                kategorie = kategorieauswahl_ausgabe() #zeigt kategorien für ausgabe und verlangt input vom user für spätere suche
                break #beendet die schleife bei gültiger eingabe

            else:
                print('Ungültige Eingabe. Bitte 1 oder 2 eingeben.') #bei ungültiger eingabe ob einnahme oder ausgabe erscheint diese meldung und man muss erneut eingeben

        with open(DATEI, 'r', newline='') as file: #lädt alle daten aus der csv
            reader = csv.DictReader(file)#erstellt ein reader objekt
            daten= list(reader)   #liest ale daten in die liste daten
        neue_daten = [] #liste für neue daten
        bearbeitet= False #flag für beabreitung

        for row in daten: #loop durch alle einträge
            if (
                round(float(row['betrag']),2)== round(betrag_suche,2) and #betragsüberprüfung
                row['typ']==AoE_auswahl.strip() and
                row['kategorie']== kategorie and
                row ['datum']== datum #sucht mit den eingaben vom user
                
            ):
                print(f'\nGefundener Eintrag: {row['datum']} | {row['betrag']} | {row['typ']} | {row['kategorie']}') #print falls eintrag gefunden
                print('\n1)Ja | 2)Nein')
                bestaetigung = input('Diesen Eintrag bearbeiten? (1/2):').strip() #fragt user ob er wirklich bearbeiten will
                if bestaetigung== '1': #falls user 1 für ja sagt
                    while True: #verlangt gültige eingabe
                        neuer_typ_wahl=input('Neuer Typ (1=Einnahme | 2=Ausgabe):')
                        if neuer_typ_wahl=='1':
                            neuer_typ='Einnahme'
                            break #sobald ein gültiger typ gewählt wurde gehts weiter
                        elif neuer_typ_wahl=='2':
                            neuer_typ='Ausgabe'
                            break #sobald ein gültiger typ gewählt wurde gehts weiter
                        elif neuer_typ_wahl=='':
                            neuer_typ=''
                            break #falls user keine eingabe macht wird das alte übernommen
                        else:
                            print('Ungültige Eingabe! Bitte 1 oder 2 wählen.')
                    neuer_betrag= input('Neuer Betrag: ').strip() #user gibt neuen betrag ein
                    neues_datum= datum_eingabe() #neues datum 
                    ziel_typ= neuer_typ if neuer_typ else row['typ'] #bestimmt den typ, der für die kategorie wahl genutzt wird
                    neue_kategorie= row['kategorie'] #setzt alte kategorie als standard
                    
                 
                    while True: #ruft kategorie auswahl basierend auf dem zieltyp auf
                        if ziel_typ =='Einnahme':
                            neue_kategorie = kategorieauswahl_einnahme()
                            break #beendet bei gültiger eingabe

                        elif ziel_typ== 'Ausgabe':
                            neue_kategorie = kategorieauswahl_ausgabe()
                            break #beendet bei gültiger eingabe

                        else:
                            print('Ungültiger Typ angegeben. Bitte zuerst Einnahme oder Ausgabe eingeben')
                            break
                    if neuer_typ.strip()=='':
                        neuer_typ=row['typ']
                    if neues_datum.strip()=='':
                        neues_datum=row['datum']
                    if neuer_betrag.strip()=='':
                        neuer_betrag= row['betrag']
                        #falls nichts vom user eingegeben wird,w ird der alte wert übernommen  

                    neue_daten.append({ #fügt neuen/bearbeiteten eintrag zur liste hinzu
                        'datum': neues_datum,
                        'betrag': neuer_betrag,
                        'typ': neuer_typ,
                        'kategorie': neue_kategorie
                    })
                    bearbeitet= True #setzt flag auf true
                    continue #springt zum nächsten eintrag und kopiert den alten unbearbeiteten eintrag nicht
            neue_daten.append(row) #fügt zeilen die nicht beabreiten wurden zur aktuellen liste hinzu

        with open(DATEI, 'w', newline='') as file: #öffnet csv im schreibmodus
            writer = csv.DictWriter(file, fieldnames= ['datum', 'betrag','typ', 'kategorie'])#definiert spaltenname für writer
            writer.writeheader() #schreibt die spalten überschriften
            writer.writerows(neue_daten) #schreibt alle bearbeiteten und unveränderten einträge zurück
                    
        if bearbeitet: #falls bearbeitet
            print('\nEintrag wurde bearbeitet')
        else:
            print('\nKein Eintrag wurde bearbeitet oder gefunden')

    elif optionauswahl == 'x':
        return
    else:
        print('Ungültige Eingabe, bitte 1/2 eingeben!')