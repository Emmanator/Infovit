emner = []
karakterer = {}
fagområde = {}


def get_subjects(area: str | None, level: str | None) -> list[str]:
    matching = []

    for i in emner:
        area_code = i[:-3]
        if (area is None or fagområde[area_code] == area) and (level is None or i[-3] == level[0]):
            matching.append(i)

    return matching


def get_graded_subjects(to_grade: list[str]) -> dict[str, str | None]:
    graded = {}

    for i in to_grade:
        if i in karakterer:
            graded[i] = karakterer[i]
        else:
            graded[i] = None

    return graded


def show_graded(graded: dict[str, str | None]):
    for sub in sorted(graded.keys()):
        if graded[sub] is None:
            print(sub)
        else:
            print(f'{sub} {graded[sub]}')


def add():
    global emner
    nytt_emne = str(input('Nytt emne: '))
    emner.append(nytt_emne)
    return


def karakter_sett():
    emne2 = input('Emne: ')
    while emne2 not in emner:
        emne2 = input('Må være et gyldig emne: ')

    sett_karakter = input('Karakter (<enter> for å slette): ')
    while sett_karakter not in ['A', 'B', 'C', 'D', 'E', 'F', '']:
        sett_karakter = input('Må være karakter A-F: ')

    if sett_karakter == '':
        if emne2 in karakterer:
            del karakterer[emne2]
        return

    karakterer[emne2] = sett_karakter


def karaktersnitt(graded):
    global karakterer
    nummer = 0
    abc_grade = {'A': 96, 'B': 86, 'C': 76, 'D': 66, 'E': 56, 'F': 50}
    le = 0
    for i in graded.values():
        if i is None:
            continue
        a = abc_grade[i]
        nummer += a
        le += 1
    kalk = nummer / le
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


def field_get():
    field = input('Fag: ')
    while field != '' and field not in fagområde.values():
        field = input('Fag (må være gyldig emne): ')
    field = field or None
    return field


def nivå_get():
    nivå = input('Nivå: ')
    while nivå != '' and nivå[0] not in ['1', '2', '3']:
        nivå = input('Nivå (må være gyldig nivå: ')
    nivå = nivå or None
    return nivå


def lagre():
    with open('hi2_emner.txt', 'w', encoding='utf-8') as a:
        for i in emner:
            a.write(i)
            a.write('\n')
    with open('hi2_fagområde.txt', 'w', encoding='utf-8') as s:
        for k, v in fagområde.items():
            s.write(f'{k} {v}')
            s.write('\n')
    with open('hi2_karakterer.txt', 'w', encoding='utf-8') as s:
        for k, v in karakterer.items():
            s.write(f'{k} {v}')
            s.write('\n')


def last():
    global emner
    global karakterer
    global fagområde

    emner = []
    with open('hi2_emner.txt', 'r', encoding='utf-8') as a:
        for i in a:
            emner.append(i[:-1])

    karakterer = {}
    with open('hi2_karakterer.txt', 'r', encoding='utf-8') as s:
        for i in s:
            k, v = i.split(' ')
            karakterer[k] = v[:-1]

    fagområde = {}
    with open('hi2_fagområde.txt', 'r', encoding='utf-8') as s:
        for i in s:
            k, v = i.split(' ')
            fagområde[k] = v[:-1]


def meny():
    print("""--------------------
1 - Emneliste
2 - Legg til Emne
3 - Sett karakter
4 - Karaktersnitt
5 - Avslutt
6 - Lagring
--------------------""")


def start():
    meny()
    last()
    while True:
        choice = input('Velg handling (0 for meny)> ')
        match choice:  # bruker match case istedefor if/elif/else (Krever Python 3.10) syns det ser ryddigere ut.
            case '0':
                meny()
            case '1':
                print('Velg fag og/eller emnenivå (<enter> for alle)')
                field = field_get()
                nivå = nivå_get()

                a = get_subjects(field, nivå)
                b = get_graded_subjects(a)
                show_graded(b)
            case '2':
                add()
            case '3':
                karakter_sett()
            case '4':
                print('Velg fag og/eller emnenivå (<enter> for alle)')
                field = field_get()
                nivå = nivå_get()

                a = get_subjects(field, nivå)
                b = get_graded_subjects(a)
                print(karaktersnitt(b))
            case '5':
                save = input('Vil du lagre endringene? (j/n) ')
                if save == 'j':
                    lagre()
                return
            case '6':
                lagre()
            case _:
                print('Velg 0-6.')


start()
