# Oppgave 2
alder = int(input('Oppgi alder: '))
bodd = int(input('Hvor mange år har du bodd i Tulleby?: '))

bystyre_akrav = 25
bystyre_bkrav = 5
ordfrer_akrav = 30
ordfrer_bkrav = 9

# Alderskrav
# Bruker krav variablene definert tiligere fpr å gjøre enkle matte utregninger
bystyre = bystyre_akrav - alder
ordfrer = ordfrer_akrav - alder
# Bodkrav
bybkrav = bystyre_bkrav - bodd
ordbkrav = ordfrer_bkrav - bodd

# if, elif, else statements som skjekker hva din alder er kommer tilbake med
# en respons for hvor mange år til man blir kvalifisert.
if alder >= 30 and bodd >= 9:
    print('Du kan bli ordfører eller sitte i bystyret.')
elif alder >= 25 and bodd >= 5:
    print('Du kan sitte i bystyret.')
    print(f'Prøv igjen om {max(ordfrer, ordbkrav)} år for å bli ordfører.')
else:
    print('Du er hverken kvalifisert til å sitte i bystyret eller ordfører.')
    print(f'Kvalifisert til bystyret om {max(bystyre,bybkrav)} år eller ordfører om {max(ordfrer, ordbkrav)}.')
