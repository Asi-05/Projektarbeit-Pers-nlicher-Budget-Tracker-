import csv                                                                 #importiert CSV Bibliothek aus Python Standardbibliothek

#Legt den Dateinamen als Konstante fest (Vorteil-> kann einfacher geändert werden)
DATEI = 'budget.csv'

#prüfen, ob die CSV Datei existiert, ansonsten wird diese erstellt
def datei_pruefen():
    '''Funktion um CSV Datei zu prüfen'''
    try:
        with open (DATEI, 'x', newline = '') as file:                   #öffnet die Datei im x Modus (erstellt NUR neue Datei, wenn sie nicht bereits existiert), newline = '' verhindert, dass leere Zeilen in der CSV datei
            writer = csv.writer(file)                                   #erstellt ein CSV Schreibobjekt, Daten können so Kommagetrennt geschrieben werden --> (passiert automatisch)
            writer.writerow(['datum', 'betrag', 'typ', 'kategorie'])    #schreibt die spalten überschriften in der CSV Datei
    except FileExistsError:                                             #falls die Datei schon existiert, tritt dieser Fehler auf (Wird aufgefangen und PASS)
        pass                                                            #Dann wird einfach nichts gemacht (Datei bleibt bestehen)