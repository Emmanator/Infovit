# Oppgave 2
# n = (int(input('Fra:')))
# m = (int(input('Til:')))

# Oppgave 3
# import random
#
# tegn = '?' * (random.randint(10,60))
# print(tegn)
# lengde = len(tegn)
# svar = int(input("Guess the amount of ?: "))
#
# if svar == lengde:
#     print("That's correct!")
# else:
#     print("That's false!")
# print(f'{lengde} is the correct answer.')

# Oppgave 4
# import math
#
# n = int(input('Tall 1: '))
# m = int(input('Tall 2: '))
# nm = int(str(n) + str(m))
# mn = int(str(m) + str(n))
# print(f'{nm} og {mn}')
# print(f'Kvadraroten av {nm} * {mn} er {math.sqrt(mn * nm):.2f}')

# Oppgave 5
tre_sifret_tall = int(input('skriv et tresifret tall: '))
s1 = ((tre_sifret_tall % 100) % 10)

print(s1)