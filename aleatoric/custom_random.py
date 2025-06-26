import cv2
import numpy as np
import hashlib
import struct

def capture_frame(camera):
    ret, frame = camera.read()
    if not ret:
        raise RuntimeError("Kamerabild konnte nicht aufgenommen werden.")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray

def get_noise_image_diff(img1, img2):
    return cv2.absdiff(img1, img2)

def hash_noise_image(image):
    image_bytes = image.tobytes()
    return hashlib.sha256(image_bytes).digest()

def get_random_bytes_from_camera(num_bytes=4):
    camera = cv2.VideoCapture(0)
    try:
        frame1 = capture_frame(camera)
        cv2.waitKey(30)
        frame2 = capture_frame(camera)
        noise = get_noise_image_diff(frame1, frame2)
        hash_bytes = hash_noise_image(noise)
        return hash_bytes[:num_bytes]
    finally:
        camera.release()

def bytes_to_uint32(b):
    return struct.unpack("I", b)[0]  # 4 Bytes → unsigned int

def get_random_number(start, end):
    if start >= end:
        raise ValueError("Startwert muss kleiner als Endwert sein.")
    
    # 4 zufällige Bytes holen
    rand_bytes = get_random_bytes_from_camera(4)
    rand_int = bytes_to_uint32(rand_bytes)

    # Bereich skalieren
    range_size = end - start + 1
    return start + (rand_int % range_size)

# Beispiel
for _ in range(5):
    rnd = get_random_number(10, 100)
    print("Zufallszahl:", rnd)
