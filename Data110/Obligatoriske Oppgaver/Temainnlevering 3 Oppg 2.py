# Oppgave 3
import math
alder = int(input('Oppgi alder: '))
bodd = int(input('Hvor mange år har du bodd i Tulleby?: '))

bystyre_akrav = 25
bystyre_bkrav = 5
ordfører_akrav = 30
ordfører_bkrav = 9

# Alderskrav
bystyre = bystyre_akrav - alder
ordfører = ordfører_akrav - alder
# Bodkrav
bybkrav = bystyre_bkrav - bodd
ordbkrav = ordfører_bkrav - bodd

print(bystyre, ordfører, bybkrav, ordbkrav)
if alder >= 30 and bodd >= 9:
    print('Du kan bli ordfører eller sitte i bystyret.')
elif alder >= 26 and bodd >= 5 > 9:
    print('Du kan sitte i bystyret.')
    print(f'Prøv igjen om {ordbkrav} år for å bli ordfører.')
elif alder >= 25 and bodd >= 9:
    print('Du kan sitte i bystyret.')
    print(f'Prøv igjen om {max(ordfører, ordbkrav)} år for å bli ordfører.')




else:
    print('Du er ikke kvalifisert enda,')
