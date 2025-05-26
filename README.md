🧠 Über das Collatz Problem
"Nimm eine beliebige natürliche Zahl.
Wenn sie gerade ist, teile sie durch 2.
Wenn sie ungerade ist, multipliziere sie mit 3 und addiere 1.
Wiederhole diesen Vorgang und du wirst irgendwann bei 1 ankommen."

Obwohl dies für alle getesteten Zahlen zu stimmen scheint, ist es nicht bewiesen – ein großes offenes Problem der Mathematik!
# 🔢 Collatz Analyse & Visualisierung (Python)
Dieses Python-Projekt berechnet das 3n+1 Problem (auch bekannt als Collatz Folge)

## 🚀 Funktionen
- Berechnung Collatz Folge für beliebige Startzahl
- Ausgabe jeder Zahl der Folge **untereinander**
- Anzeige:
  - Gesamtanzahl Schritte
  - Anzahl "geteilt durch 2"-Operationen
  - Anzahl "×3 + 1"-Operationen
- **Graphische Darstellung** der Folge per Diagramm

## 🖼️ Beispielausgabe
Collatz Folge: <br>
27 <br>
82 <br>
41 <br>
...

Anfangszahl: 27 <br>
Anzahl Schritte: 111 <br>
Teilungen durch 2: 70 <br>
×3 + 1 Schritte: 41 <br>

## 📊 Diagramm Ausgabee
Programm zeigt ein Liniendiagramm mit Verlauf der Folge der Schritte.

## 🧑‍💻 Installation
```bash
git clone https://github.com/MIGZnumberONE/collatz-analyse.git
cd collatz-analyse
pip install matplotlib
```

## ▶️ Nutzung <br>
python collatz.py
