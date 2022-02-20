# Avsnitt 4.14 (Python for Everyone)
# Exercise 1

# Oppgave 1
# a)
def myndig(alder):
    if alder >= 18:
        print('you can drink')
    else:
        print("you can't drink")


# b)
def myndig(alder):
    return alder >= 18


# if myndig(17):
#     print('you can drink')
# else:
#     print("you can't drink")


# Oppgave 2
def siffer(tall, n):
    return int(str(tall)[n - 1])


# Oppgave 3
def fullname(firstname, lastname, middlename=None):
    if middlename is None:
        print(firstname, lastname)
    else:
        print(firstname, middlename, lastname)


# Oppgave 4
import random


Spar = '\u2660'
Ruter = '\u2666'
Kløver = '\u2663'
Hjerter = '\u2665'
farger = [Spar, Ruter, Kløver, Hjerter]
tall = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def tilfeldigKort(kort=None):
    if kort is None:
        kort = random.choice(farger)
    return kort + random.choice(tall)


# Oppgave 5
num2words = {
    1: 'En', 2: 'To', 3: 'Tre', 4: 'Fire', 5: 'Fem',
    6: 'Seks', 7: 'Sju', 8: 'Åtte', 9: 'Ni', 10: 'Ti',
    11: 'Elve', 12: 'Tålv', 13: 'Tretten', 14: 'Fjorten',
    15: 'Femten', 16: 'Seksten', 17: 'Søtten', 18: 'Atten',
    19: 'Nitten', 20: 'Sjue', 30: 'Tredve', 40: 'Førti',
    50: 'Femti', 60: 'Sexti', 70: 'Søtti', 80: 'Åtti',
    90: 'Nitti', 0: 'Null'
}


def n2w(number):
    global num2words
    if 0 <= number <= 19 or number % 10 == 0:
        return num2words[number]
    else:
        tens = (number // 10) * 10
        digit = number % 10
        return f'{num2words[tens]}{num2words[digit].lower()}'


# Oppgave 6
def sorter3(a, b, c):
    # if b<=a: a,b=b,a
    # if b>c: b,c=c,b
    # if b<=a: a,b=b,a
    # print(x,y,z)
    if a <= b <= c:
        return f'{a} {b} {c}'
    if a <= c <= b:
        return f'{a} {c} {b}'
    if b <= a <= c:
        return f'{b} {a} {c}'
    if b <= c <= a:
        return f'{b} {c} {a}'
    if c <= a <= b:
        return f'{c} {a} {b}'
    if c <= b <= a:
        return f'{c} {b} {a}'


# Oppgave 7
def oppskrift():
    valg = input('Hva vil du ha til middag? ')
    print("""bland mel, gjær og vann
kna grundig og la heve i 1 time
brun kjøttdeig på middels varme
hell over tomatsaus og la det koke opp
kjevle ut deigen i en sirkel""")
    if valg == 'pizza':
        print("""fordel fyllet utover hele deigen
strø på revet ost
stek i 15 minutter ved 200 grader""")
    if valg == 'calzone':
        print("""fordel fyllet på halve deigen
brett over den andre halvparten og
klem kantene sammen
stek i 20 minutter ved 220 grader""")


# Oppgave 8
