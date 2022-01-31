# Oppgave 1
import math
# O = π * 2r kalkulerer arealet fra radius
r = float(input('Raidus:'))
a = math.pi * r ** 2

# printer a med 3 desimaler
print(f'Arealet til en sirkel med radius {r} er {a:.3f}.')

# Oppgave 2
# Benytter len() for å få en variabel som leser hvor mange bokstaver det er i sentence
sentence = str(input('Enter a sentence: '))
input_lengde = len(sentence)
guess = int(input('Guess the number of characters in previous input: '))

# Benytter if else statement til å se om du gjetter riktig.
if guess == input_lengde:
    print("That's correct!")
else:
    print("That's false!")

# Oppgave 3
import random
# tar input som en integer, random tall fra 1 til 100
tall = int(input('Gi meg et tall: '))
rand = random.randint(1 , 100)

# Setter verdien produsert av random og legger den bak input tallet
kombinert = int(str(tall) + str(rand))
# deler kombinert verdi på det originale tallet
print(kombinert / tall)
