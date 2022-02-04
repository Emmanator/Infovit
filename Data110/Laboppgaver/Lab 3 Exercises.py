# Exercise 1, 2
while True:
    try:
        hours = int(input('Enter hours: '))
        rate = float(input('Enter rate: '))
    except ValueError: # Om det blir error spør den om informasjonen igjen.
        print('Må skrive tall')
        continue
    else:
        # Ayy takk for at du skrev et nummer lmao
        break

pay = hours * rate
if hours > 40:
    overtimerate = 0.5 * rate
    overtime = (hours - 40) * overtimerate
    print(pay + overtime)
else:
    print(pay)

# Exercise 3

# Read score, if score is above 1 or not a numerical input prompt the user to try again
while True:
    try:
        score = float(input('Please insert score: '))
    except ValueError:
        print('please insert number')
        continue
    if score > 1.00:
        print('bad score')
        continue
    else:
        break

if score == 1:
    print('Perfect score!')
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else:
    print('F')