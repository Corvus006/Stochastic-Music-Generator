from aleatoric.score_exporter import *
from aleatoric.stochastic_composer import create_multi_voice_score
from music21 import *

def main():
    # Create example score
    score = create_multi_voice_score()
    
    # Generate PDF and MP3
    generate_pdf_and_mp3(score, "aleatory_music")

if __name__ == "__main__":
    main()
