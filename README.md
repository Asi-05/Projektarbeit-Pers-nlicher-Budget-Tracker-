# 💰 Personal Budget Planer

Dieses Projekt hat folgende Ziele:
-Einen personellen Budgetplaner programmieren
-

## 📝 Analysis

**Problem**
> 🚧 Describe the real-world problem your application solves. (Not HOW, but WHAT)

Viele Menschen möchten ihre persönlichen Finanzen besser verwalten, haben aber keine einfache Möglichkeit ihre Einnahmen und Ausgaben zu erfassen und übersichtlich darzustellen. Eine manuelle Nachführung mit Tabellen ist mühsam und fehleranfällig.


**Scenario**
> 🚧 Describe when and how a user will use your application

Example: Der Benutzer möchte regelmässig seine Einnahmen und Ausgaben eingeben, diese in Kategorien sortieren und eine Übersicht über seine Finanzen erhalten inklusive Summen und Bilanzen über bestimmte Zeiträume.

**User stories:**

1. Als Benutzer möchte ich meine Einnahmen und Ausgaben erfassen, um meine Finanzen zu überwachen.
2. Als Benutzer möchte ich Kategorien zuweisen können (z.B. Miete, Freizeit, Transport)
3. Als Benutzer möchte ich Summen und Bilanzen für bestimmte Zeiträumen abrufen.
4. Als Benutzer möchte ich die Einträge bearbeiten oder löschen können.
5. Als Benutzer möchte ich Bilanze einsehen können.

**Use cases:**
- Betrag erfassen (Einnahmen oder Ausgaben)
- Summen nach Kategorien anzeigen
- Bilanz Anzeigen
- Einträge bearbeiten/löschen
- Programm beenden

## ✅ Project Requirements

1. Interaktive Anwendung (Konsoleneingabe)
2. Datenvalidierung (Eingabeprüfung)
3. Datenverarbeitung (Lesen/Schreiben)

---

### 1. Interaktive Anwendung (Konsoleneingabe)

> 🚧 In this section, document how your project fulfills each criterion.  
---
Die Anwendung interagiert über die Konsole mit dem Benutzer. Benutzer können: 
 1) Einnahmen hinzufügen
 2) Ausgaben hinzufügen
 3) Übersicht anzeigen
 4) Editieren
 5) Programm beenden

---


### 2. Datenvalidierung (Eingabeprüfung)

Die Anwendung validiert alle Benutzereingaben um Datenintegrität und reibungslose Benutzererfahrung zu gewährleisten. Dies ist im main.py und datei_pruefen.py wie folgt implementiert: 

- **Funktions selektion:** Wenn der Benutzer eine Nummer eingibt prüft das Programm, ob die Eingabe innerhalb des gültigen Bereiches ist:
	```python
	while True: 
        auswahl = start_menu() #funktion (start_menu) wird abgerufen, return choice gibt wert an bspw: 3

        if auswahl == "1":
            einnahmen_hinzufuegen()
        elif auswahl == "2":
            ausgaben_hinzufuegen()
        elif auswahl == "3":
            uebersicht_anzeigen()
        elif auswahl == "4":
            editieren()
        elif auswahl == "5":
            print("Vielen Dank, dass du den Budgetplaner verwendet hast. Auf Wiedersehen!")
            break

        else:
            print(" X Ungültige Eingabe, bitte nochmals versuchen.")
	```
	Dies lässt nur gültige Zahlen durch, um die gewünschte Funktion auszulösen.

- **CSV Datei validieren:** Beim ausführen jeder Funktion wird geprüft, ob schon eine CSV Datei existiert. Falls Ja wird die Fehlermeldung: FileExistsError übersprungen. Falls keine CSV Datei existiert wird eine neue erstellt mit dem Namen: 'budged.csv'
```python
 DATEI = 'budget.csv' 

def datei_pruefen():    #prüfen, ob die CSV Datei exestiert, ansonsten wird diese erstellt
    try:
        with open (DATEI, 'x', newline = '') as file:       #öffnet die Datei im x Modus (erstellt neue Datei, wenn sie nicht existiert)
            writer = csv.writer(file)                       #erstellt ein CSV Schreibobjekt
            writer.writerow(['datum', 'betrag', 'typ', 'kategorie'])    #schreibt die spalten überschriften
    except FileExistsError:            #falls die Datei schon existiert, tritt dieser Fehler auf
        pass                                #Dann wird einfach nichts gemacht (Datei bleibt bestehen)
	
```

Diese Prüfungen verhindern Abstürze und leiten den Benutzer dazu an, korrekte Eingaben zu machen, die den Projektrichtlinien beschriebenen Validierungsanforderungen entsprechen.

---

---


### 3. Datenverarbeitung (Lesen/Schreiben)

The application reads and writes data using files:

- **Input file:** `menu.txt` — Contains the pizza menu, one item per line in the format `PizzaName;Size;Price`.
	- Example:
		```
		Margherita;Medium;12.50
		Salami;Large;15.00
		Funghi;Small;9.00
		```
	- The application reads this file at startup to display available pizzas.

- **Output file:** `invoice_001.txt` (and similar) — Generated when an order is completed. Contains a summary of the order, including items, quantities, prices, discounts, and totals.
	- Example:
		```
		Invoice #001
		----------------------
		1x Margherita (Medium)   12.50


		2x Salami (Large)        30.00
		----------------------
		Total:                  42.50
		Discount:                2.50
		Amount Due:             40.00
		```
		- The output file serves as a record for both the user and the pizzeria, ensuring accuracy and transparency.

## ⚙️ Implementation

### Technology
- Python 3.x
- Environment: GitHub Codespaces
- No external libraries

### 📂 Repository Structure
```text
PizzaRP/
├── main.py             # main program logic (console application)
├── menu.txt            # pizza menu (input data file)
├── invoice_001.txt     # example of a generated invoice (output file)
├── docs/               # optional screenshots or project documentation
└── README.md           # project description and milestones
```

### How to Run
> 🚧 Adjust if needed.
1. Open the repository in **GitHub Codespaces**
2. Open the **Terminal**
3. Run:
	```bash
	python3 main.py
	```

### Libraries Used

- `os`: Used for file and path operations, such as checking if the menu file exists and creating new files.
- `glob`: Used to find all invoice files matching a pattern (e.g., `invoice_*.txt`) to determine the next invoice number.

These libraries are part of the Python standard library, so no external installation is required. They were chosen for their simplicity and effectiveness in handling file management tasks in a console application.


## 👥 Team & Beiträge

| Name       			| Beitrag									   |
|-----------------------|----------------------------------------------|
|Asithan Supendran  	|Erstellung vom Hauptmenü, Einnahmefunktion, Aufteilung der funktionen,  
|Filmon Samy			|               
|Janath Balasubramaniam |   



## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)

  
