from music21 import *

def create_multi_voice_score(title="Aleatorische Musik"):
    
    score = stream.Score()
    
    # Adds title and composer metadata
    score.append(metadata.Metadata())
    score.metadata.title = title
    score.metadata.composer = "Musik-Aleatorik Generator"

    # Create first part
    part1 = stream.Part()
    part1.partName = "Stimme 1"
    part1.insert(0, instrument.Piano())
    
    # Example nodes for voice 1
    part1.append(note.Note("C4", quarterLength=1))
    part1.append(note.Note("E4", quarterLength=1))
    part1.append(note.Note("G4", quarterLength=1))
    part1.append(note.Note("C5", quarterLength=1))
    
    # Create second part with a different instrument
    part2 = stream.Part() 
    part2.partName = "Stimme 2"
    part2.insert(0, instrument.Violin())
    
    # Example nodes for voice 2
    part2.append(note.Note("E4", quarterLength=2))
    part2.append(note.Note("D4", quarterLength=2))
    
    score.append(part1)
    score.append(part2)
    
    return score