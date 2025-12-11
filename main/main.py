from einnahmen_ausgaben.ausgaben_hinzufuegen import *               #Stern importiert alle Funktionen von den Funktionsdateien
from datei_kontrollieren.datei_pruefen import *
from datum_eingabe.datum_eingabe import *
from eingaben_editieren.editieren import *
from einnahmen_ausgaben.einnahmen_hinzfuegen import *
from uebersicht_einnahmen_ausgaben.uebersicht_anzeigen import *


print("=== Willkommen zu deinem Budgetplaner ===")

def main():
    """Hauptmenü"""

#Funktion für Menü
    def start_menu():                                               #definiert die Funktoin Start mit Namen start_menu
        print("\nWas willst du heute machen?")
        print("1) Einnahmen hinzufügen")
        print("2) Ausgaben hinzufügen")
        print("3) Übersicht anzeigen")
        print("4) Editieren")
        print("5) Programm beenden")
    
        choice = input("Bitte wähle eine Option (1-5): ")
        # choice ...
        return choice                                               #choice wird gemäss eingabe vom User wiedergegeben



    # Hauptprogramm mit Schleife
    while True: 
        auswahl = start_menu()                                      #funktion (start_menu) wird abgerufen, return choice gibt wert an bspw: 3

        if auswahl == "1":
            einnahmen_hinzufuegen()
        elif auswahl == "2":
            ausgaben_hinzufuegen()
        elif auswahl == "3":
            uebersicht_anzeigen()
        elif auswahl == "4":
            editieren()
        elif auswahl == "5":
            print("\nVielen Dank, dass du den Budgetplaner verwendet hast. Auf Wiedersehen!")
            break

        else:
            print(" X Ungültige Eingabe, bitte nochmals versuchen.")


if __name__ == "__main__":
    main()



