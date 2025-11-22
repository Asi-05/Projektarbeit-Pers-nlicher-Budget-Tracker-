from datetime import datetime  
from datei_pruefen import *
import csv 

def datum_eingabe(prompt):
    while True:
        eingabe = input(prompt).strip()
        try:
            datum_obj = datetime.strptime(eingabe, '%d.%m.%Y')
            return datum_obj   # Wichtig: direkt ein datetime-Objekt zurückgeben!
        except ValueError:
            print('Ungültiges Datum! Bitte im Format TT.MM.YYYY eingeben.')