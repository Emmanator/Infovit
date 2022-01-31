# Oppgave 1
# Exercise 1
x = 5
print(x + 1)

# Exercise 2
name = input('Enter your name:')
print(f'Hello {name}')

# Exercise 3
hours = int(input('input hours:'))
rate = int(input('input rate:'))
print('Pay =', (hours * rate))

# Exercise 4
width = 17
height = 12
print(width // 2)
print(width / 2.0)
print(height / 3)
print(1 + 2 * 5)

# Exercise 5
# Fra celsius til fahrenheit °F = (°C × 9/5) + 32
# Fra fahrenheit til celsius °C = (°F − 32) × 5/9
celsius = int(input('Enter Celsius:'))

# Celsius til Fahrenheit
CtF = (celsius * 9/5) + 32
print(f'{celsius:.2f}\N{degree celsius} = {CtF:.2f}\N{degree fahrenheit}')