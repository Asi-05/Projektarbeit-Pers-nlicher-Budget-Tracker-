# 💰 Personal Budget Planer

Dieses Projekt hat folgende Ziele:
Einen personellen Budgetplaner programmieren
-

## 📝 Analyse

**Problem**

Viele Menschen möchten ihre persönlichen Finanzen besser verwalten, haben aber keine einfache Möglichkeit ihre Einnahmen und Ausgaben zu erfassen und übersichtlich darzustellen. Eine manuelle Nachführung mit Tabellen ist mühsam und fehleranfällig.


**Szenario**

Beispiel: Der Benutzer möchte regelmässig seine Einnahmen und Ausgaben eingeben, diese in Kategorien sortieren und eine Übersicht über seine Finanzen erhalten inklusive Summen und Bilanzen über bestimmte Zeiträume.

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

## ✅ Projekt Anforderungen

1. Interaktive Anwendung (Konsoleneingabe)
2. Datenvalidierung (Eingabeprüfung)
3. Datenverarbeitung (Lesen/Schreiben)

---

### 1. Interaktive Anwendung (Konsoleneingabe) 
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

- **Funktions selektion:** Wenn der Benutzer eine Nummer eingibt prüft das Programm, ob sich die Eingabe innerhalb des gültigen Bereiches befindet :
	```python
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
            print("Vielen Dank, dass du den Budgetplaner verwendet hast. Auf Wiedersehen!")
            break

        else:
            print(" X Ungültige Eingabe, bitte nochmals versuchen.")

	```
Dies lässt nur gültige Zahlen durch, um die gewünschte Funktion auszulösen.

- **CSV Datei validieren:** Beim ausführen jeder Funktion wird geprüft, ob schon eine CSV Datei existiert. Falls Ja wird die Fehlermeldung: FileExistsError übersprungen. Falls keine CSV Datei existiert wird eine neue erstellt mit dem Namen: 'budged.csv'
```python
 DATEI = 'budget.csv' 

def datei_pruefen():    												#prüfen, ob die CSV Datei exestiert, ansonsten wird diese erstellt
    try:
        with open (DATEI, 'x', newline = '') as file:       			#öffnet die Datei im x Modus (erstellt neue Datei, wenn sie nicht existiert)
            writer = csv.writer(file)                      		 		#erstellt ein CSV Schreibobjekt
            writer.writerow(['datum', 'betrag', 'typ', 'kategorie'])    #schreibt die spalten überschriften
    except FileExistsError:            									#falls die Datei schon existiert, tritt dieser Fehler auf
        pass                                							#Dann wird einfach nichts gemacht (Datei bleibt bestehen)
	
```

Diese Prüfungen verhindern Abstürze und leiten den Benutzer dazu an, korrekte Eingaben zu machen, die den Projektrichtlinien beschriebenen Validierungsanforderungen entsprechen.

---

---


### 3. Datenverarbeitung (Lesen/Schreiben)

Die Applikation liest aus einer CSV Datei und schreibt Daten in eine CSV datei.

- **Input file:** `budget.csv` — Enthält die Daten, welche vorhin vom User eingegeben wurden in Zeilen und Spalten `'datum', 'betrag','typ', 'kategorie'`.
	- Beispiel: 
		```
		datum,betrag,typ,kategorie
		01.04.2025,3000.0,Einnahme,Lohn
		01.05.2025,3000.0,Einnahme,Lohn
		25.05.2025,250.0,Einnahme,Sonstiges
		01.06.2025,3000.0,Einnahme,Lohn
		```
	- Beim aufruf der Funktion 'uebersicht_anzeigen.py' wird auf die budget.csv datei zugegriffen, und der Inhalt wird eingelesen, um die entsprechende Übersicht anzuzeigen.

- **Output Funktion:** `uebersicht_anzeigen.py` - Greift auf die CSV Datei zu und zeigt die gewünschte Übersicht im Terminal an. Beispielsweise will der User eine Kategorieübersicht von der Kategorie Lohn.
	- Beispiel:
		```
		Counter    Datum        Betrag       Typ       
		----------------------------------------------------------------------
		1          01.04.2025   3000.0       Einnahme   
		2          01.05.2025   3000.0       Einnahme
  		3          01.06.2025   3000.0       Einnahme     
		```
		- Diese Anzeige dient als Übersicht für den User, um seine Eingaben in einer Übersicht zu sehen. So kann der User gezielt Daten aussuchen und bearbeiten oder löschen mit der `editieren.py` Funktion.
## ⚙️ Implementation

### Technology
- Python 3.13.7
- Umgebung: GitHub Codespaces / Visual Studio Code
- Keine externen Bibliotheken

### 📂 Repository Struktur
```text
.
├─ main/
│  ├─ datei_kontrollieren/				# Logik zur Prüfung der Datei/CSV
│  │  └─ datei_pruefen.py
│  ├─ datum_eingabe/					# Eingabe und Validierung von Datumswerten
│  │  └─ datum_eingabe.py
│  ├─ eingaben_editieren/				# Bearbeiten bestehender Einträge
│  │  └─ editieren.py
│  ├─ einnahmen_ausgaben/				# Hinzufügen von Einnahmen/Ausgaben
│  │  ├─ ausgaben_hinzufuegen.py
│  │  └─ einnahmen_hinzufuegen.py
│  ├─ kategorie_auswahl/				# Auswahl der Kategorie
│  │  └─ kategorieauswahl.py
│  ├─ uebersicht_einnahmen_ausgaben/	# Anzeigen der Übersicht
│  │  └─ uebersicht_anzeigen.py
│  └─ main.py							# Hauptstarter des Programms
│
├─ budget.csv
├─ README.md
├─ .gitignore
└─ .DS_Store

```

### Wie funktioniert das Programm
1. Repository in **GitHub Codespaces** öffnen
2. **Terminal** öffnen
3. Eingeben:
	```bash
 	cd main
 
 und dann 
 
	python3 main.py
	```

### Libraries Used

- `datetime`: Wird verwendet, um Datumsangaben im Programm einzugeben und zu verarbeiten. Zum Beispiel, wenn Einnahmen oder Ausgaben erfasst werden. Ausserdem hilft `datetime` dabei, Übersichten nach Datum anzuzeigen sowie Einträge anhand ihres Datums zu finden und oder zu bearbeiten.
- `csv`: Wird genutzt, um CSV-Dateien zu lesen, schreiben und zu verarbeiten. Wie zum beispiel: `budget.csv`. 


## 👥 Team & Beiträge

| Name       			| Beitrag									   																	   |
|-----------------------|------------------------------------------------------------------------------------------------------------------|
|Asithan Supendran  	|Hauptmenüfunktion, Einnahmefunktion, Aufteilung der funktionen, Erstellung der branches und Aufbau des Codespaces |
|Filmon Samy			|Editierfunktion, Ausgabenfunktion, Löschen Funktion 															   |              
|Janath Balasubramaniam |Kategorie Auswahl Funktion, Übersichtsfunktion, Datumeingabe Funktion 											   |  



## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)

  
