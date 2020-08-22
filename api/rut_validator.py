import sys
from itertools import cycle


def rut_validator(rut):
    rut = rut.upper()
    rut = rut.replace("-", "")
    rut = rut.replace(".", "")
    aux = rut[:-1]
    dv = rut[-1:]

    backwards = map(int, reversed(str(aux)))
    factors = cycle(range(2, 8))
    try:
        s = sum(d * f for d, f in zip(backwards, factors))
    except:
        return False
    else:
        res = (-s) % 11

        if str(res) == dv:
            return True
        elif dv == "K" and res == 10:
            return True
        else:
            return False
