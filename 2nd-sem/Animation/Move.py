import math as m


def move(x, y_stat, phi, Ay, vphi, vx, secs):
    new_x = x + vx * secs
    new_phi = phi + vphi
    new_y = y_stat + Ay * m.sin(new_phi)
    return (new_x, new_y, new_phi)
