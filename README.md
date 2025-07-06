# Stochastic Music Generator

A **Stochastic Music Generator** that uses **webcam-based randomness** and **XML configuration** to compose aleatoric musical pieces and export them as sheet music (PDF) and audio (MP3).

## 🎵 How does it work?

**Simple 4-step explanation:**

1. **Configuration reading**: The program reads the `config/config.xml` file, which contains all musical parameters (instruments, rhythms, dynamics, measure count ranges).

2. **Randomness from webcam**: The camera continuously captures images and uses tiny movements and camera noise to generate true random numbers.

3. **Music composition**: Based on the XML configuration and webcam random numbers, a complete musical piece is automatically composed (notes, rhythms, dynamics).

4. **Export in 4 formats**: The finished work is automatically exported as:
   - **PDF** (sheet music for playing)
   - **MP3** (audio for listening)
   - **MIDI** (for music software)
   - **MusicXML** (for other notation programs)



## 📁 Project Structure

```
Music-Aleatoric/
├── aleatoric/
│   ├── __init__.py
│   ├── stochastic_composer.py    # Main composer with intelligent instrument mapping
│   ├── score_exporter.py         # PDF/MP3 export
│   ├── custom_random.py          # Webcam random generator with pool system
│   └── config_parser.py          # XML configuration with measure count ranges
├── config/
│   └── config.xml                # Music settings including measure count ranges
├── output/                       # Generated files
├── main.py                       # Main program
├── requirements.txt              # Python dependencies
└── README.md
```

## 🚀 Installation - Step by Step

### Prerequisites: Git and Terminal Access

Before we start, you'll need **Git** (to download the project) and know how to open a **Terminal/Command Prompt**.

#### Installing Git

**Git** is a tool that lets you download and manage code projects from the internet.

