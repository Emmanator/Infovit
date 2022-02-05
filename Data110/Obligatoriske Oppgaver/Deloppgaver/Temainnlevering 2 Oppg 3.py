# Oppgave 3
import random
# tar input som en integer, random tall fra 1 til 100
tall = int(input('Gi meg et tall: '))
rand = random.randint(1 , 100)

# Setter verdien produsert av random og legger den bak input tallet
kombinert = int(str(tall) + str(rand))
# deler kombinert verdi på det originale tallet
print(kombinert / tall)
