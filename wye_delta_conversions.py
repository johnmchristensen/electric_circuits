def delta2wye(ra, rb, rc):
    sum = ra + rb + rc
    return (rc * rb) / sum, (rc * ra) / sum, (ra * rb) / sum

def wye2delta(r1, r2, r3):
    sum = r1 * r2 + r1 * r3 + r2 * r3
    return sum / r1, sum / r2, sum / r3