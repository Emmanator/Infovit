# Hovedinnlevering 3
import pickle  # Brukt for å lagre spillet
import itertools  # Brukt for å stokke decket
from random import *  # Brukt for å stokke decket


# import pickle

# Reglene til spillet osv. er plassert i en class. Kan gjør det lettere å kunne gjøre om interfacet til spillet til
# tkinter som vi har lært om i TI7.
class TheWish:
    deck = []

    def __init__(self, filename=None):
        if filename is None:
            symboler = ['\u2665', '\u2663', '\u2666', '\u2660']
            tall = ['A', '7', '8', '9', '10', 'J', 'Q', 'K']
            temp = [n + l.rjust(2) for (n, l) in itertools.product(symboler, tall)]
            shuffle(temp)
            self.deck = [temp[x:x + 4] for x in range(0, len(temp), 4)]
        else:
            self.deck = pickle.load(open(filename, 'rb'))

    def fjern_par(self, c1, c2):
        conv = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

        if c1 != c2 and c1 in conv and c2 in conv and self.deck[conv[c1]][0][2:] == self.deck[conv[c2]][0][2:]:
            self.deck[conv[c1]].pop(0)
            self.deck[conv[c2]].pop(0)
        else:
            print('Feil input, prøv igjen')

    def victory(self):
        if sum([len(x) for x in self.deck]) == 0:  # Ser om det ikke er noen kort igjen for å se om du vinner
            return True

    def loss(self):
        kopi = []
        for i in self.deck:
            if i:
                kopi.append((i[0][1:]))

        tap_sjekk = set(kopi)  # set() gjør at alle er unike
        if len(kopi) == len(tap_sjekk):     # så om lengden til kopi = lengden til tap_sjekk
            print(kopi, tap_sjekk)          # så er det ingen unike kort igjen og spiller taper.
            print(len(kopi), len(tap_sjekk))
            return True

    # Bruker pickle som lagre funksjon for å beholde hvordan deck listen ser ut mellom sesjoner
    # Gjør at staten av deck listen blir bevart, noe jeg ikke tror er mulig i en vanlig txt fil
    def lagre(self, filename):
        pickle.dump(self.deck, open(filename, 'wb'))


def spill(game):
    bokstaver = list('ABCDEFGH')
    while True:
        if game.victory():
            print('nicenice, du vinner')
            break
        elif game.loss():
            print('du tapte')
            break
        else:
            game.lagre('The Wish_autosave.p')
            for index, bunke in enumerate(game.deck):
                if len(bunke) > 0:
                    print(f'  {bokstaver[index]}  ', end='')
                else:
                    print(f'  {bokstaver[index]}  ', end='')
            print()
            for index, bunke in enumerate(game.deck):
                if len(bunke) > 0:
                    print(f'[{bunke[0]}]', end='')
                else:
                    print(f'[   ]', end='')
            print()
            for index, bunke in enumerate(game.deck):
                if len(bunke) > 0:
                    print(f'  {len(bunke)}  ', end='')
                else:
                    print(f'  0  ', end='')
        print()
        user = input('velg kort (x for å avbryte):').upper()
        if user == 'X':
            break
        elif len(user) == 2:
            c1 = user[0]
            c2 = user[1]
            game.fjern_par(c1, c2)


def meny():
    print("""--------------------
1 - start nytt spill
2 - lagre spillet
3 - hent lagret spill
4 - hent autosave
5 - avslutt
Velg handling
--------------------""")


def start():
    game = None
    meny()
    while True:
        valg = input('Velg handling (0 for meny): ')
        match valg:
            case '0':
                meny()
            case '1':
                game = TheWish()
                spill(game)
            case '2':
                game.lagre('The Wish.p')
            case '3':
                game = TheWish('The Wish.p')
                spill(game)
            case '4':
                game = TheWish('The Wish_autosave.p')
                spill(game)
            case '5':
                return
            case _:
                print('Velg 0-4')


start()
