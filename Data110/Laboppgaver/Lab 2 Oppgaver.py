# Oppgave 2
# n = (int(input('Fra:')))
# m = (int(input('Til:')))

# Oppgave 3
import random

tegn = '?' * (random.randint(10,60))
print(tegn)
lengde = len(tegn)
svar = int(input("Guess the number of ?s: "))

if svar == lengde:
    print("That's correct!")
else:
    print("That's false!")
