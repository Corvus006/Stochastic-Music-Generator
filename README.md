# Musik-Aleatorik

Ein **Stochastischer Musik-Generator**, der mithilfe von **Webcam-basierter Zufälligkeit** und **XML-Konfiguration** aleatorische Musikstücke komponiert und als Noten (PDF) und Audio (MP3) exportiert.

## 🎼 Was ist Aleatorische Musik?

**Aleatorische Musik** (von lat. *alea* = Würfel) ist Musik, die durch **Zufall** komponiert wird. Unser Generator nutzt die **Webcam** als Zufallsquelle für echte Unvorhersagbarkeit in der Komposition.

## 🎯 Features

- **Webcam-Zufallsgenerator**: Nutzt Kamerabilder für echte Zufälligkeit
- **XML-Konfiguration**: Flexible Einstellung von Instrumenten, Rhythmen, Dynamik und Taktanzahl
- **Ensemble-Unterstützung**: Streichtrio, Holzbläserquintett, Klavier Solo, etc.
- **Intelligente Instrumentenerkennung**: Fuzzy-Matching und automatische Fallbacks
- **Konfigurierbare Taktanzahl**: Definiere Bereiche (z.B. 30-40 Takte) in der XML
- **Automatischer Export**: PDF-Noten und MP3-Audio
- **Music21-Integration**: Professionelle Musiknotation
- **MuseScore-Kompatibilität**: Hochwertige PDF- und Audio-Ausgabe

## 📁 Projektstruktur

```
Musik-Aleatorik/
├── aleatoric/
│   ├── __init__.py
│   ├── stochastic_composer.py    # Hauptkomponist mit intelligentem Instrument-Mapping
│   ├── score_exporter.py         # PDF/MP3 Export
│   ├── custom_random.py          # Webcam-Zufallsgenerator mit Pool-System
│   └── config_parser.py          # XML-Konfiguration mit Taktanzahl-Bereichen
├── config/
│   └── config.xml                # Musik-Einstellungen inkl. Taktanzahl-Bereiche
├── output/                       # Generierte Dateien
├── main.py                       # Hauptprogramm
├── requirements.txt              # Python-Abhängigkeiten
└── README.md
```

## 🚀 Installation - Schritt für Schritt 

### Schritt 1: Python installieren

**Python** ist die Programmiersprache, die unser Musik-Generator verwendet.

