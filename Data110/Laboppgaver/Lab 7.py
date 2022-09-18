# Oppgave 1
def skrivnavn(navn):
    x = navn.split()
    antallnavn = len(x)
    print(f'{x[-1]}, {x[0]} ', end='')
    for n in range(1, antallnavn - 1):
        print(x[n][0] + '. ', end='')


# skrivnavn('Ole Ole Ole Ole Ole Ole Ole Ole Ole Olsen')


# Oppgave 2
def flett(x: str, y: str):
    r = ''
    i = 0
    while i < len(x) and i < len(y):
        r += x[i] + y[i]
        i += 1
    if i == len(x):
        return r + y[i:]
    else:
        return r + x[i:]


# print(flett('abcdefgh', '1234567890'))


# Oppgave 3
a = 'hei'
b = 'hopp'
# print(a, b)
temp = a
a = b
b = temp
# print(a, b)

# Oppgave 4
tekst = 'tre små musikanter på høybro plass \n' \
        'sto og spilte på en kontrabass \n' \
        'så kom en konstabel, spurte hva var hendt \n' \
        'tre små musikanter på høybro plass'


def vokalerstatning(lyrics, a):
    vokaler = 'aeiouyæøåAEIOUYÆØÅ'
    if a not in vokaler:
        return 'ikke en vokal'
    for vokaler in vokaler:
        lyrics = lyrics.replace(vokaler, a)
    return lyrics


# print(vokalerstatning(tekst, 'a'))


# Oppgave 5
def antallord(a):
    return len(a.split())


# print(antallord('Tre små musikanter på Høybro plass'))

# Oppgave 6
def skrivstorsmå(tekst):
    q = tekst.split()
    storsmå = ''
    for f in range(0, len(q)):
        if (f % 2 == 0):
            storsmå += f'{q[f].upper()} '
        else:
            storsmå += f'{q[f].lower()} '
    return storsmå


# print(skrivstorsmå('Tre små musikanter på Høybro plass'))

# Oppgave 7
TV = \
    '''
    Tulleveien Velforening
    leder: Kari
    kasserer: Ole
    IT-ansvarlig: Liv
    parkeringsansvarlig: Kari
    arrangementsansvarlig: Liv
    hagekonsulent: Kari
    brannansvarlig: Kari
    '''


def antallverv(navn):
    antall = 0
    verv = TV.splitlines()
    for f in verv:
        if navn in f:
            antall += 1
    return antall


def innsett(navn, jobb):
    verv = TV
    for f in jobb:
        fra = verv.find(f) + len(f) + 1  # finner posisjonen til vervet
        til = verv.find('\n', fra)
        t = verv[fra:]
        x = verv[fra:til]  # finner personen som har vervet
        v = t.replace(x, navn, 1)  # og erstatter denne med den nye
        verv = verv[:fra] + v
    return verv


TV = innsett('Per', ['kasserer', 'hagekonsulent'])
print(TV)
