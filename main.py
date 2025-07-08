from aleatoric.score_exporter import *
from aleatoric.stochastic_composer import create_multi_voice_score, create_random_score
from music21 import *

def main():
    print("=== Stochastic Music Generator ===")
    print("Using webcam-based randomness and XML configuration")
    print()
    
    # Option 1: Create score with specific ensemble
    print("Generating String Trio composition...")
    score1 = create_multi_voice_score("String Trio", 12, "Aleatoric String Trio")
    generate_pdf_and_mp3(score1, "string_trio_aleatoric")
    
    print()
    
    # Option 2: Completely random ensemble and length
    print("Generating completely random composition...")
    score2 = create_random_score()
    generate_pdf_and_mp3(score2, "completely_aleatoric")
    
    # Option 3: Piano solo
    print("Generating piano solo...")
    score3 = create_multi_voice_score("Piano Solo", 16, "Aleatoric Piano Piece")
    generate_pdf_and_mp3(score3, "piano_aleatoric")
    
    print()
    
    print("\n=== Generation Complete ===")
    print("Check the 'output' folder for generated files.")

if __name__ == "__main__":
    main()
