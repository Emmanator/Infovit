# Hovedinnlevering 3
import pickle
import itertools
from random import *

# import pickle

deck = []


def kort():
    global deck
    deck = []
    symboler = ['\u2665', '\u2663', '\u2666', '\u2660']
    tall = ['A', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [n + l.rjust(2) for (n, l) in itertools.product(symboler, tall)]


def stokk(splitt):
    global deck
    shuffle(splitt)
    splitt = [splitt[x:x + 4] for x in range(0, len(splitt), 4)]
    deck = splitt
    return splitt


def fjern_par(c1, c2):
    global deck
    bokstaver = list('ABCDEFGH')
    conv = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

    if c1 != c2 and c1 in bokstaver and c2 in bokstaver and deck[conv[c1]][0][2:] == deck[conv[c2]][0][2:]:
        deck[conv[c1]].pop(0)
        deck[conv[c2]].pop(0)
    else:
        print('Feil input, prøv igjen')


def victory(korts):
    if sum([len(x) for x in korts]) == 0:
        return True


def loss(korts):
    kopi = []
    for i in korts:
        if i:
            kopi.append((i[0][1:]))

    tap_sjekk = set(kopi)
    if len(kopi) == len(tap_sjekk):
        print(kopi, tap_sjekk)
        print(len(kopi), len(tap_sjekk))
        return True


# Bruker pickle som lagre funksjon for å beholde hvordan deck listen ser ut mellom sesjoner
# Gjør at staten av deck listen blir bevart, noe jeg ikke tror er mulig i en vanlig txt fil
def lagre(kort2):
    pickle.dump(kort2, open('The Wish.p', 'wb'))
    return


def last_inn():
    global deck
    try:
        deck = pickle.load(open('The Wish.p', 'rb'))
        spill(deck)
    except FileNotFoundError:
        print('Fant ingen lagret fil')


# Auto-lagring funksjon, blir brukt i spill funksjonen før vært trekk
# Tenker det kan være greit å kunne lagre uten å måtte gjøre det manuelt
# Fra et kode perspektiv så er det basically det samme som den forrige greia da :/
def autosave(kort2):
    pickle.dump(kort2, open('The Wish_autosave.p', 'wb'))


def last_inn_autosave():
    global deck
    try:
        deck = pickle.load(open('The Wish_autosave.p', 'rb'))
        spill(deck)
    except FileNotFoundError:
        print('Fant ingen autosave')


def spill(korts):
    bokstaver = list('ABCDEFGH')
    while True:
        if victory(korts):
            print('nicenice, du vinner')
            break
        elif loss(korts):
            print('taper altså')
            break
        else:
            autosave(korts)
            for index, bunke in enumerate(korts):
                if len(bunke) > 0:
                    print(f'  {bokstaver[index]}  ', end='')
                else:
                    print(f'  {bokstaver[index]}  ', end='')
            print()
            for index, bunke in enumerate(korts):
                if len(bunke) > 0:
                    print(f'[{bunke[0]}]', end='')
                else:
                    print(f'[   ]', end='')
            print()
            for index, bunke in enumerate(korts):
                if len(bunke) > 0:
                    print(f'  {len(bunke)}  ', end='')
                else:
                    print(f'  0  ', end='')
        print()
        user = input('velg kort (x for å avbryte):').upper()
        if user == 'X':
            start()
            break
        elif len(user) == 2:
            c1 = user[0]
            c2 = user[1]
            fjern_par(c1, c2)
        else:
            spill(korts)


def meny():
    print("""--------------------
1 - start nytt spill
2 - lagre spillet
3 - hent lagret spill
4 - hent automatisk lagret spill
5 - avslutt
Velg handling (0 for meny)
--------------------""")


def start():
    global deck
    meny()
    while True:
        valg = input('Velg handling: ')
        match valg:
            case '0':
                meny()
            case '1':
                kort()
                spill(stokk(deck))
            case '2':
                lagre(deck)
            case '3':
                last_inn()
                spill(deck)
            case '4':
                last_inn_autosave()
                spill(deck)
            case '5':
                return
            case _:
                print('Velg 0-4')


start()
