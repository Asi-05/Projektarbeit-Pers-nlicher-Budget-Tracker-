#Titel
print("=== Willkommen zu deinem Budgetplaner ===")

#Funktion für Menü
def start_menu():
    print("\nWas willst du heute machen?")
    print("1) Einnahmen hinzufügen")
    print("2) Ausgaben hinzufügen")
    print("3) Übersicht anzeigen")
    print("4) Edit")
    print("5) Programm beenden")
    
    choice = input("Bitte wähle eine Option (1-4): ")
    return choice

#Hauptprogramm mit Schleife
while True:
    auswahl = start_menu()

    if auswahl == "1":
        print("Einnahmen hinzufügen")
    elif auswahl == "2":
        print("Ausgaben hinzufügen")
    elif auswahl == "3":
        print("Überischt anzeigen")
    elif auswahl == "4":
        print("Edit")
    elif auswahl == "5":
        print("Programm beendet. Auf Wiedersehen!")
        break

    else:
        print(" X Ungültige Eingabe, bitte nochmals versuchen.")


