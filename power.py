from ac_circuit_elements import get_angle_radians, get_magnitude, calc_sinusoidal_rms, from_phasor
import numpy as np

def calc_average_power(voltage_rect, current_rect):
    return 0.5 * get_magnitude(voltage_rect) * get_magnitude(current_rect) * np.cos(get_angle_radians(voltage_rect) - get_angle_radians(current_rect))

def calc_max_average_power(voltage_thevenin, impedance_thevenin):
    return np.abs(get_magnitude(voltage_thevenin)) ** 2 / (8 * get_magnitude(impedance_thevenin))

def calc_max_average_power_resistive(current_thevenin, load_resistance):
    return 0.5 * get_magnitude(current_thevenin) ** 2 * load_resistance

def calc_power_from_current_rms(current_rms, resistance):
    return current_rms ** 2 * resistance

def calc_power_from_voltage_rms(voltage_rms, resistance):
    return voltage_rms ** 2 / resistance

def calc_apparent_power(voltage, current):
    return calc_sinusoidal_rms(voltage) * calc_sinusoidal_rms(current)

def calc_power_factor(voltage, current):
    return np.cos(get_angle_radians(voltage) - get_angle_radians(current))

def calc_s_from_power_and_power_factor(power, power_factor, is_leading):
    theta = np.arccos(power_factor)
    if (is_leading):
        theta = theta * -1

    s_mag = power / power_factor

    return from_phasor(s_mag, theta)

def calc_power_factor_from_s(s):
    angle = get_angle_radians(s)
    return {
        "pf": np.cos(angle),
        "leading": angle < 0
    }

def mag2rms(m):
    return m / np.sqrt(2)

def complex2rms(c):
    return get_magnitude(c) / np.sqrt(2)
