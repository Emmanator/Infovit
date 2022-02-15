# Oppgave 1
speed = int(input('Hva var farten: '))
bot = 1000
bonus_bot = 100
fartsgrense = 50

if speed > fartsgrense:
    kostnad = bot + (bonus_bot * (speed - fartsgrense))
    print(f'du får {kostnad}kr i bot siden du kjørte over fartsgrensen: {speed}km/t')
else:
    print('ingen bot')

# Oppgave 2
