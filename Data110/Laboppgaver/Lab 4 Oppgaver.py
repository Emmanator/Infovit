# Oppgave 1
# a)
# def myndig(alder):
#     if alder >= 18:
#         print('you can drink')
#     else:
#         print("you can't drink")

# b)
import random


def myndig(alder):
    return alder >= 18


if myndig(17):
    print('you can drink')
else:
    print("you can't drink")


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


print(tilfeldigKort())
