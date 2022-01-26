# 1.
# Exercise 1:
# Secondary memory: lagrer programmer og data, og holder på data når strømmer er av. svar: c
# Exercise 2: et program er et sett med instrukser som spesifiserer en komputasjon
# Exercise 3: Compiler translates high-level language into low-level language all at once. Interpreter does it one line
#             at a time
# Exercise 4: Svaret er c)
# Exercise 5: Bruker "primt" istedefor "print"
# Exercise 6: b) main memory
# Exercise 7: it will print 44

# 2.
# i) syntaks feil ii) syntakst feil iii) logisk feil iv) utregningen er plassert før variabler er definert
# v) ??? hvem er syk nokk til å skrive dette vi) logisk feil

# b) skriv de rette programmet for å regne ut kvinneandelen

antallStudenter = 55
antallKvinner = 32
kvinneAndel = antallKvinner/antallStudenter
print(f'kvinneandelen er {kvinneAndel:.2f}')

# 3.
# Fra celsius til fahrenheit °F = (°C × 9/5) + 32
# Fra fahrenheit til celsius °C = (°F − 32) × 5/9
celsius = 15.56
fahrenheit = 60

# Celsius til Fahrenheit
CtF = (celsius * 9/5) + 32
# Fahrenheit til Celsius
FtC = (fahrenheit - 32) * 5/9

print(f'{fahrenheit:.2f}\N{degree fahrenheit} tilsvarer {FtC:.2f}\N{degree celsius}')
print(f'{celsius:.2f}\N{degree celsius} tilsvarer {CtF:.2f}\N{degree fahrenheit}')

print(f'{celsius:.2f}\N{degree celsius} = {CtF:.2f}\N{degree fahrenheit}')
print(f'{fahrenheit:.2f}\N{degree fahrenheit} = {FtC:.2f}\N{degree celsius}')
