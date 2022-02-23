# Oppgave 1
class dørvakt:


def kapasitetvakt(kapasitet):
    max_cap = kapasitet
        case 1:
            kommer = int(input('Hvor mange kommer?: '))
            if come > kapasitet:
                print(f'Not enough space, only {kapasitet} spots left')
                come = kapasitet
            kapasitet -= come
            print(f'{kapasitet}')
        case 2:
            leave = int(input('Hvor mange går?: '))
            current_people = max_cap - kapasitet
            if leave > current_people:
                print(f'wtf bro that is more than {max_cap} only {current_people} can leave')
                leave = current_people
            kapasitet += leave
            print(f'{kapasitet}')
        case 0:
            return 'takk for nå'
        case _:
            print('oh god oh fuck, input again')
