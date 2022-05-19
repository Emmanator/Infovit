# Hovedinnlevering 2
# liste og dictionary på starten som fylles opp med load() funksjonen.
import os

emner = []
karakterer = {}
fagområde = {}


# Siden mitt.uib ikke lar meg levere textfiler filer så har jeg inkludert en funksjon som lager et sett tekst filer
# med noen eksempel verdier
def create_default_file():
    global emner
    global karakterer
    global fagområde

    # Funksjonen ser etter filene og om den ikke finner en av de så genererer den nye tekstfiler.
    if not (os.path.exists('jij014_hi2_emner.txt')) or not (os.path.exists(
            'jij014_hi2_fagområde.txt')) or not (os.path.exists('jij014_hi2_karakterer.txt')):
        emner = ['INFO100', 'INFO104', 'ECON100', 'JAP100', 'JAP110', 'INFO120', 'INFO125', 'KOGVIT101', 'JAP120',
                 'ECON200', 'ECON220', 'ECON240', 'ECON300', 'ECON320', 'ECON3240', 'GEO125']
        karakterer = {'INFO100': 'C', 'INFO104': 'B', 'ECON100': 'B', 'JAP100': 'C', 'JAP110': 'C', 'KOGVIT101': 'B',
                      'ECON300': 'F', 'ECON320': 'A', 'ECON340': 'B', 'INFO125': 'B'}
        fagområde = {'JAP': 'japansk', 'INFO': 'informasjonsvitenskap', 'ECON': 'økonomi',
                     'KOGVIT': 'kognitivvitenskap', 'GEO': 'geografi'}
        lagre()


def lagre():  # denne funksjonen skriver all informasjonen i listen og dictionary til en text fil
    with open('jij014_hi2_emner.txt', 'w', encoding='utf-8') as a:  # utf-8 encoding for å lese æøå
        for i in emner:
            a.write(i)
            a.write('\n')  # \n for å indikere ny linje i tekstdokumentet

    with open('jij014_hi2_fagområde.txt', 'w', encoding='utf-8') as s:
        for k, v in fagområde.items():
            s.write(f'{k} {v}')  # legger til mellomrom for å splitte elementene senere
            s.write('\n')

    with open('jij014_hi2_karakterer.txt', 'w', encoding='utf-8') as s:
        for k, v in karakterer.items():
            s.write(f'{k} {v}')
            s.write('\n')


def load():  # Laster inn data fra tekstfiler og legger de til listen/dictionary på starten
    global emner
    global karakterer
    global fagområde

    emner = []
    with open('jij014_hi2_emner.txt', 'r', encoding='utf-8') as a:
        for i in a:
            emner.append(i[:-1])  # :-1 for å fjerne \n karakteren

    karakterer = {}
    with open('jij014_hi2_karakterer.txt', 'r', encoding='utf-8') as s:
        for i in s:
            k, v = i.split(' ')
            karakterer[k] = v[:-1]

    fagområde = {}
    with open('jij014_hi2_fagområde.txt', 'r', encoding='utf-8') as s:
        for i in s:
            k, v = i.split(' ')
            fagområde[k] = v[:-1]


def hent_emner(area: str | None, level: str | None) -> list[str]:
    matching = []

    for i in emner:
        area_code = i[:-3]
        if (area is None or fagområde[area_code] == area) and (level is None or i[-3] == level[0]):
            print(i)
            matching.append(i)

    return matching


def hent_karakter(to_grade: list[str]) -> dict[str, str | None]:
    graded = {}

    for i in to_grade:
        if i in karakterer:
            graded[i] = karakterer[i]
        else:
            graded[i] = None
    return graded


def vis_gradert(graded: dict[str, str | None]):
    for sub in sorted(graded.keys()):
        if graded[sub] is None:
            print(sub)
        else:
            print(f'{sub} {graded[sub]}')


def add():
    nytt_emne = input('Nytt emne(<enter> for å avbryte): ')

    # Ser om nytt_emne sin fagkode er en gyldig key i fagområde, ellers så spør det om et gyldig emne.
    while nytt_emne[:-3] not in fagområde.keys() and nytt_emne != '':
        nytt_emne = str(input('Nytt emne (Må være gyldig emne, <enter> for å avbryte): '))
    if nytt_emne == '':
        return

    emner.append(nytt_emne)


def karakter_sett():
    emne2 = input('Emne (<enter> for å avbryte): ')

    while emne2 not in emner and emne2 != '':
        emne2 = input('Må være et gyldig emne (<enter> for å avbryte): ')
    if emne2 == '':  # Metode for å unngå å sitte fast i denne funksjonen.
        return

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


# bruker funskoner for å hente hvilket fag/nivå av fag brukeren ønsker
# gjør det lettere å bruke koden flere ganger som i handling 1 og 4
def fagområde_get():
    field = input('Fag: ')
    while field != '' and field not in fagområde.values():
        field = input('Fag (må være gyldig emne): ')
    field = field or None
    return field


def nivå_get():
    nivå = input('Nivå: ')
    while nivå != '' and nivå[0] not in ['1', '2', '3']:  # forsikrer at det er et gyldig nivå
        nivå = input('Nivå (må være gyldig nivå: ')  # skjekker bare starten av nivå tallet
    nivå = nivå or None
    return nivå


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
    meny()  # meny() og load() kjøres en gang på starten av funksjonen
    create_default_file()
    load()

    while True:
        choice = input('Velg handling (0 for meny): ')
        match choice:  # bruker match case istedefor if/elif/else (Krever Python 3.10) syns det ser ryddigere ut.
            case '0':
                meny()  # for å vis menyen igjen
            case '1':
                print('Velg fag og/eller emnenivå (<enter> for alle): ')
                field = fagområde_get()
                nivå = nivå_get()

                a = hent_emner(field, nivå)
                b = hent_karakter(a)
                vis_gradert(b)
            case '2':
                add()
            case '3':
                karakter_sett()
            case '4':
                print('Velg fag og/eller emnenivå (<enter> for alle): ')
                field = fagområde_get()
                nivå = nivå_get()

                a = hent_emner(field, nivå)
                b = hent_karakter(a)
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
