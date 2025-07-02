from music21 import *
from difflib import get_close_matches
from .custom_random import get_random_number
from .config_parser import parse_config, MusicConfig

class StochasticComposer:
    def __init__(self, config_path="config/config.xml"):
        self.config = parse_config(config_path)
        # ...existing instrument_mapping code...
        self.instrument_mapping = {
            # Strings - English primary, German secondary for compatibility
            "violin": instrument.Violin,
            "viola": instrument.Viola,
            "cello": instrument.Violoncello,
            "violoncello": instrument.Violoncello,
            "contrabass": instrument.Contrabass,
            "double bass": instrument.Contrabass,
            "violine": instrument.Violin,  # German compatibility
            "geige": instrument.Violin,    # German compatibility
            "bratsche": instrument.Viola,  # German compatibility
            "kontrabass": instrument.Contrabass,  # German compatibility
            
            # Woodwinds - English primary
            "flute": instrument.Flute,
            "piccolo": instrument.Piccolo,
            "oboe": instrument.Oboe,
            "clarinet": instrument.Clarinet,
            "bassoon": instrument.Bassoon,
            "saxophone": instrument.Saxophone,
            "flöte": instrument.Flute,      # German compatibility
            "querflöte": instrument.Flute,  # German compatibility
            "klarinette": instrument.Clarinet,  # German compatibility
            "fagott": instrument.Bassoon,   # German compatibility
            "saxophon": instrument.Saxophone,  # German compatibility
            
            # Brass - English primary
            "horn": instrument.Horn,
            "trumpet": instrument.Trumpet,
            "trombone": instrument.Trombone,
            "tuba": instrument.Tuba,
            "waldhorn": instrument.Horn,    # German compatibility
            "trompete": instrument.Trumpet, # German compatibility
            "posaune": instrument.Trombone, # German compatibility
            
            # Keyboards - English primary
            "piano": instrument.Piano,
            "harpsichord": instrument.Harpsichord,
            "organ": instrument.Organ,
            "keyboard": instrument.Piano,
            "klavier": instrument.Piano,    # German compatibility
            "flügel": instrument.Piano,     # German compatibility
            "cembalo": instrument.Harpsichord,  # German compatibility
            "orgel": instrument.Organ,      # German compatibility
            
            # Plucked/Harp - English primary
            "harp": instrument.Harp,
            "guitar": instrument.Guitar,
            "mandolin": instrument.Mandolin,
            "harfe": instrument.Harp,       # German compatibility
            "gitarre": instrument.Guitar,   # German compatibility
            "mandoline": instrument.Mandolin,  # German compatibility
            
            # Percussion - English primary
            "percussion": instrument.Percussion,
            "drums": instrument.Percussion,
            "timpani": instrument.Timpani,
            "schlagzeug": instrument.Percussion,  # German compatibility
            "pauken": instrument.Timpani,   # German compatibility
            
            # Voice - English primary
            "soprano": instrument.Soprano,
            "alto": instrument.Alto,
            "tenor": instrument.Tenor,
            "bass": instrument.Bass,
            "baritone": instrument.Baritone,
            "sopran": instrument.Soprano,   # German compatibility
            "alt": instrument.Alto,         # German compatibility
            "bariton": instrument.Baritone, # German compatibility
        }
    
    def get_random_measures_count(self):
        """Get a random number of measures from config range."""
        return get_random_number(self.config.num_measures_min, self.config.num_measures_max)
        
    # ...existing methods...
    def note_name_to_midi(self, note_name):
        """Convert note name like 'C4' to MIDI number."""
        try:
            n = note.Note(note_name)
            return n.pitch.midi
        except:
            return 60  # Default to C4
    
    def midi_to_note_name(self, midi_num):
        """Convert MIDI number to note name."""
        try:
            n = note.Note(midi=midi_num)
            return n.nameWithOctave
        except:
            return "C4"
    
    def get_random_note_in_range(self, range_low, range_high):
        """Generate a random note within the instrument's range."""
        low_midi = self.note_name_to_midi(range_low)
        high_midi = self.note_name_to_midi(range_high)
        
        random_midi = get_random_number(low_midi, high_midi)
        return self.midi_to_note_name(random_midi)
    
    def get_random_rhythm(self):
        """Get a random rhythm from config."""
        rhythm_idx = get_random_number(0, len(self.config.rhythms) - 1)
        rhythm_str = self.config.rhythms[rhythm_idx]
        
        # Convert fraction string to quarterLength
        if rhythm_str == "1/1":
            return 4.0
        elif rhythm_str == "1/2":
            return 2.0
        elif rhythm_str == "1/4":
            return 1.0
        elif rhythm_str == "1/8":
            return 0.5
        elif rhythm_str == "1/16":
            return 0.25
        else:
            return 1.0  # Default
    
    def get_random_dynamic(self):
        """Get a random dynamic from config."""
        dynamic_idx = get_random_number(0, len(self.config.dynamics) - 1)
        return self.config.dynamics[dynamic_idx]
    
    def get_random_articulation(self):
        """Get a random articulation from config."""
        articulation_idx = get_random_number(0, len(self.config.articulations) - 1)
        return self.config.articulations[articulation_idx]
    
    def add_articulation_to_note(self, note_obj, articulation_name):
        """Add articulation to a note object."""
        if articulation_name == "staccato":
            note_obj.articulations.append(articulations.Staccato())
        elif articulation_name == "accent":
            note_obj.articulations.append(articulations.Accent())
        elif articulation_name == "tenuto":
            note_obj.articulations.append(articulations.Tenuto())
        # legato and none don't need explicit articulation marks
    
    def get_music21_instrument(self, instrument_name):
        """Convert instrument name to music21 instrument object with intelligent matching."""
        if not instrument_name:
            return instrument.Piano()
            
        name_clean = instrument_name.lower().strip()
        
        # 1. Direct search in mapping
        if name_clean in self.instrument_mapping:
            return self.instrument_mapping[name_clean]()
        
        # 2. Partial search (contains word)
        for key, instr_class in self.instrument_mapping.items():
            if key in name_clean or name_clean in key:
                print(f"Partial match: '{instrument_name}' -> {instr_class.__name__}")
                return instr_class()
        
        # 3. Fuzzy String Matching (similar spelling)
        instrument_keys = list(self.instrument_mapping.keys())
        close_matches = get_close_matches(name_clean, instrument_keys, n=1, cutoff=0.6)
        
        if close_matches:
            matched_key = close_matches[0]
            matched_instrument = self.instrument_mapping[matched_key]
            print(f"Fuzzy match: '{instrument_name}' -> '{matched_key}' -> {matched_instrument.__name__}")
            return matched_instrument()
        
        # 4. Category-based fallback logic
        fallback = self._get_category_fallback(name_clean)
        if fallback:
            print(f"Category fallback: '{instrument_name}' -> {fallback.__name__}")
            return fallback()
        
        # 5. Last fallback based on instrument range from config
        config_fallback = self._get_config_based_fallback(instrument_name)
        if config_fallback:
            print(f"Config-based fallback: '{instrument_name}' -> {config_fallback.__name__}")
            return config_fallback()
        
        # 6. Ultimate fallback
        print(f"No match found for '{instrument_name}', using Piano as default")
        return instrument.Piano()
    
    def _get_category_fallback(self, name_clean):
        """Category-based fallback logic."""
        # String categories
        if any(word in name_clean for word in ["string", "streicher", "strings", "bogen"]):
            return instrument.Violin
            
        # Wind categories
        if any(word in name_clean for word in ["wind", "bläser", "holz", "wood", "brass", "blech"]):
            return instrument.Flute
            
        # Keyboard categories
        if any(word in name_clean for word in ["key", "taste", "keyboard"]):
            return instrument.Piano
            
        # Percussion categories
        if any(word in name_clean for word in ["drum", "schlag", "percussion", "perc"]):
            return instrument.Percussion
            
        return None
    
    def _get_config_based_fallback(self, instrument_name):
        """Fallback based on range from configuration."""
        # Search for the instrument in the config
        for ensemble in self.config.ensembles.values():
            for instr in ensemble.instruments:
                if instr.name.lower() == instrument_name.lower():
                    # Decide based on range
                    low_midi = self.note_name_to_midi(instr.range_low)
                    high_midi = self.note_name_to_midi(instr.range_high)
                    
                    # Very low -> Bass instrument
                    if low_midi < 40:  # below E2
                        return instrument.Contrabass
                    # Medium-low -> Cello/Bassoon
                    elif low_midi < 55:  # below G3
                        return instrument.Violoncello
                    # Medium -> Viola/Horn
                    elif low_midi < 65:  # below F4
                        return instrument.Viola
                    # High -> Violin/Flute
                    else:
                        return instrument.Violin
        
        return None
    
    def create_random_measure(self, instr, beats_per_measure=4):
        """Create a random measure for an instrument."""
        measure = stream.Measure()
        current_beats = 0.0
        
        while current_beats < beats_per_measure:
            remaining_beats = beats_per_measure - current_beats
            
            # Get random rhythm, but don't exceed remaining beats
            rhythm = self.get_random_rhythm()
            if rhythm > remaining_beats:
                rhythm = remaining_beats
            
            # Decide if we want a note, chord, or rest
            note_type = get_random_number(1, 10)
            
            if note_type <= 7:  # 70% chance for note/chord
                # Decide how many notes (up to instrument's max)
                max_notes = min(3, instr.max_simultaneous_notes)
                if max_notes == 1:
                    num_notes = 1
                else:
                    num_notes = get_random_number(1, max_notes)
                
                if num_notes == 1:
                    # Single note
                    note_name = self.get_random_note_in_range(instr.range_low, instr.range_high)
                    n = note.Note(note_name, quarterLength=rhythm)
                    
                    # Add random articulation
                    articulation = self.get_random_articulation()
                    self.add_articulation_to_note(n, articulation)
                    
                    measure.append(n)
                else:
                    # Chord
                    chord_notes = []
                    for _ in range(num_notes):
                        note_name = self.get_random_note_in_range(instr.range_low, instr.range_high)
                        chord_notes.append(note_name)
                    
                    c = chord.Chord(chord_notes, quarterLength=rhythm)
                    
                    # Add random articulation
                    articulation = self.get_random_articulation()
                    self.add_articulation_to_note(c, articulation)
                    
                    measure.append(c)
            else:  # 30% chance for rest
                r = note.Rest(quarterLength=rhythm)
                measure.append(r)
            
            current_beats += rhythm
        
        return measure
    
    def create_random_score(self, ensemble_name="Piano Solo", num_measures=None, title="Aleatoric Music"):
        """Create a complete random score using the specified ensemble."""
        if ensemble_name not in self.config.ensembles:
            available = list(self.config.ensembles.keys())
            raise ValueError(f"Ensemble '{ensemble_name}' not found. Available: {available}")
        
        # Use config-based random measures if not specified
        if num_measures is None:
            num_measures = self.get_random_measures_count()
            print(f"Using random measure count from config: {num_measures} measures (range: {self.config.num_measures_min}-{self.config.num_measures_max})")
        
        ensemble = self.config.ensembles[ensemble_name]
        score = stream.Score()
        
        # Add metadata
        score.append(metadata.Metadata())
        score.metadata.title = title
        score.metadata.composer = "Stochastic Music Generator"
        
        # Add time signature
        time_sig = meter.TimeSignature('4/4')
        
        # Create parts for each instrument
        for instr in ensemble.instruments:
            part = stream.Part()
            part.partName = instr.name
            
            # Add instrument
            music21_instr = self.get_music21_instrument(instr.name)
            part.insert(0, music21_instr)
            part.insert(0, time_sig)
            
            # Add random dynamic at the beginning
            initial_dynamic = self.get_random_dynamic()
            part.insert(0, dynamics.Dynamic(initial_dynamic))
            
            # Create random measures
            for measure_num in range(num_measures):
                measure = self.create_random_measure(instr)
                
                # Occasionally add new dynamics
                if get_random_number(1, 100) <= 20:  # 20% chance
                    new_dynamic = self.get_random_dynamic()
                    measure.insert(0, dynamics.Dynamic(new_dynamic))
                
                part.append(measure)
            
            score.append(part)
        
        return score

def create_multi_voice_score(ensemble_name="String Trio", num_measures=None, title="Aleatoric Composition"):
    """Create a random multi-voice score using the stochastic composer."""
    composer = StochasticComposer()
    return composer.create_random_score(ensemble_name, num_measures, title)

def create_random_score():
    """Create a random score with random ensemble selection and random measures from config."""
    composer = StochasticComposer()
    
    # Choose random ensemble
    ensemble_names = list(composer.config.ensembles.keys())
    ensemble_idx = get_random_number(0, len(ensemble_names) - 1)
    chosen_ensemble = ensemble_names[ensemble_idx]
    
    # Use random measures from config (num_measures=None triggers config-based random)
    num_measures = composer.get_random_measures_count()
    
    print(f"Generating random score with {chosen_ensemble}, {num_measures} measures (config range: {composer.config.num_measures_min}-{composer.config.num_measures_max})")
    
    return composer.create_random_score(
        ensemble_name=chosen_ensemble,
        num_measures=num_measures,
        title=f"Aleatoric Music - {chosen_ensemble}"
    )