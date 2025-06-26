import cv2
import numpy as np
import hashlib
import struct
import time

class WebcamRandomGenerator:
    def __init__(self):
        self.camera = None
        self.last_frame = None
        self.random_pool = []
        self.pool_index = 0
        
    def __enter__(self):
        self.open_camera()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_camera()
    
    def open_camera(self):
        """Öffnet die Kamera einmal."""
        if self.camera is None:
            self.camera = cv2.VideoCapture(0)
            if not self.camera.isOpened():
                raise RuntimeError("Kamera konnte nicht geöffnet werden.")
            # Ersten Frame für Initialisierung
            time.sleep(0.1)  # Kurz warten bis Kamera bereit ist
            ret, frame = self.camera.read()
            if ret:
                self.last_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    def close_camera(self):
        """Schließt die Kamera."""
        if self.camera is not None:
            self.camera.release()
            self.camera = None
    
    def capture_frame(self):
        """Nimmt ein einzelnes Bild auf."""
        if self.camera is None:
            raise RuntimeError("Kamera ist nicht geöffnet.")
        
        ret, frame = self.camera.read()
        if not ret:
            raise RuntimeError("Kamerabild konnte nicht aufgenommen werden.")
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    def generate_random_pool(self, pool_size=50):
        """Generiert einen Pool von Zufallszahlen aus mehreren Kamerabildern."""
        if self.camera is None:
            self.open_camera()
        
        self.random_pool = []
        
        for _ in range(pool_size):
            # Kurz warten für Bildveränderung
            time.sleep(0.01)  # 10ms sollten reichen
            
            current_frame = self.capture_frame()
            
            if self.last_frame is not None:
                # Differenz zwischen aktuellem und letztem Frame
                noise = cv2.absdiff(current_frame, self.last_frame)
                
                # Hash generieren
                image_bytes = noise.tobytes()
                hash_bytes = hashlib.sha256(image_bytes).digest()
                
                # 4 Bytes zu uint32 konvertieren
                rand_int = struct.unpack("I", hash_bytes[:4])[0]
                self.random_pool.append(rand_int)
            
            self.last_frame = current_frame
        
        self.pool_index = 0
        print(f"Zufallspool mit {len(self.random_pool)} Werten generiert.")
    
    def get_random_from_pool(self, start, end):
        """Holt eine Zufallszahl aus dem Pool."""
        if start >= end:
            raise ValueError("Startwert muss kleiner als Endwert sein.")
        
        # Wenn Pool leer oder aufgebraucht, neu generieren
        if not self.random_pool or self.pool_index >= len(self.random_pool):
            self.generate_random_pool()
        
        # Zahl aus Pool holen
        rand_int = self.random_pool[self.pool_index]
        self.pool_index += 1
        
        # Bereich skalieren
        range_size = end - start + 1
        return start + (rand_int % range_size)

# Globaler Generator
_global_generator = None

def get_random_number(start, end):
    """Vereinfachte Funktion für Kompatibilität mit bestehendem Code."""
    global _global_generator
    
    if _global_generator is None:
        _global_generator = WebcamRandomGenerator()
        _global_generator.open_camera()
    
    return _global_generator.get_random_from_pool(start, end)

def initialize_random_generator():
    """Initialisiert den Generator und erstellt einen ersten Pool."""
    global _global_generator
    _global_generator = WebcamRandomGenerator()
    _global_generator.open_camera()
    _global_generator.generate_random_pool(100)  # Großer Pool für viele Zufallszahlen
    print("Webcam-Zufallsgenerator initialisiert.")

def cleanup_random_generator():
    """Schließt die Kamera und räumt auf."""
    global _global_generator
    if _global_generator is not None:
        _global_generator.close_camera()
        _global_generator = None
        print("Webcam-Zufallsgenerator geschlossen.")

# Context Manager für explizite Kontrolle
def webcam_random_session():
    """Context Manager für eine Webcam-Random-Session."""
    return WebcamRandomGenerator()

# Beispiel für Nutzung:
if __name__ == "__main__":
    # Option 1: Automatisch (wie bisher)
    print("=== Automatische Nutzung ===")
    for i in range(10):
        rnd = get_random_number(1, 100)
        print(f"Zufallszahl {i+1}: {rnd}")
    
    cleanup_random_generator()
    
    print("\n=== Explizite Session ===")
    # Option 2: Explizite Session mit Context Manager
    with webcam_random_session() as generator:
        generator.generate_random_pool(20)
        for i in range(15):
            rnd = generator.get_random_from_pool(1, 100)
            print(f"Session Zufallszahl {i+1}: {rnd}")
