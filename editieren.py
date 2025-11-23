from datetime import datetime  
from datei_pruefen import *
from kategorieauswahl import *
from datum_eingabe import *
import csv 

def editieren():
    
    datei_pruefen()
    daten = []
    print('\n1) Eintrag löschen')
    print('2) Eintrag bearbeiten')

    print('x) zurück')

    optionauswahl = input("\nBitte wähle 1 oder 2:")

    if optionauswahl == '1':

        datum = datum_eingabe()
        
        while True: #Betrag abfragen
            try:
                betrag_suche = float(input("Gesuchter Betrag(CHF): "))
                break
            except ValueError:
                print("Bitte gültigen Betrag eingeben!")

        print('Bitte Einnahme oder Ausgabe')

        while True:
            AoE_auswahl = input('\nBitte Einnahme oder Ausgabe angeben: ').strip()

            if AoE_auswahl == 'Einnahme':
                kategorie = kategorieauswahl_einnahme()
                break

            elif AoE_auswahl == 'Ausgabe':
                kategorie = kategorieauswahl_ausgabe()
                break

            else:
                print('Ungültige Eingabe. Bitte "Einnahme" oder "Ausgabe" eingeben.')


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
            print('\nEintrag wurde gelöscht')
        else:
            print('\nKein Eintrag wurde gelöscht oder gefunden')


    elif optionauswahl == '2':
        
        datum = datum_eingabe()
        
        while True: #Betrag abfragen
            try:
                betrag_suche = float(input("Gesuchter Betrag (CHF): "))
                break
            except ValueError:
                print("Bitte gültigen Betrag eingeben!")
            
        print('Einnahme oder Ausgabe')
        
        while True:
            AoE_auswahl = input('\nBitte Einnahme oder Ausgabe angeben:').strip()
            if AoE_auswahl == 'Einnahme':
                kategorie = kategorieauswahl_einnahme()
                break

            elif AoE_auswahl == 'Ausgabe':
                kategorie = kategorieauswahl_ausgabe()
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
                bestaetigung = input('Diesen Eintrag bearbeiten? (Ja/Nein):').lower()
                if bestaetigung=='ja':
                    neuer_typ= input('Einnahme oder Ausgabe:')
                    neuer_betrag= input('Neuer Betrag: ')
                    neues_datum= input('Neues Datum (TT.MM.JJJ):')
                    ziel_typ= neuer_typ if neuer_typ else row['typ']
                    neue_kategorie= row['kategorie']
                    
                 
                    while True:
                        if ziel_typ =='Einnahme':
                            neue_kategorie = kategorieauswahl_einnahme()
                            break

                        elif ziel_typ== 'Ausgabe':
                            neue_kategorie = kategorieauswahl_ausgabe()
                            break

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
            print('\nEintrag wurde bearbeitet')
        else:
            print('\n Kein Eintrag wurde bearbeitet oder gefunden')

    elif optionauswahl == 'x':
        return