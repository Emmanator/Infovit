import itertools

a = 1 * 2 + 3 > 1 + 2 * 3

print(a)

b = [[1, 2, 3, 4, 5, 6, 7, 8, 9][0]]

print(b)

c = {1: 2, 2: 4, 4: 8}[(1, 2, 4, 8)[1]]

print(c)

d = ['en', 'to', 'tre', 'fire']
d.sort(reverse=True)
print(d)

e = 'Hva gjør split?'.split()

print(e)


def B(x):
    return x > 5


resultat = [x + 1 for x in range(1, 11) if B(x)]
print(resultat)

resultat2 = list(map(lambda x: x + 1, filter(B, range(1, 11))))
print(resultat2)

resultat3 = []
for x in range(1, 11):
    if B(x):
        resultat3.append(x + 1)
print(resultat3)

print(1 + 2 * 2 + 1)
print(1 * '2' + 2 * '1')


def f(x):
    print(x)
    return x + 1


print(f(f(1)))

L = [0, 1, 2, 3, 4, 5]
print(L[2])

aldere = {'Liv': 5, 'Ola': 4, 'Ane': 5, 'Per': 6, 'Eli': 4, 'Jon': 5}


def finnAlle(fortegnelse, verdi):
    resultat = []
    for x in fortegnelse.items():
        if x[1] == verdi:
            resultat.append(x[0])
    return resultat


print(finnAlle(aldere, 5))

x1 = 6
y1 = 2


def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y


print(swap(x1, y1))


def fjernDuplikater(list1):
    nodupes = []
    for x in list1:
        if x not in nodupes:
            nodupes.append(x)
    return nodupes


print(fjernDuplikater([5, 7, 5, 3, 2, 7, 5]))

hester = ['Blakken', 'Svarten', 'Gampen']
ryttere = ['Kari', 'Ola']


def muligheter(list1, list2):
    a = [f'{n}, {l}' for (n, l) in itertools.product(list1, list2)]
    return a


print(muligheter(hester, ryttere))


def f(x):  # tar altid in x og plusser det med y, uansett hva
    return x + y


def g(x, y):
    print(x - y)
    print(f(x - y))  # x - y er bare lokale variabler


x = 2
y = 3
g(y, x)  # følg nøye med hva argumentene er på eksamen

sammenlagt = {}


def lesSammenlagt():
    global sammenlagt
    sammenlagt = {}
    with open("totalt.txt", 'r', encoding='utf-8') as s:
        for i in s:
            k, v = i.split(' ')
            sammenlagt[k] = int(v[:-1])


def oppdater(a):
    global sammenlagt
    temp = []
    with open(a, 'r', encoding='utf-8') as s:
        for i in s:
            temp.append(i[:-1])
    for navn in sammenlagt:
        if navn in temp[0]:
            sammenlagt[navn] += 10
        if navn in temp[1]:
            sammenlagt[navn] += 7
        if navn in temp[2]:
            sammenlagt[navn] += 5
        if navn in temp[3]:
            sammenlagt[navn] += 3
        if navn in temp[4]:
            sammenlagt[navn] += 1
    return


def skrivsammenlagt():
    with open('totalt.txt', 'w', encoding='utf-8') as s:
        for k, v in sammenlagt.items():
            s.write(f'{k} {v}')
            s.write('\n')


def plasseringSammendrag():
    inv_map = {}
    for k, v in sammenlagt.items():
        inv_map[v] = inv_map.get(v, []) + [k]

    for key in sorted(inv_map, reverse=True):
        print(key, "poeng:", " ".join(inv_map[key]))


lesSammenlagt()
print(sammenlagt)
plasseringSammendrag()
# 1
# L = (1, 2, 3)
# x = len(L)
# print(L[x])
# 2
# R = range(2, 4)
# print(R[R[1]])

# Punkt 3
fil = open('personer.txt')
tekst = fil.read()
fil.close()
x = {}
for y in tekst:
    for z in tekst.split():
        if y in z:
            x[y] = x.get(y, 0) + 1
for y in x: print(y, x[y])

fil = open('personer.txt')
P = None


# Punkt 4
class person:
    def __init__(self, f, e):
        self.fornavn = f
        self.etternavn = e
        self.n = None

    def skriv(self):
        x = P
        while x != None:
            if x.fornavn == self.fornavn:
                print(x.fornavn, x.etternavn)
            x = x.n


for l in fil:
    (x, y) = l.split()
    p = person(x, y)
    p.n = P
    P = p
fil.close()
P.skriv()

# Punkt 5
one = 1
ONE = 1
two = [2]
TWO = [2]
print(one is ONE and TWO is two)


