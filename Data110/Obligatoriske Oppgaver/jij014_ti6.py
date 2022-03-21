import os


# Jeg gjorde både oppg 1 og 2 til funksjoner siden jeg syns det er ryddigere
# Oppgave 1
def add():  # En funksjon som skriver til telefon.txt
    tlf = open('telefon.txt', 'a')
    print('Legg til navn og nummer, avslutt med <enter>')
    while True:
        nytekst = input('Navn og nummer: ')
        if nytekst == '':  # if sjekk for å lukke programmet på enter
            tlf.close()
            return  # return før noe blir endret
        tlf.write(nytekst)
        tlf.write('\n')


# Oppgave 2
def endre():
    with open('telefon.txt', 'r') as f:
        with open('telefon_new.txt', 'w') as c:
            navn = input('Navn: ')
            for i in f:
                if i.startswith(navn):
                    split = i.split()
                    print(f'Gammelt telefonnummer: {split[-1]}')
                    ny_tlf = input('Nytt nummer: ')
                    c.write(f'{split[0]} {ny_tlf}\n')
                else:
                    c.write(i)
    os.remove('telefon.txt')
    os.rename('telefon_new.txt', 'telefon.txt')


# Oppgave 3
def fjernVokaler(text):  # bruker tekst variabel så det funker med flere filer
    with open(text, 'r', encoding='utf-8') as f:  # trenger utf-8 encoding for å kunne lese æøå
        with open(f'NY{text}', 'w', encoding='utf-8') as c:
            vokaler = "aeiouyæøåAEIOUYÆØÅ"
            for i in f.read():  # bruker read for å lese hver karakter i teksdokumentet
                if i not in vokaler:
                    c.write(i)





fjernVokaler('treSmåMusikanter.txt')
