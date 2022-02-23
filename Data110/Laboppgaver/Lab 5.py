import random


# Oppgave 1
def siste(last):
    return last[-1]


# Oppgave 2
def skrivsekvens(last):
    s = ''
    for i in last:
        s += f'{i}\t'
    if s == '':
        return s
    return s[:-1]


# Oppgave 3
def sifferhoyre(num):
    # digits = [int(d) for d in str(num)]
    digits = map(int, str(num))
    return sum(digits)


# Oppgave 4
def leshelltall(meldinger, a=None, b=None):
    for i in meldinger:
        tall = int(input(i))
        if (a is None or tall >= a) and (b is None or tall <= b):
            return tall
    return 'you fail'


# Oppgave 5
def kapasitetvakt(kapasitet):
    print("""Noen ankommer - tast 1
Noen går - tast 2
Avslutt - 0""")
    max_cap = kapasitet
    while True:
        choice = int(input())
        match choice:
            case 1:
                come = int(input('Hvor mange kommer?: '))
                if come > kapasitet:
                    print(f'Not enough space, only {kapasitet} spots left')
                    come = kapasitet
                kapasitet -= come
                print(f'{kapasitet}')
            case 2:
                leave = int(input('Hvor mange går?: '))
                current_people = max_cap - kapasitet
                if leave > current_people:
                    print(f'wtf bro that is more than {max_cap} only {current_people} can leave')
                    leave = current_people
                kapasitet += leave
                print(f'{kapasitet}')
            case 0:
                return 'takk for nå'
            case _:
                print('oh god oh fuck, input again')


# Oppgave 6
def ssk():
    muligheter = ['papir', 'saks', 'stein']
    maskin = random.choice(muligheter)
    spiller = input(f'Velg papir,saks eller stein: ')
    print('Maskinen velger', maskin)
    if spiller == maskin:
        return 'uavgjort'
    elif (spiller == 'papir' and maskin == 'stein') or \
            (spiller == 'saks' and maskin == 'papir') or \
            (spiller == 'stein' and maskin == 'saks'):
        return 'vant'
    else:
        return 'tapt'


# a)
def rps(runder):
    runde = 0
    vant = 0
    tapt = 0
    uavgjort = 0
    for i in range(runder):
        runde += 1
        print(f'Runde {runde}')
        resultat = ssk()
        if resultat == 'vant':
            vant += 1
        elif resultat == 'tapt':
            tapt += 1
        else:
            uavgjort += 1
        print(f'Stillingen er {vant} - {tapt} - ({uavgjort} uavgjorte)')
    print('spillet er slutt')


# b)
def stein_saks_papir():
    vant = 0
    tapt = 0
    uavgjort = 0
    best_of = int(input('Førstemann til? '))
    while vant < best_of and tapt < best_of:
        resultat = ssk()
        if resultat == 'vant':
            vant += 1
        elif resultat == 'tapt':
            tapt += 1
        else:
            uavgjort += 1
        print(f'Stillingen er {vant} - {tapt} - ({uavgjort} uavgjorte)')
    print('--------------')
    if vant > tapt:
        print('You win')
    else:
        print('du tapte')


# Oppgave 7
# a)
def blanke(n):
    if n < 1 or n > 9:
        return 'må være mellom 1-9'
    for i in range(n):
        print(str(f'{i + 1} ' * n))


# b)
def ruter(n):
    line = ''
    for j in range(1, n + 1):
        line += str(f'{j} ')
    for i in range(n):
        print(' ' * i + line)


# Oppgave 8
def permutasjoner(tekst, i, lengde):
    if i == lengde:
        print(''.join(tekst))
    else:
        for j in range(i, lengde):
            tekst[i], tekst[j] = tekst[j], tekst[i]
            permutasjoner(tekst, i + 1, lengde)
            tekst[i], tekst[j] = tekst[j], tekst[i]


string = 'abc'
n = len(string)
tekst = list(string)
permutasjoner(tekst, 0, n)
