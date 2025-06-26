from aleatoric.score_exporter import *
from aleatoric.stochastic_composer import create_multi_voice_score, create_random_score
from music21 import *

def main():
    print("=== Stochastic Music Generator ===")
    print("Using webcam-based randomness and XML configuration")
    print()
    
    # Option 1: Create score with specific ensemble
    print("Generating Streichtrio composition...")
    score1 = create_multi_voice_score("Streichtrio", 12, "Aleatorisches Streichtrio")
    generate_pdf_and_mp3(score1, "streichtrio_aleatorisch")
    
    print()
    
    # Option 2: Completely random ensemble and length
    print("Generating completely random composition...")
    score2 = create_random_score()
    generate_pdf_and_mp3(score2, "vollstaendig_aleatorisch")
    
    print()
    
    # Option 3: Piano solo
    print("Generating piano solo...")
    score3 = create_multi_voice_score("Klavier Solo", 16, "Aleatorisches Klavierstück")
    generate_pdf_and_mp3(score3, "klavier_aleatorisch")
    
    print("\n=== Generation Complete ===")
    print("Check the 'output' folder for generated files.")

if __name__ == "__main__":
    main()
