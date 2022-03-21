# filbehandling
tlf = open('../telefon.txt', 'r')


def telefon():
    search = input('Navn: ')
    split = list(tlf)
    converted_nummer = []
    nummer = []
    for k in split:
        converted_nummer.append(k.strip())
    for i in converted_nummer:
        if i.startswith(search):
            jobb = i.split(' ')
            nummer.append(jobb[-1])
    return nummer


print(telefon())


# STORE BOKSTAVER
