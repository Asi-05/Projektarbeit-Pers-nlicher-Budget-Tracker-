import csv 

DATEI = 'budget.csv' 

def datei_pruefen():    #prüfen, ob die CSV Datei existiert, ansonsten wird diese erstellt
    '''Funktion um CSV Datei zu prüfen'''
    try:
        with open (DATEI, 'x', newline = '') as file:                   #öffnet die Datei im x Modus (erstellt neue Datei, wenn sie nicht existiert)
            writer = csv.writer(file)                                   #erstellt ein CSV Schreibobjekt
            writer.writerow(['datum', 'betrag', 'typ', 'kategorie'])    #schreibt die spalten überschriften
    except FileExistsError:            #falls die Datei schon existiert, tritt dieser Fehler auf
        pass                                #Dann wird einfach nichts gemacht (Datei bleibt bestehen)