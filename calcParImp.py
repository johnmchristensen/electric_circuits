import numpy as np

def calcParImp(*imps):
    """
    Calculate the equivalent parallel impedance of two or more impedances.

    Parameters:
        *imps: Variable number of impedances (real or complex).

    Returns:
        Complex equivalent parallel impedance.

    Formula:
        1/Z_eq = 1/Z1 + 1/Z2 + ... + 1/Zn
    """
    if len(imps) == 0:
        raise ValueError("At least one impedance must be provided.")
    if any(z == 0 for z in imps):
        raise ValueError("Impedance cannot be zero (short circuit).")

    return 1 / sum(1 / complex(z) for z in imps)
