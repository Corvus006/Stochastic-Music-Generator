from music21 import *
from difflib import get_close_matches
from .custom_random import get_random_number
from .config_parser import parse_config, MusicConfig

class StochasticComposer:
    def __init__(self, config_path="config/config.xml"):
        self.config = parse_config(config_path)
        # ...existing instrument_mapping code...
        self.instrument_mapping = {
            # Strings - German/English
            "violine": instrument.Violin,
            "violin": instrument.Violin,
            "geige": instrument.Violin,
            "viola": instrument.Viola,
            "bratsche": instrument.Viola,
            "cello": instrument.Violoncello,
            "violoncello": instrument.Violoncello,
            "kontrabass": instrument.Contrabass,
            "doublebass": instrument.Contrabass,
            
            # Woodwinds
            "flöte": instrument.Flute,
            "flute": instrument.Flute,
            "querflöte": instrument.Flute,
            "piccolo": instrument.Piccolo,
            "oboe": instrument.Oboe,
            "klarinette": instrument.Clarinet,
            "clarinet": instrument.Clarinet,
            "fagott": instrument.Bassoon,
            "bassoon": instrument.Bassoon,
            "saxophon": instrument.Saxophone,
            "saxophone": instrument.Saxophone,
            
            # Brass
            "horn": instrument.Horn,
            "waldhorn": instrument.Horn,
            "trompete": instrument.Trumpet,
            "trumpet": instrument.Trumpet,
            "posaune": instrument.Trombone,
            "trombone": instrument.Trombone,
            "tuba": instrument.Tuba,
            
            # Keyboards
            "klavier": instrument.Piano,
            "piano": instrument.Piano,
            "flügel": instrument.Piano,
            "keyboard": instrument.Piano,
            "cembalo": instrument.Harpsichord,
            "harpsichord": instrument.Harpsichord,
            "orgel": instrument.Organ,
            "organ": instrument.Organ,
            
            # Plucked/Harp
            "harfe": instrument.Harp,
            "harp": instrument.Harp,
            "gitarre": instrument.Guitar,
            "guitar": instrument.Guitar,
            "mandoline": instrument.Mandolin,
            "mandolin": instrument.Mandolin,
            
            # Percussion
            "schlagzeug": instrument.Percussion,
            "drums": instrument.Percussion,
            "percussion": instrument.Percussion,
            "timpani": instrument.Timpani,
            "pauken": instrument.Timpani,
            
            # Voice
            "sopran": instrument.Soprano,
            "soprano": instrument.Soprano,
            "alt": instrument.Alto,
            "alto": instrument.Alto,
            "tenor": instrument.Tenor,
            "bass": instrument.Bass,
            "bariton": instrument.Baritone,
            "baritone": instrument.Baritone,
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
        
        # 1. Direkte Suche im Mapping
        if name_clean in self.instrument_mapping:
            return self.instrument_mapping[name_clean]()
        
        # 2. Partielle Suche (enthält Wort)
        for key, instr_class in self.instrument_mapping.items():
            if key in name_clean or name_clean in key:
                print(f"Partial match: '{instrument_name}' -> {instr_class.__name__}")
                return instr_class()
        
        # 3. Fuzzy String Matching (ähnliche Schreibweise)
        instrument_keys = list(self.instrument_mapping.keys())
        close_matches = get_close_matches(name_clean, instrument_keys, n=1, cutoff=0.6)
        
        if close_matches:
            matched_key = close_matches[0]
            matched_instrument = self.instrument_mapping[matched_key]
            print(f"Fuzzy match: '{instrument_name}' -> '{matched_key}' -> {matched_instrument.__name__}")
            return matched_instrument()
        
        # 4. Kategorien-basierte Fallback-Logik
        fallback = self._get_category_fallback(name_clean)
        if fallback:
            print(f"Category fallback: '{instrument_name}' -> {fallback.__name__}")
            return fallback()
        
        # 5. Letzter Fallback basierend auf Instrumentenbereich aus Config
        config_fallback = self._get_config_based_fallback(instrument_name)
        if config_fallback:
            print(f"Config-based fallback: '{instrument_name}' -> {config_fallback.__name__}")
            return config_fallback()
        
        # 6. Ultimativer Fallback
        print(f"No match found for '{instrument_name}', using Piano as default")
        return instrument.Piano()
    
    def _get_category_fallback(self, name_clean):
        """Kategorien-basierte Fallback-Logik."""
        # Streicher-Kategorien
        if any(word in name_clean for word in ["string", "streicher", "strings", "bogen"]):
            return instrument.Violin
            
        # Bläser-Kategorien
        if any(word in name_clean for word in ["wind", "bläser", "holz", "wood", "brass", "blech"]):
            return instrument.Flute
            
        # Tasten-Kategorien
        if any(word in name_clean for word in ["key", "taste", "keyboard"]):
            return instrument.Piano
            
        # Schlag-Kategorien
        if any(word in name_clean for word in ["drum", "schlag", "percussion", "perc"]):
            return instrument.Percussion
            
        return None
    
    def _get_config_based_fallback(self, instrument_name):
        """Fallback basierend auf Tonbereich aus der Konfiguration."""
        # Suche das Instrument in der Config
        for ensemble in self.config.ensembles.values():
            for instr in ensemble.instruments:
                if instr.name.lower() == instrument_name.lower():
                    # Basierend auf Tonbereich entscheiden
                    low_midi = self.note_name_to_midi(instr.range_low)
                    high_midi = self.note_name_to_midi(instr.range_high)
                    
                    # Sehr tief -> Bass-Instrument
                    if low_midi < 40:  # unter E2
                        return instrument.Contrabass
                    # Mittel-tief -> Cello/Fagott
                    elif low_midi < 55:  # unter G3
                        return instrument.Violoncello
                    # Mittel -> Viola/Horn
                    elif low_midi < 65:  # unter F4
                        return instrument.Viola
                    # Hoch -> Violine/Flöte
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
    
    def create_random_score(self, ensemble_name="Klavier Solo", num_measures=None, title="Aleatorische Musik"):
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

def create_multi_voice_score(ensemble_name="Streichtrio", num_measures=None, title="Aleatorische Komposition"):
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
        title=f"Aleatorische Musik - {chosen_ensemble}"
    )