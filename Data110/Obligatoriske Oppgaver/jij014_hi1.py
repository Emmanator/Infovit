# Oppgave 1
import math


def pi(d=2):  # uten noe verdi går funksjonen automatisk til 2
    if d > 15:  # 15 er maks antall math.pi returnerer
        print('For mange desimaler')
        return math.pi
    else:
        return f'{math.pi:.{d}f}'


# Oppgave 2
# Fra celsius til fahrenheit °F = (°C × 9/5) + 32
# Fra fahrenheit til celsius °C = (°F − 32) × 5/9
# unit: str = 'C' gjør at default value er C så funksjonen fungerer om man bare gir ett tall.
def temperaturKonvertering(degrees: float, unit: str = 'C') -> float:  # degrees aksepterer bare floats
    if unit == 'F':
        return (degrees - 32) * 5 / 9
    else:
        return (degrees * 9 / 5) + 32  # om brukeren skriver F kommer F -> C konversjon ellers er det C -> F


# Oppgave 3
history = []  # er for siste endring historie i velg()
saldo = 500  # baseline saldo
rentesats = 0.01  # baseline rente


# innskudd() tar mengden og legger det til history som en string, og gir saldo en new verdi
def innskudd(d):
    global saldo
    global rentesats
    global history
    old_d = saldo
    saldo += d
    history.append(f'+{d}')
    if old_d <= 1000000 < saldo:  # om gammel saldo var under 1000000 og ny saldo er over 1000000 gir den bonusrente
        print("gratulerer, du får bonusrente")
        rentesats += 0.01


# utakk() er lik innskud bare omvendt
def uttak(w):
    global saldo
    global rentesats
    global history
    if w > saldo:  # ser om uttaket er høyere enn saldo
        print('overtrekk')
        print(f'Saldo: {saldo}')
        return
    old_w = saldo
    saldo -= w
    history.append(f'-{w}')
    if old_w >= 1000000 > saldo:  # om old_w var over 1000000 og ny saldo er under 1000000 trekker den bonusrente
        print("du har nå ordinær rente")
        rentesats -= 0.01


# beregner bare rente med nåværende saldo, endrer ikke variabelen
def beregnRente():
    global saldo
    global rentesats
    return saldo * rentesats


# bruker innskudd funksjonen sammen med beregnrente funksjonen for saldo * rente
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
    match choice:  # bruker match case istedefor if/elif/else (Krever Python 3.10) syns det ser ryddigere ut.
        case '1':  # Match case ser mye ryddigere ut i denne sammenhengen, enn en rekke med if/elif/else statements imo.
            print(f'Saldo: {saldo:.2f}')  # Saldo er begrenset til 2 desimaler, kalkuleres som normalt ellers.
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
            print('Velg 1-5.')

while True:
    velg()