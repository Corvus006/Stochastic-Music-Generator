import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import List, Dict
import os

@dataclass
class Instrument:
    name: str
    range_low: str
    range_high: str
    max_simultaneous_notes: int
    description: str

@dataclass
class Ensemble:
    name: str
    instruments: List[Instrument]

@dataclass
class MusicConfig:
    rhythms: List[str]
    dynamics: List[str]
    articulations: List[str]
    ensembles: Dict[str, Ensemble]
    num_measures_min: int
    num_measures_max: int

def parse_config(config_path="config/config.xml"):
    """Parse the XML configuration file and return a MusicConfig object."""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    tree = ET.parse(config_path)
    root = tree.getroot()
    
    # Parse num_measures
    num_measures_min = 8  # Default
    num_measures_max = 16  # Default
    
    num_measures_elem = root.find('num_measures')
    if num_measures_elem is not None and num_measures_elem.text:
        num_measures_text = num_measures_elem.text.strip()
        if '-' in num_measures_text:
            # Format: "30-40"
            min_str, max_str = num_measures_text.split('-')
            num_measures_min = int(min_str.strip())
            num_measures_max = int(max_str.strip())
        else:
            # Format: "20" (feste Anzahl)
            num_measures_min = int(num_measures_text)
            num_measures_max = int(num_measures_text)
    
    # Parse rhythms
    rhythms = []
    rhythms_elem = root.find('rhythms')
    if rhythms_elem is not None:
        rhythms = [rhythm.text for rhythm in rhythms_elem.findall('rhythm')]
    
    # Parse dynamics
    dynamics = []
    dynamics_elem = root.find('dynamics')
    if dynamics_elem is not None:
        dynamics = [dynamic.text for dynamic in dynamics_elem.findall('dynamic')]
    
    # Parse articulations
    articulations = []
    articulations_elem = root.find('articulations')
    if articulations_elem is not None:
        articulations = [articulation.text for articulation in articulations_elem.findall('articulation')]
    
    # Parse instrumentations
    ensembles = {}
    instrumentations_elem = root.find('instrumentations')
    if instrumentations_elem is not None:
        for ensemble_elem in instrumentations_elem.findall('ensemble'):
            ensemble_name = ensemble_elem.get('name')
            instruments = []
            
            for instrument_elem in ensemble_elem.findall('instrument'):
                name = instrument_elem.get('name')
                range_str = instrument_elem.get('range')
                max_notes = int(instrument_elem.get('maxSimultaneousNotes', 1))
                description = instrument_elem.text or ""
                
                # Parse range
                range_low, range_high = range_str.split('-')
                
                instrument = Instrument(name, range_low, range_high, max_notes, description)
                instruments.append(instrument)
            
            ensembles[ensemble_name] = Ensemble(ensemble_name, instruments)
    
    return MusicConfig(rhythms, dynamics, articulations, ensembles, num_measures_min, num_measures_max)