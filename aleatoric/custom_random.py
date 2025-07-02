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
        """Opens the camera once."""
        if self.camera is None:
            self.camera = cv2.VideoCapture(0)
            if not self.camera.isOpened():
                raise RuntimeError("Camera could not be opened.")
            # First frame for initialization
            time.sleep(0.1)  # Wait briefly until camera is ready
            ret, frame = self.camera.read()
            if ret:
                self.last_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    def close_camera(self):
        """Closes the camera."""
        if self.camera is not None:
            self.camera.release()
            self.camera = None
    
    def capture_frame(self):
        """Captures a single image."""
        if self.camera is None:
            raise RuntimeError("Camera is not open.")
        
        ret, frame = self.camera.read()
        if not ret:
            raise RuntimeError("Camera image could not be captured.")
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    def generate_random_pool(self, pool_size=50):
        """Generates a pool of random numbers from multiple camera images."""
        if self.camera is None:
            self.open_camera()
        
        self.random_pool = []
        
        for _ in range(pool_size):
            # Wait briefly for image change
            time.sleep(0.01)  # 10ms should be enough
            
            current_frame = self.capture_frame()
            
            if self.last_frame is not None:
                # Difference between current and last frame
                noise = cv2.absdiff(current_frame, self.last_frame)
                
                # Generate hash
                image_bytes = noise.tobytes()
                hash_bytes = hashlib.sha256(image_bytes).digest()
                
                # Convert 4 bytes to uint32
                rand_int = struct.unpack("I", hash_bytes[:4])[0]
                self.random_pool.append(rand_int)
            
            self.last_frame = current_frame
        
        self.pool_index = 0
        print(f"Random pool with {len(self.random_pool)} values generated.")
    
    def get_random_from_pool(self, start, end):
        """Gets a random number from the pool."""
        if start >= end:
            raise ValueError("Start value must be less than end value.")
        
        # If pool is empty or exhausted, regenerate
        if not self.random_pool or self.pool_index >= len(self.random_pool):
            self.generate_random_pool()
        
        # Get number from pool
        rand_int = self.random_pool[self.pool_index]
        self.pool_index += 1
        
        # Scale range
        range_size = end - start + 1
        return start + (rand_int % range_size)

# Global generator
_global_generator = None

def get_random_number(start, end):
    """Simplified function for compatibility with existing code."""
    global _global_generator
    
    if _global_generator is None:
        _global_generator = WebcamRandomGenerator()
        _global_generator.open_camera()
    
    return _global_generator.get_random_from_pool(start, end)

def initialize_random_generator():
    """Initializes the generator and creates a first pool."""
    global _global_generator
    _global_generator = WebcamRandomGenerator()
    _global_generator.open_camera()
    _global_generator.generate_random_pool(100)  # Large pool for many random numbers
    print("Webcam random generator initialized.")

def cleanup_random_generator():
    """Closes the camera and cleans up."""
    global _global_generator
    if _global_generator is not None:
        _global_generator.close_camera()
        _global_generator = None
        print("Webcam random generator closed.")

# Context Manager for explicit control
def webcam_random_session():
    """Context Manager for a webcam random session."""
    return WebcamRandomGenerator()

# Example usage:
if __name__ == "__main__":
    # Option 1: Automatic (as before)
    print("=== Automatic Usage ===")
    for i in range(10):
        rnd = get_random_number(1, 100)
        print(f"Random number {i+1}: {rnd}")
    
    cleanup_random_generator()
    
    print("\n=== Explicit Session ===")
    # Option 2: Explicit session with Context Manager
    with webcam_random_session() as generator:
        generator.generate_random_pool(20)
        for i in range(15):
            rnd = generator.get_random_from_pool(1, 100)
            print(f"Session random number {i+1}: {rnd}")