##### Windows:
1. Go to [git-scm.com/download/win](https://git-scm.com/download/win)
2. Download and install Git for Windows
3. During installation, accept the default settings
4. This also installs "Git Bash" which provides a Unix-like terminal

##### macOS:
```bash
# Option 1: Download from git-scm.com (easier)
# Go to git-scm.com/download/mac and download the installer

# Option 2: With Homebrew (if installed)
brew install git

# Option 3: Git might already be installed, test with:
git --version
```

##### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install git
```

##### Linux (Arch/Manjaro):
```bash
sudo pacman -S git
```

#### How to Open Terminal/Command Prompt

You'll need to use the **terminal** to run commands. Here's how to open it:

##### Windows:
- **Method 1**: Press `Windows + R`, type `cmd`, press Enter
- **Method 2**: Press `Windows + X`, select "Command Prompt" or "PowerShell"
- **Method 3**: Search for "Command Prompt" in the Start menu
- **Method 4**: Right-click in a folder while holding Shift, select "Open command window here"
- **Method 5**: Use "Git Bash" (installed with Git) for a Unix-like experience

##### macOS:
- **Method 1**: Press `Cmd + Space`, type "Terminal", press Enter
- **Method 2**: Go to Applications → Utilities → Terminal
- **Method 3**: Press `Cmd + Space`, type "iTerm" if you have iTerm2 installed

##### Linux:
- **Method 1**: Press `Ctrl + Alt + T`
- **Method 2**: Press `Super` (Windows key), type "Terminal"
- **Method 3**: Right-click on desktop, select "Open Terminal" (on some distributions)

#### Test Git Installation

Open your terminal and test that Git is working:

```bash
git --version
# Should show something like: git version 2.x.x
```

### Step 1: Install Python

**Python** is the programming language our music generator uses.

#### Windows:
1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download the latest Python version (min. 3.8)
3. **Important**: Check **"Add Python to PATH"** during installation!
4. Install Python with default settings

#### macOS:
```bash
# Option 1: Download from python.org (easier)
# Go to python.org/downloads and download the macOS version

# Option 2: With Homebrew (if installed)
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

### Step 2: Test Python

Open a **Terminal** (Linux/Mac) or **Command Prompt** (Windows):

```bash
python --version
# Should show: Python 3.8.x or higher

# If "python" doesn't work, try:
python3 --version
```

### Step 3: Download the Project

Now that you have Git installed, download the music generator project:

```bash
# Clone (download) the project from GitHub
git clone https://github.com/Corvus006/Stochastic-Music-Generator.git

# Navigate into the project folder
cd Stochastic-Music-Generator
```

### Step 4: Create Virtual Environment

**Windows:**
```cmd
# Create environment
python -m venv music_env

# Activate environment
music_env\Scripts\activate

# You should now see "(music_env)" before your prompt
```

**Linux/macOS:**
```bash
# Create environment
python3 -m venv music_env

# Activate environment
source music_env/bin/activate

# You should now see "(music_env)" before your prompt
```

### Step 5: Install Python Packages

With activated virtual environment:

```bash
# Install all required packages
pip install -r requirements.txt

# If that doesn't work, install individually:
pip install music21 opencv-python numpy
```

### Step 6: Install MuseScore (for PDF/MP3 Export)

**MuseScore** converts our music data into beautiful PDF sheet music and MP3 audio.

#### Windows:
1. Go to [musescore.org](https://musescore.org)
2. Download and install MuseScore 4
3. Start MuseScore once to ensure it works

#### macOS:
```bash
# With Homebrew
brew install musescore

# Or download from musescore.org
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install musescore3
# or for newer version:
sudo snap install musescore
```

#### Linux (Arch/Manjaro):
```bash
sudo pacman -S musescore
```

### Step 7: Connect Webcam

- Make sure a **webcam** is connected
- Most laptops already have an integrated webcam
- USB webcams also work

### Step 8: Generate First Music!

```bash
# Activate virtual environment (if not already active)
# Windows: music_env\Scripts\activate
# Linux/Mac: source music_env/bin/activate

# Generate music
python main.py
```

## 📋 Requirements (Automatically installed)

```
music21>=8.1.0
opencv-python>=4.8.0
numpy>=1.24.0
```

## 🔄 Virtual Environment - Important Commands

### Activate environment:
**Every time you use the project, you must activate the virtual environment:**

**Windows:**
```cmd
cd Music-Aleatoric
music_env\Scripts\activate
```

**Linux/macOS:**
```bash
cd Music-Aleatoric
source music_env/bin/activate
```

### Deactivate environment:
```bash
deactivate
```

### Check if environment is active:
- You see `(music_env)` before your terminal prompt
- Or test: `which python` (should point to the venv)

## 🎵 Usage

### Simple Usage
```bash
# Make sure virtual environment is active!
# You should see (music_env) in your terminal

python main.py
```

The program automatically generates:
1. **String Trio** (random measure count from config range)
2. **Random Ensemble** (random measure count from config range)
3. **Piano Piece** (random measure count from config range)

## ⚙️ Configuration

The file `config/config.xml` contains all musical parameters:

#### Measure Count Ranges:
```xml
<num_measures>30-40</num_measures>  <!-- Random between 30 and 40 measures -->
<!-- or -->
<num_measures>20</num_measures>     <!-- Fixed number of 20 measures -->
```

## 📁 Output & File Formats

Each composition automatically creates its own folder in `output/` with **4 different file formats**:

```
output/
├── string_trio_aleatoric/
│   ├── string_trio_aleatoric.musicxml    # For other notation programs
│   ├── string_trio_aleatoric.pdf         # Professionally typeset sheet music
│   ├── string_trio_aleatoric.mid         # For further editing
│   └── string_trio_aleatoric.mp3         # Audio playback
└── other_compositions/
```

**What you get:**
- **PDF**: Print-ready sheet music for performance
- **MP3**: Immediately listenable audio version
- **MIDI**: For DAWs and music software

---
*Let the webcam decide how your music sounds! 🎲🎵*
