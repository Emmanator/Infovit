# Oppgave 1
def siste(last):
    return last[-1]


# Oppgave 2
def skrivSekvens(last):
    s = ''
    for i in last:
        s += f'{i}\t'
    if s == '':
        return s
    return s[:-1]


# Oppgave 3
def sifferHøyre(num):
    # digits = [int(d) for d in str(num)]
    digits = map(int, str(num))
    return sum(digits)


# Oppgave 4
def lesHelltall(meldinger, Min=None, Max=None):
    for i in meldinger:
        tall = int(input(i))
        if (Min is None or tall >= Min) and (Max is None or tall <= Max):
            return tall
    return 'you fail'


# Oppgave 5
def kapasitetVakt(kapasitet):
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

