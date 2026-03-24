import numpy as np
import sympy as sp

def to_capacitor_impedance(c, f):
    return 1 / (c * f * 1j)

def to_inductor_impedance(i, f):
    return i * f * 1j

def from_phasor(mag, angle_radians):
    real = mag * np.cos(angle_radians)
    img = mag * np.sin(angle_radians)
    return real + 1j * img

def to_phasor(rect):
    """
    Convert a number (complex, int, or float) to phasor (magnitude, angle in degrees).
    Args:
        rect (complex/int/float): Number to convert
    Returns:
        tuple: (magnitude, angle in degrees)
    """
    if isinstance(rect, dict):
        return {k: to_phasor(v) for k, v in rect.items()}

    if not isinstance(rect, complex):
      rect = complex(rect)

    magnitude = abs(rect)
    # Handle int/float (real numbers)
    if isinstance(rect, (int, float)):
        angle_deg = 0.0 if rect >= 0 else 180.0
    else:
        angle_deg = np.degrees(np.angle(rect))
    return magnitude, angle_deg

def convert_sol_to_phasor_strings(sol):
    return {k: to_string(*v) for k, v in sol.items()}

def to_string(mag, angle_deg):
    return f"{mag} @ {angle_deg}"

def to_phasor_string(rect):
    return to_string(*to_phasor(rect))

def get_magnitude(rect):
    return to_phasor(rect)[0]

def get_angle_radians(rect):
    return np.deg2rad(to_phasor(rect)[1])