#### Windows:
1. Gehe auf [python.org/downloads](https://www.python.org/downloads/)
2. Lade die neueste Python-Version herunter (mind. 3.8)
3. **Wichtig**: Bei der Installation **"Add Python to PATH"** ankreuzen!
4. Installiere Python mit den Standard-Einstellungen

#### macOS:
```bash
# Option 1: Von python.org herunterladen (einfacher)
# Gehe auf python.org/downloads und lade die macOS-Version herunter

# Option 2: Mit Homebrew (falls installiert)
brew install python
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

#### Linux (Arch/Manjaro):
```bash
sudo pacman -S python python-pip
```

### Schritt 2: Python testen

Öffne ein **Terminal** (Linux/Mac) oder die **Eingabeaufforderung** (Windows):

```bash
python --version
# Sollte zeigen: Python 3.8.x oder höher

# Falls "python" nicht funktioniert, versuche:
python3 --version
```

### Schritt 3: Virtuelles Environment erstellen

Ein **virtuelles Environment** ist wie ein separater Bereich für unser Musik-Projekt, damit es nicht mit anderen Python-Programmen interferiert.

#### Projekt herunterladen:
```bash
git clone [repository-url]
cd Musik-Aleatorik
```

#### Virtual Environment erstellen:

**Windows:**
```cmd
# Environment erstellen
python -m venv musik_env

# Environment aktivieren
musik_env\Scripts\activate

# Du solltest jetzt "(musik_env)" vor deinem Prompt sehen
```

**Linux/macOS:**
```bash
# Environment erstellen
python3 -m venv musik_env

# Environment aktivieren
source musik_env/bin/activate

# Du solltest jetzt "(musik_env)" vor deinem Prompt sehen
```

### Schritt 4: Python-Pakete installieren

Mit aktiviertem Virtual Environment:

```bash
# Alle benötigten Pakete installieren
pip install -r requirements.txt

# Falls das nicht funktioniert, einzeln installieren:
pip install music21 opencv-python numpy
```

### Schritt 5: MuseScore installieren (für PDF/MP3 Export)

**MuseScore** verwandelt unsere Musik-Daten in schöne PDF-Noten und MP3-Audio.

#### Windows:
1. Gehe auf [musescore.org](https://musescore.org)
2. Lade MuseScore 4 herunter und installiere es
3. Starte MuseScore einmal, um sicherzustellen, dass es funktioniert

#### macOS:
```bash
# Mit Homebrew
brew install musescore

# Oder von musescore.org herunterladen
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install musescore3
# oder für neuere Version:
sudo snap install musescore
```

#### Linux (Arch/Manjaro):
```bash
sudo pacman -S musescore
```

### Schritt 6: Webcam anschließen

- Stelle sicher, dass eine **Webcam** angeschlossen ist
- Die meisten Laptops haben bereits eine integrierte Webcam
- USB-Webcams funktionieren ebenfalls

### Schritt 7: Erste Musik generieren!

```bash
# Virtual Environment aktivieren (falls nicht bereits aktiv)
# Windows: musik_env\Scripts\activate
# Linux/Mac: source musik_env/bin/activate

# Musik generieren
python main.py
```

## 📋 Requirements (Automatisch installiert)

```
music21>=8.1.0
opencv-python>=4.8.0
numpy>=1.24.0
```

## 🔄 Virtual Environment - Wichtige Befehle

### Environment aktivieren:
**Jedes Mal, wenn du das Projekt verwendest, musst du das Virtual Environment aktivieren:**

**Windows:**
```cmd
cd Musik-Aleatorik
musik_env\Scripts\activate
```

**Linux/macOS:**
```bash
cd Musik-Aleatorik
source musik_env/bin/activate
```

### Environment deaktivieren:
```bash
deactivate
```

### Prüfen, ob Environment aktiv ist:
- Du siehst `(musik_env)` vor deinem Terminal-Prompt
- Oder teste: `which python` (sollte auf das venv zeigen)

## 🎵 Verwendung

### Einfache Nutzung
```bash
# Stelle sicher, dass Virtual Environment aktiv ist!
# Du solltest (musik_env) in deinem Terminal sehen

python main.py
```

Das Programm generiert automatisch:
1. **Streichtrio** (zufällige Taktanzahl aus Config-Bereich)
2. **Zufälliges Ensemble** (zufällige Taktanzahl aus Config-Bereich)
3. **Klavierstück** (zufällige Taktanzahl aus Config-Bereich)

### Programmatische Nutzung

```python
from aleatoric.stochastic_composer import create_multi_voice_score, create_random_score
from aleatoric.score_exporter import generate_pdf_and_mp3

# Automatische Taktanzahl aus XML-Config (z.B. 30-40 Takte)
score = create_multi_voice_score("Streichtrio", title="Mein aleatorisches Streichtrio")
generate_pdf_and_mp3(score, "mein_streichtrio")

# Spezifische Taktanzahl (überschreibt Config)
score = create_multi_voice_score("Streichtrio", 16, "Kurzes Streichtrio")
generate_pdf_and_mp3(score, "kurzes_streichtrio")

# Komplett zufällig (Ensemble UND Taktanzahl aus Config)
random_score = create_random_score()
generate_pdf_and_mp3(random_score, "zufallskomposition")

# Verschiedene Ensembles mit Config-Taktanzahl
piano_score = create_multi_voice_score("Klavier Solo", title="Aleatorisches Klavierstück")
quintet_score = create_multi_voice_score("Holzbläserquintett", title="Bläserquintett")
```

## ⚙️ Konfiguration

Die Datei `config/config.xml` enthält alle musikalischen Parameter:

### Neue Features in der XML-Konfiguration:

#### Taktanzahl-Bereiche:
```xml
<num_measures>30-40</num_measures>  <!-- Zufällig zwischen 30 und 40 Takten -->
<!-- oder -->
<num_measures>20</num_measures>     <!-- Feste Anzahl von 20 Takten -->
```

### Verfügbare Ensembles:
- **Streichtrio**: Violine, Viola, Cello
- **Holzbläserquintett**: Flöte, Oboe, Klarinette, Fagott, Horn
- **Klavier Solo**: Soloklavier
- **Harfe Solo**: Soloharfe
- **Kammermusik**: Klarinette + Klavier, Flöte + Klavier, Violine + Klavier

### Musikalische Parameter:
- **Rhythmen**: 1/1, 1/2, 1/4, 1/8, 1/16
- **Dynamik**: pp, p, mp, mf, f, ff
- **Artikulation**: legato, staccato, accent, tenuto, none
- **Taktanzahl**: Konfigurierbare Bereiche (z.B. 30-40)

### Vollständige Beispiel-Konfiguration:
```xml
<aleatoricMusic>
  <num_measures>25-35</num_measures>
  
  <rhythms>
    <rhythm>1/1</rhythm>
    <rhythm>1/2</rhythm>
    <rhythm>1/4</rhythm>
    <rhythm>1/8</rhythm>
    <rhythm>1/16</rhythm>
  </rhythms>

  <dynamics>
    <dynamic>pp</dynamic>
    <dynamic>p</dynamic>
    <dynamic>mp</dynamic>
    <dynamic>mf</dynamic>
    <dynamic>f</dynamic>
    <dynamic>ff</dynamic>
  </dynamics>

  <articulations>
    <articulation>legato</articulation>
    <articulation>staccato</articulation>
    <articulation>accent</articulation>
    <articulation>tenuto</articulation>
    <articulation>none</articulation>
  </articulations>

  <instrumentations>
    <ensemble name="Mein Trio">
      <instrument name="Violine" range="G3-E7" maxSimultaneousNotes="2">
        Violinbeschreibung
      </instrument>
      <instrument name="Klavier" range="A0-C8" maxSimultaneousNotes="10">
        Klavierbeschreibung
      </instrument>
    </ensemble>
  </instrumentations>
</aleatoricMusic>
```

## 🎲 Intelligente Instrumentenerkennung

Das System erkennt Instrumente mit mehreren fortschrittlichen Methoden:

### 1. Direktes Mapping (Deutsch/Englisch):
```python
"violine" → Violin()
"klavier" → Piano()
"flöte" → Flute()
"cello" → Violoncello()
```

### 2. Fuzzy String Matching:
```python
"viollin" → "violine" → Violin()  # Tippfehler-Korrektur
"klarnet" → "klarinette" → Clarinet()  # Abkürzungen
```

### 3. Kategorie-basierte Fallbacks:
```python
"Holzbläser" → Flute()
"Streicher" → Violin()
"Tasteninstrument" → Piano()
```

### 4. Config-basierte Fallbacks:
Nutzt den Tonbereich aus der XML zur automatischen Instrumentenwahl:
- Sehr tief (unter E2) → Kontrabass
- Tief (unter G3) → Cello
- Mittel (unter F4) → Viola
- Hoch → Violine

## 🎲 Wie funktioniert der Webcam-Zufallsgenerator? - Einfach erklärt

**Grundprinzip in 10 Sätzen:**

1. Die **Webcam** macht kontinuierlich Fotos deines Gesichts oder deiner Umgebung.

2. Der Computer **vergleicht** jedes neue Bild mit dem vorherigen Bild und sucht nach Unterschieden.

3. Selbst wenn du stillhältst, gibt es **winzige Bewegungen** (Atmung, Augenblinzeln) und elektronisches **Kamera-Rauschen**.

4. Diese minimalen **Bildveränderungen** werden in Zahlen umgewandelt - jeder Pixel hat einen Helligkeitswert.

5. Ein **mathematischer Hash-Algorithmus** (SHA256) verwandelt diese Bilddaten in eine scheinbar zufällige Zahlenfolge.

6. Das Besondere: Schon die **kleinste Änderung** im Bild führt zu einer völlig anderen Zufallszahl.

7. Dadurch entstehen **50-100 Zufallszahlen** auf einmal, die in einem Pool gespeichert werden.

8. Wenn dein Musikprogramm eine Zufallszahl braucht (z.B. für eine Note), wird eine aus diesem **Pool** genommen.

9. Das System nutzt also die **physikalische Unvorhersagbarkeit** der realen Welt statt computergenerierter Pseudo-Zufälle.

10. **Resultat**: Deine Musik wird durch echte, physikalische Zufälligkeit aus der Umgebung komponiert - jedes Stück ist dadurch wirklich einzigartig!

**Kurz gesagt:** Webcam → Bildveränderungen → Hash-Mathematik → Echte Zufallszahlen → Einzigartige Musik! 🎵

```python
# Beispiel für Webcam-Random-Nutzung
from aleatoric.custom_random import get_random_number, initialize_random_generator, cleanup_random_generator

# Einmal initialisieren
initialize_random_generator()

# Viele schnelle Abfragen
note_pitch = get_random_number(60, 84)  # C4 bis C6
rhythm_choice = get_random_number(0, 4)  # 5 Rhythmus-Optionen

# Am Ende aufräumen
cleanup_random_generator()
```

## 📁 Output-Struktur

Jede Komposition erstellt einen eigenen Ordner in `output/`:

```
output/
├── streichtrio_aleatorisch/
│   ├── streichtrio_aleatorisch.musicxml
│   ├── streichtrio_aleatorisch.pdf
│   ├── streichtrio_aleatorisch.mid
│   └── streichtrio_aleatorisch.mp3
├── vollstaendig_aleatorisch/
│   └── ...
└── klavier_aleatorisch/
    └── ...
```

## 🎼 Beispiel-Ausgabe

Nach dem Ausführen erhältst du:
- **PDF**: Professionell gesetzte Noten
- **MP3**: Audio-Wiedergabe des Stücks
- **MIDI**: Für weitere Bearbeitung
- **MusicXML**: Für Import in andere Notenprogramme


## 🔧 Erweiterte Nutzung

### Taktanzahl-Konfiguration
```xml
<!-- Verschiedene Bereiche für verschiedene Stimmungen -->
<num_measures>8-12</num_measures>   <!-- Kurze Miniaturen -->
<num_measures>20-30</num_measures>  <!-- Mittlere Länge -->
<num_measures>50-80</num_measures>  <!-- Ausführliche Stücke -->
<num_measures>16</num_measures>     <!-- Feste Anzahl -->
```

### Eigene Ensembles definieren
```xml
<ensemble name="Mein Jazz-Trio">
  <instrument name="Saxophon" range="Bb3-F#6" maxSimultaneousNotes="1">
    Alt-Saxophon für Jazz-Improvisationen
  </instrument>
  <instrument name="Klavier" range="A0-C8" maxSimultaneousNotes="6">
    Jazz-Piano mit Akkorden
  </instrument>
  <instrument name="Kontrabass" range="E1-G4" maxSimultaneousNotes="1">
    Walking Bass
  </instrument>
</ensemble>
```

### Webcam-Session manuell steuern
```python
from aleatoric.custom_random import webcam_random_session

with webcam_random_session() as generator:
    generator.generate_random_pool(100)  # 100 Zufallszahlen vorher generieren
    for i in range(50):
        note = generator.get_random_from_pool(60, 72)
        print(f"Note {i}: {note}")
```

### Verschiedene Kompositionslängen
```python
# Nutzt Config-Bereich (z.B. 30-40 Takte)
auto_score = create_multi_voice_score("Holzbläserquintett")

# Überschreibt Config mit spezifischer Länge
short_score = create_multi_voice_score("Klavier Solo", 8, "Miniatur")
long_score = create_multi_voice_score("Streichtrio", 100, "Ausführliche Komposition")
```

## 🐛 Troubleshooting - Häufige Probleme

### "python ist kein erkannter Befehl" (Windows)
```cmd
# Versuche stattdessen:
python3 main.py

# Oder Python neu installieren mit "Add to PATH" Option
```

### Virtual Environment aktiviert sich nicht
```bash
# Windows: Stelle sicher, dass du in PowerShell oder CMD bist
musik_env\Scripts\activate.bat

# Linux/Mac: Prüfe den Pfad
ls musik_env/bin/activate
source musik_env/bin/activate
```

### Webcam-Probleme
```bash
# Linux: Webcam testen
ls /dev/video*
v4l2-ctl --list-devices

# Webcam-Berechtigung
sudo usermod -a -G video $USER

# Neustart nach Berechtigung
```

### MuseScore nicht gefunden
```bash
# MuseScore-Pfad prüfen
which musescore3
whereis musescore

# Alternative Installation
snap install musescore
```

### Fehlende Python-Module
```bash
# Virtual Environment aktivieren, dann:
pip install --upgrade music21 opencv-python numpy

# Falls pip nicht funktioniert:
python -m pip install music21 opencv-python numpy
```

### "Keine Berechtigung" Fehler (Linux/Mac)
```bash
# Python-Pakete für Benutzer installieren:
pip install --user music21 opencv-python numpy
```

### XML-Konfigurationsfehler
```bash
# Prüfe XML-Syntax
python -c "import xml.etree.ElementTree as ET; ET.parse('config/config.xml')"

# Beispiel für gültige num_measures:
# <num_measures>30-40</num_measures>  ✓
# <num_measures>25</num_measures>     ✓
# <num_measures>10-5</num_measures>   ✗ (Min > Max)
```
---

*Lass die Webcam entscheiden, wie deine Musik klingt! 🎲🎵*
