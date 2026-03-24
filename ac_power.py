from ac_circuit_elements import get_angle_radians, get_magnitude
import numpy as np

def calc_average_power(voltage_rect, current_rect):
    return 0.5 * get_magnitude(voltage_rect) * get_magnitude(current_rect) * np.cos(get_angle_radians(voltage_rect) - get_angle_radians(current_rect))