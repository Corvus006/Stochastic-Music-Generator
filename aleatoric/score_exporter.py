import subprocess
import os
import platform
from music21 import midi
def generate_pdf_with_title(score, filename="aleatory_music"):
    """
    Generates a PDF file from a music21 Score using MuseScore.
    Works on both Windows and Linux.
    Creates an output folder with the piece name.
    """
    # Create output directory
    output_dir = os.path.join("output", filename)
    os.makedirs(output_dir, exist_ok=True)
    
    xml_file = os.path.join(output_dir, f"{filename}.musicxml")
    pdf_file = os.path.join(output_dir, f"{filename}.pdf")

    # Save MusicXML
    score.write('musicxml', fp=xml_file)
    print(f"MusicXML saved: {xml_file}")

    # Different MuseScore paths depending on operating system
    if platform.system() == "Windows":
        musescore_commands = [
            'MuseScore3.exe',
            'MuseScore4.exe', 
            'mscore.exe',
            r'C:\Program Files\MuseScore 3\bin\MuseScore3.exe',
            r'C:\Program Files\MuseScore 4\bin\MuseScore4.exe',
            r'C:\Program Files (x86)\MuseScore 3\bin\MuseScore3.exe',
            r'C:\Program Files (x86)\MuseScore 4\bin\MuseScore4.exe'
        ]
    else:  # Linux/Unix/macOS
        musescore_commands = [
            'musescore',
            'mscore',
            'MuseScore',
            '/usr/bin/musescore',
            '/usr/local/bin/musescore',
            '/snap/bin/musescore',
            '/opt/musescore/bin/musescore'
        ]
    
    for cmd in musescore_commands:
        try:
            subprocess.run([cmd, '-o', pdf_file, xml_file], check=True)
            print(f"PDF generated with MuseScore: {pdf_file}")
            return
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue
            
    # If MuseScore was not found
    print("MuseScore not found!")
    if platform.system() == "Windows":
        print("Please install MuseScore from: https://musescore.org/")
    else:
        print("Install MuseScore with one of the following commands:")
        print("  Ubuntu/Debian: sudo apt install musescore")
        print("  Fedora: sudo dnf install musescore")
        print("  Arch: sudo pacman -S musescore")
        print("  Or from: https://musescore.org/")
    print("Or open the MusicXML file manually in MuseScore:")
    print(f"  {os.path.abspath(xml_file)}")

def generate_mp3_from_score(score, filename="aleatory_music"):
    """
    Generates an MP3 file from a music21 Score.
    Uses different methods depending on available software.
    Creates an output folder with the piece name.
    """
    # Create output directory
    output_dir = os.path.join("output", filename)
    os.makedirs(output_dir, exist_ok=True)
    
    midi_file = os.path.join(output_dir, f"{filename}.mid")
    mp3_file = os.path.join(output_dir, f"{filename}.mp3")
    
    try:
        # Save as MIDI
        score.write('midi', fp=midi_file)
        print(f"MIDI saved: {midi_file}")
    
        conversion_successful = False
        
        if not conversion_successful:
            if platform.system() == "Windows":
                musescore_commands = [
                    'MuseScore3.exe', 'MuseScore4.exe', 'mscore.exe',
                    r'C:\Program Files\MuseScore 3\bin\MuseScore3.exe',
                    r'C:\Program Files\MuseScore 4\bin\MuseScore4.exe'
                ]
            else:
                musescore_commands = ['musescore', 'mscore', '/usr/bin/musescore']
            
            for cmd in musescore_commands:
                try:
                    subprocess.run([cmd, '-o', mp3_file, midi_file], check=True)
                    print(f"MP3 generated with MuseScore: {mp3_file}")
                    conversion_successful = True
                    break
                except (subprocess.CalledProcessError, FileNotFoundError):
                    continue
        
        if not conversion_successful:
            print("MP3 conversion failed!")
            print("Install one of the following options:")
            if platform.system() == "Windows":
                print("  - MuseScore (https://musescore.org/)")
                print("  - FluidSynth + FFmpeg")
            else:
                print("  - Ubuntu/Debian: sudo apt install fluidsynth fluid-soundfont-gm ffmpeg")
                print("  - Ubuntu/Debian: sudo apt install timidity ffmpeg")
                print("  - Fedora: sudo dnf install fluidsynth soundfont2-default ffmpeg")
            print(f"MIDI file available: {os.path.abspath(midi_file)}")
            
    except Exception as e:
        print(f"Error generating MP3: {e}")

def generate_pdf_and_mp3(score, filename="aleatory_music"):
    """
    Generates both PDF and MP3 from a music21 Score.
    All files are saved in an output folder named after the piece.
    """
    output_dir = os.path.join("output", filename)
    print(f"Generating PDF and MP3 for: {filename}")
    print(f"Output directory: {os.path.abspath(output_dir)}")
    generate_pdf_with_title(score, filename)
    generate_mp3_from_score(score, filename)
