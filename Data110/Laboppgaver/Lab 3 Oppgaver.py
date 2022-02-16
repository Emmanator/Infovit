# Oppgave 1
import sys

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
navn = input('Navn: ')
alder = int(input('Alder: '))
kjønn = input('Kjønn (M/I/K): ')
barn = int(input('Antall barn: '))
vandel = int(input('Vandel, på skala fra 1(dårlig) til 9(plettfri): ' ))
rulleblad = input('Rulleblad (straffet/tiltalt/mistenkt/rent): ')
senioritet = int(input('Ansiennitet (år): '))
nøytrale_navn = ['Kristen', 'Kim', 'Janne', 'Tony']
guttenavn = ['Jakob']


if kjønn in ['M', 'I']:
    print('du er ikke kvinne')
    sys.exit()
print(f'{navn} er kvalifisert for: ')
if alder >= 20 and vandel <= 6:
    print('Støttemedlem')
if alder <= 30 and barn == 0:
    print('Soldat')
    if senioritet >= 4 and rulleblad != 'rent':
        print('Sersjant')
if alder <= 40 and senioritet >= 6 and rulleblad in ['straffet', 'tiltalt']:
    print('Kapteiner')
    if vandel <= 2 and rulleblad in ['straffet']:
        print('Kommandanter')
        if senioritet >= 8 and navn not in nøytrale_navn + guttenavn:
            print('President')

# Oppgave 3
year = int(input('år: '))

if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
    print('Skuddår')
else:
    print('assår')


# Oppgave 4
letters = input('a-h: ').lower()
numbers = int(input('1-8: '))

board = (ord(letters) - ord('a')) + numbers

if board % 2 == 0:
    print('White tile')
else:
    print('black tile')

# Oppgave 5
kode = 'cum'
attempt = input('input kode: ') == kode or input('try again loser: ') == kode

if attempt:
    print('haha you win, you get cum')
else:
    print('no cum for you!!!!!!!!')

# Oppgave 6
import sys

success = False

for i in range(2):
    teller = int(input('teller: '))
    nevner = int(input('nevner: '))
    if teller < 0 or teller > 100 or nevner < 0 or nevner > 100:
        print('haha you failed, try again')
        continue
    else:
        success = True
        break

if success:
    print('we can do things now')
    print(f'{teller} / {nevner} = {teller / nevner}')
else:
    print('how are you this bad at this')
    sys.exit()

# Oppgave 7
import random

options = ['papir', 'saks', 'stein']
jeg = input('Velg papir,saks eller stein:')
maskin = random.choice(options)


print('Maskinen velger', maskin)
if jeg == maskin:
    print('uavgjort')
elif (jeg == 'papir' and maskin == 'stein') or \
    (jeg == 'saks' and maskin == 'papir') or \
    (jeg == 'stein' and maskin == 'saks'):
    print('du vant')
else:
    print('maskinen vant')
