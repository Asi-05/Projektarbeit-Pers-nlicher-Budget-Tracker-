import csv              #importiert CSV Bibliothek aus Python Standardbibliothek

DATEI = 'budget.csv'    #Legt den Dateinamen als Konstante fest (Vorteil-> kann einfacher geändert werden)

def datei_pruefen():    #prüfen, ob die CSV Datei existiert, ansonsten wird diese erstellt
    '''Funktion um CSV Datei zu prüfen'''
    try:
        with open (DATEI, 'x', newline = '') as file:                   #öffnet die Datei im x Modus (erstellt NUR neue Datei, wenn sie nicht bereits existiert)
            writer = csv.writer(file)                                   #erstellt ein CSV Schreibobjekt, Daten können so Kommagetrennt schreiben
            writer.writerow(['datum', 'betrag', 'typ', 'kategorie'])    #schreibt die spalten überschriften in der CSV Datei
    except FileExistsError:                 #falls die Datei schon existiert, tritt dieser Fehler auf (Wird aufgefangen und PASS)
        pass                                #Dann wird einfach nichts gemacht (Datei bleibt bestehen)