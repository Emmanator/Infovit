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
        return (degrees - 32) * 5 / 9
    else:
        return (degrees * 9 / 5) + 32  # else: skjer bare om funksjonen får bare ett tall og ikke C eller F


# Oppgave 3
history = []
saldo = 500
rentesats = 0.01


def innskudd(d):
    global saldo
    global rentesats
    global history
    old_d = saldo
    saldo += d
    history.append(f'+{d}')
    if old_d <= 1000000 < saldo:
        print("gratulerer, du får bonusrente")
        rentesats += 0.01


def uttak(w):
    global saldo
    global rentesats
    global history
    if w > saldo:
        print('overtrekk')
        return
    old_w = saldo
    saldo -= w
    history.append(f'-{w}')
    if old_w >= 1000000 > saldo:
        print("du har nå ordinær rente")
        rentesats -= 0.01


def beregnRente():
    global saldo
    global rentesats
    return saldo * rentesats


def renteoppgjøret():
    innskudd(beregnRente())


def velg():
    print("""--------------------
1 - vis saldo
2 - innskudd
3 - uttak
4 - renteoppgjør
5 - siste endringer
--------------------""")
    choice = input('Velg handling: ')
    match choice:
        case '1':
            print('Saldo: ', saldo)
        case '2':
            beløp = float(input('beløp: '))
            innskudd(beløp)
        case '3':
            beløp = float(input('beløp: '))
            uttak(beløp)
        case '4':
            renteoppgjøret()
        case '5':
            for i in history[-3:]:
                print(i)
        case _:
            print('Denne funksjonen aksepterer bare 1-4')

while True:
    velg()