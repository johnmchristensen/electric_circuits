from ac_circuit_elements import get_angle_radians, get_magnitude
import numpy as np

def calc_average_power(voltage_rect, current_rect):
    return 0.5 * get_magnitude(voltage_rect) * get_magnitude(current_rect) * np.cos(get_angle_radians(voltage_rect) - get_angle_radians(current_rect))

def calc_max_average_power(voltage_thevenin, impedance_thevenin):
    return np.abs(get_magnitude(voltage_thevenin)) ** 2 / (8 * get_magnitude(impedance_thevenin))

def calc_max_average_power_resistive(current_thevenin, load_resistance):
    return 0.5 * get_magnitude(current_thevenin) ** 2 * load_resistance

def calc_power(current_rms, resistance):
    return current_rms ** 2 * resistance