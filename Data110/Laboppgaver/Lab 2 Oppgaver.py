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
import sys
# int(input)) aksepterer bare integers så trenger ikke å skape error melding enda
tst = int(input('Skriv et tresifret tall:'))

if len(str(tst)) != 3:  # Skjekker om tst er 3 karakterer lang
    print("Error! må være 3 karakterer")
    sys.exit()

# matte magi
s1 = ((tst % 100) % 10)
s2 = ((tst // 10) % 10)
s3 = (tst // 100)
print(f'Permutasjoner: '
      f'{s3}{s2}{s1},'
      f'{s3}{s1}{s2},'
      f'{s2}{s3}{s1},'
      f'{s2}{s1}{s3},'
      f'{s1}{s3}{s2},'
      f'{s1}{s2}{s3}.')
