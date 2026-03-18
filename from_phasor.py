import numpy as np

def from_phasor(mag, angle_radians):
    real = mag * np.cos(angle_radians)
    img = mag * np.sin(angle_radians)
    return real + 1j * img