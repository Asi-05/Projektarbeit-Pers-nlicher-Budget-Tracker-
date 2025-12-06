from datetime import datetime  
from datei_kontrollieren.datei_pruefen import *
import csv 

def datum_eingabe():
    '''Funktion um datum einzugeben''' 
    while True:  
        datum_eingabe = input('Datum (DD. MM. YYYY): ').strip()         #fragt das Datum ab und entfernt die leerzeichen
        try:                                                            
            datum_obj = datetime.strptime(datum_eingabe, '%d.%m.%Y')    #prüfen ob eingabe Format korrekt ist
            datum = datum_obj.strftime('%d.%m.%Y')                      #formatiert das datum einheitlich für die csv datei 
            return datum                                            
    
        except ValueError:                                              #falls das datum ungültig ist
            print('Ungültiges Datum! Bitte im Format TT.MM.YYYY eingeben.')


def datum_eingabe_uerbesichtanzeigen(prompt):
    while True:
        eingabe = input(prompt).strip()
        try:
            datum_obj = datetime.strptime(eingabe, '%d.%m.%Y')
            return datum_obj                                            #Wichtig: direkt ein datetime-Objekt zurückgeben!
        except ValueError:
            print('Ungültiges Datum! Bitte im Format TT.MM.YYYY eingeben.')

