emner = ['INFO100', 'INFO104', 'ECON100', 'JAP100', 'JAP110', 'INFO120', 'INFO125', 'KOGVIT101', 'JAP120', 'ECON200',
         'ECON220', 'ECON240', 'ECON300', 'ECON320', 'ECON340']
karakterer = {'INFO100': 'C', 'INFO104': 'B', 'ECON100': 'B', 'JAP100': 'C', 'JAP110': 'C', 'KOGVIT101': 'B',
              'ECON300': 'F', 'ECON220': 'D'}
fagområde = {'JAP': 'japansk', 'INF': 'informasjonsvitenskap', 'ECO': 'økonomi', 'KOG': 'kognitivvitenskap'}


def emneliste():
    global emner
    global karakterer
    global fagområde
    inv_map = {v: k for k, v in fagområde.items()}  # konverterer fagområde liste til det omvendte
    sorter = []
    print('Velg fag og/eller emnenivå (<enter> for alle)')
    field = str(input('Fag: ') or None)
    if field is not None:
        field = inv_map.get(field)
    nivå = input('Nivå: ') or None

    for p in emner:
        if (field is None or p.startswith(field)) and (nivå is None or p[-3] == nivå[0]):
            if p in karakterer:
                # print(f'{p} {karakterer[p]}')
                sorter.append(f'{p} {karakterer[p]}')
            else:
                # print(p)
                sorter.append(f'{p}')

    for s in sorted(sorter):
        print(s)
    return


def add():
    global emner
    nytt_emne = str(input('Nytt emne: '))
    emner.append(nytt_emne)
    return


def karakter():
    global emner
    global karakterer

    emne = input('Emne: ')
    while emne not in emner:
        emne = input('Må være et gyldig emne: ')

    sett_karakter = input('Karakter (<enter> for å slette): ')
    while sett_karakter not in 'ABCDEF':
        sett_karakter = input('Må være karakter A-F: ')

    karakterer[emne] = sett_karakter
    return


def karaktersnitt():
    global karakterer
    verdi = karakterer.values()
    nummer = 0
    abc_grade = {'A': 96, 'B': 86, 'C': 76, 'D': 66, 'E': 56, 'F': 50}

    for i in verdi:
        a = abc_grade[i]
        nummer += a
    kalk = nummer / len(verdi)
    kalk = int(kalk)

    match kalk:
        case n if 91 <= n <= 100:
            return 'A'
        case n if 81 <= n <= 90:
            return 'B'
        case n if 71 <= n <= 80:
            return 'C'
        case n if 61 <= n <= 70:
            return 'D'
        case n if 51 <= n <= 60:
            return 'E'
        case _:
            return 'F'


def velg():
    print("""--------------------
1 - Emneliste
2 - Legg til Emne
3 - Sett karakter
4 - Karaktersnitt
5 - Avslutt
--------------------""")
    choice = input('Velg handling: ')
    match choice:  # bruker match case istedefor if/elif/else (Krever Python 3.10) syns det ser ryddigere ut.
        case '1':  # Match case ser mye ryddigere ut i denne sammenhengen, enn en rekke med if/elif/else statements imo.
            emneliste()
        case '2':
            add()
        case '3':
            karakter()
        case '4':
            karaktersnitt()
        case '5':
            for i in history[-3:]:
                print(i)
        case _:
            print('Velg 1-5.')
