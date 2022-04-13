# Hovedinnlevering 3
from random import *

# import itertools
# import pickle

deck = []


def kort():
    global deck
    a = 6
    # deck = list(itertools.product(['\u2665', '\u2663', '\u2666', '\u2660'], ['A', '7', '8', '9', '10', 'J', 'Q', 'K']
    for i in range(7, 15):
        a += 1
        if a > 9:
            deck.append(f'\u2665{i}')
            deck.append(f'\u2663{i}')
            deck.append(f'\u2666{i}')
            deck.append(f'\u2660{i}')
        else:
            deck.append(f'\u2665 {i}')
            deck.append(f'\u2663 {i}')
            deck.append(f'\u2666 {i}')
            deck.append(f'\u2660 {i}')


def stokk(splitt):
    shuffle(splitt)
    splitt = [splitt[x:x + 4] for x in range(0, len(splitt), 4)]
    return splitt


def fjern_par(c1, c2):
    global stokker
    bokstaver = list('ABCDEFGH')
    conv = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

    if c1 != c2 and c1 in bokstaver and c2 in bokstaver and stokker[conv[c1]][0][2:] == stokker[conv[c2]][0][2:]:
        stokker[conv[c1]].pop(0)
        stokker[conv[c2]].pop(0)
    else:
        print('Feil input, prøv igjen')


def victory(korts):
    if sum([len(x) for x in korts]) == 0:
        return True


def loss(korts):
    kopi = []
    for i in korts:
        try:
            kopi.append(int(i[0][2:]))
        except:
            continue

    tap_sjekk = set(kopi)
    if len(kopi) == len(tap_sjekk):
        return True


def lagre():
    return


def load():
    return


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
            for index, bunke in enumerate(korts):
                if len(bunke) > 0:
                    # test = f'{bokstaver[index]} [{bunke[0]}] {" " * (len(bunke[0]) % 2)}{"? " * len(bunke[1:])}'
                    # print(test)
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
        user = input('velg kort:').upper()
        if len(user) == 2:
            c1 = user[0]
            c2 = user[1]
            fjern_par(c1, c2)
        else:
            spill(korts)


kort()
stokker = stokk(deck)
spill(stokker)


def meny():
    valg = input('Velg handling')
    match valg:

