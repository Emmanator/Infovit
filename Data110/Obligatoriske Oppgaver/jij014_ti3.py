# Oppgave 1
# 1. a) Når x = 9 og y = 66 returnerer x != 7 and y <= 50 False
#       og (x > 7 or 50 < y) and (x > y or y < 100) returnerer True
# 2. b) not(not((x != 7 and y <= 50))
#       not(x == 7 or y > 50)


# Oppgave 2
alder = int(input('Oppgi alder: '))
bodd = int(input('Hvor mange år har du bodd i Tulleby?: '))

bystyre_akrav = 25
bystyre_bkrav = 5
ordfører_akrav = 30
ordfører_bkrav = 9

# Alderskrav
# Bruker krav variablene definert tiligere fpr å gjøre enkle matte utregninger
bystyre = bystyre_akrav - alder
ordfører = ordfører_akrav - alder
# Bodkrav
bybkrav = bystyre_bkrav - bodd
ordbkrav = ordfører_bkrav - bodd

# if, elif, else statements som skjekker hva din alder er kommer tilbake med
# en respons for hvor mange år til man blir kvalifisert.
if alder >= 30 and bodd >= 9:
    print('Du kan bli ordfører eller sitte i bystyret.')
elif alder >= 25 and bodd >= 5:
    print('Du kan sitte i bystyret.')
    print(f'Prøv igjen om {max(ordfører, ordbkrav)} år for å bli ordfører.')
else:
    print('Du er hverken kvalifisert til å sitte i bystyret eller ordfører.')
    print(f'Kvalifisert til bystyret om {max(bystyre,bybkrav)} år eller ordfører om {max(ordfører, ordbkrav)}.')

# Oppgave 3
x = int(input('Tall:'))
if x > 5 and x < 10:
    print('6,7,8 eller 9')
elif x >= 10:
    print('minst 10')
else:
    print('max 5')
