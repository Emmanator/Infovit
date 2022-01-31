# Oppgave 1
import math
# O = π * 2r kalkulerer arealet fra radius
r = float(input('Raidus:'))
a = math.pi * r ** 2

# printer a med 3 desimaler
print(f'Arealet til en sirkel med radius {r} er {a:.3f}.')

# Oppgave 2
# Benytter len() for å få en variabel som leser hvor mange bokstaver det er i sentence
sentence = str(input('Skriv en setning: '))
input_lengde = len(sentence)
guess = int(input('Gjett antall bokstaver '))

# Benytter if else statement til å se om du gjetter riktig.
if guess == input_lengde:
    print("Det er korrekt!")
else:
    print("Det er feil!")

# Oppgave 3
import random  # Liker å ha imports på toppen av scriptet, men har den her for oppgavens skyld.
tall = int(input('Gi meg et tall: '))  # tar bare integer inputs
rand = random.randint(1, 100)  # random tall fra 1 til 100

# Setter verdien produsert av random og legger den bak input tallet
kombinert = int(str(tall) + str(rand))
# deler kombinert verdi på det originale tallet
print(kombinert / tall)
