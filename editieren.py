from datetime import datetime  
from datei_pruefen import *
from datum_eingabe import *
import csv 

def editieren():
    
    datei_pruefen()
    daten = []
    print('\n1) Eintrag löschen')
    print('2) Eintrag bearbeiten')

    optionauswahl = input("\nBitte wähle 1 oder 2:")

    if optionauswahl == '1':

        datum = datum_eingabe()
        
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
                bestaetigung = input('Diesen Eintrag bearbeiten? (Ja/Nein):').lower()
                if bestaetigung=='ja':
                    neuer_typ= input('Einnahme oder Ausgabe:')
                    neuer_betrag= input('Neuer Betrag: ')
                    neues_datum= input('Neues Datum (TT.MM.JJJ):')
                    ziel_typ= neuer_typ if neuer_typ else row['typ']
                    neue_kategorie= row['kategorie']
                    
                 
                    while True:
                        if ziel_typ =='Einnahme':
                            print('\n1) Lohn')
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
            print('\nEintrag wurde bearbeitet')
        else:
            print('\n Kein Eintrag wurde bearbeitet oder gefunden')
