norsk = {1: 'en', 2: 'to', 3: 'tre', 4: 'fire', 5: 'fem', 6: 'seks', 7: 'sju', 8: 'åtte', 9: 'ni', 10: 'ti'}
engelsk = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
tysk = {1: 'eins', 2: 'zwei', 3: 'drei', 4: 'vier', 5: 'funf', 6: 'sechs', 7: 'sieben', 8: 'acht', 9: 'neun',
        10: 'zehn'}


def tallgloser(a, b, c):
    for i in range(1, 10):
        print(i, a[i], b[i], c[i])


tallgloser(norsk, engelsk, tysk)

s = 'en to tre fire fem seks sju åtte ni ti'


def f(t, b):
    r = []
    for o in t.split():
        if o.find(b) > -1: r.append(o)
    return r


print(f(s, 't'))


def oversett(tall, språk1, språk2):
    for n in språk1:
        if n == tall:
            return språk2[n]  # Om n er 4 så skal det returnere verdien til 4 i språk2 om jeg husker riktig :/
        else:
            print('Ugyldig tall: ', tall)


print(oversett(1, norsk, tysk))

tabell = [['Kari', 'Personalavdeling', '55667788'],  # Ser for meg at man skal stjele listen fra forrige oppgave
          ['Ola', 'Salgsavdeling', '55434332'],
          ['Liv', 'Produksjonsavdeling', '99231415'],
          ['Jens', 'Salgsavdeling', '55887777']]


def skrivTabell(tabell):
    for i in tabell:
        print((i[0].ljust(6)), i[1].ljust(30), i[2].ljust(8))


skrivTabell(tabell)


def lagTabell(tekstfil):
    nyansatte = []
    with open(tekstfil, 'r') as s:
        nyansatte = s
    return nyansatte


print(lagTabell('nyansatte.txt'))
