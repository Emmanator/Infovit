# Oppgave 1
import math


def pi(d=2):
    if d > 15:
        return 'too many decimals'
    else:
        return f'{math.pi:.{d}f}'


# Oppgave 2
# Fra celsius til fahrenheit °F = (°C × 9/5) + 32
# Fra fahrenheit til celsius °C = (°F − 32) × 5/9
# celsius = 15.56
# fahrenheit = 60
# CtF = (celsius * 9/5) + 32
# FtC = (fahrenheit - 32) * 5/9
# \N{degree celsius} \N{degree fahrenheit}
# Gjør at degrees aksepterer bare floats
# unit: str = 'C' gjør at default value er C så funksjonen fungerer om man bare gir ett tall.
def tempkonv(degrees: float, unit: str = 'C') -> float:
    if unit == 'C':
        return (degrees * 9 / 5) + 32
    elif unit == 'F':
        return (degrees - 32) * 5/9
    else:
        return (degrees * 9/5) + 32  # else: skjer bare om funksjonen får bare ett tall og ikke C eller F



#Oppgave 3