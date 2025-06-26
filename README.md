# Musik-Aleatorik

Ein **Stochastischer Musik-Generator**, der mithilfe von **Webcam-basierter Zufälligkeit** und **XML-Konfiguration** aleatorische Musikstücke komponiert und als Noten (PDF) und Audio (MP3) exportiert.

## 🎵 Wie funktioniert es?

**Einfache 4-Schritte-Erklärung:**

1. **Konfiguration lesen**: Das Programm liest die `config/config.xml` Datei, die alle musikalischen Parameter enthält (Instrumente, Rhythmen, Dynamik, Taktanzahl-Bereiche).

2. **Zufälligkeit aus Webcam**: Die Kamera nimmt kontinuierlich Bilder auf und nutzt winzige Bewegungen und Kamera-Rauschen zur Generierung echter Zufallszahlen.

3. **Musikkomposition**: Basierend auf der XML-Konfiguration und den Webcam-Zufallszahlen wird automatisch ein komplettes Musikstück komponiert (Noten, Rhythmen, Dynamik).

4. **Export in 4 Formaten**: Das fertige Werk wird automatisch exportiert als:
   - **PDF** (Noten zum Musizieren)
   - **MP3** (Audio zum Anhören)
   - **MIDI** (für Musiksoftware)
   - **MusicXML** (für andere Notenprogramme)



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


## ⚙️ Konfiguration

Die Datei `config/config.xml` enthält alle musikalischen Parameter:

#### Taktanzahl-Bereiche:
```xml
<num_measures>30-40</num_measures>  <!-- Zufällig zwischen 30 und 40 Takten -->
<!-- oder -->
<num_measures>20</num_measures>     <!-- Feste Anzahl von 20 Takten -->
```



## 📁 Output & Dateiformate

Jede Komposition erstellt automatisch einen eigenen Ordner in `output/` mit **4 verschiedenen Dateiformaten**:

```
output/
├── streichtrio_aleatorisch/
│   ├── streichtrio_aleatorisch.musicxml    # Für andere Notenprogramme
│   ├── streichtrio_aleatorisch.pdf         # Professionell gesetzte Noten
│   ├── streichtrio_aleatorisch.mid         # Für weitere Bearbeitung
│   └── streichtrio_aleatorisch.mp3         # Audio-Wiedergabe
└── weitere_kompositionen/
```

**Was du erhältst:**
- **PDF**: Druckfertige Noten zum Musizieren
- **MP3**: Sofort anhörbare Audio-Version  
- **MIDI**: Für DAWs und Musiksoftware


---
*Lass die Webcam entscheiden, wie deine Musik klingt! 🎲🎵*
