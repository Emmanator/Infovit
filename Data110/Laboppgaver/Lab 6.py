# Oppgave 1


class spillkort:
    spar = '\u2660'
    ruter = '\u2666'
    kløver = '\u2663'
    hjerter = '\u2665'
    symbols = [spar, ruter, kløver, hjerter]

    def __init__(self, ikon, tall):
        self.ikon = ikon
        self.tall = tall

    def skriv(self):
        kort = ""
        tall = self.tall
        if self.ikon in self.symbols:
            kort += self.symbols[self.ikon]
        else:
            return '?'
        if self.tall == 11:
            tall = 'J'
        elif self.tall == 12:
            tall = 'Q'
        elif self.tall == 13:
            tall = 'K'
        elif self.tall == 14:
            tall = 'A'
        print(f'{kort}{self.tall}')


sparTi = spillkort('spar', 10)
sparTi.skriv()


# Oppgave 2
class Person:
    fornavn = None
    etternavn = None
    gate = None
    poststed = None
    tlf = None

    def __init__(self, fornavn, etternavn, gate, poststed, tlf):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.gate = gate
        self.poststed = poststed
        self.tlf = tlf

    def skriv(self):
        print(f'{self.fornavn} {self.etternavn}, {self.tlf}, {self.gate}, {self.poststed}')


class Bil:
    platenr = None
    eier = None

    def __init__(self, platenr, eier):
        self.platenr = platenr
        self.eier = eier

    def skriv(self):
        print(f'{self.platenr} eier: {self.eier.fornavn} {self.eier.etternavn}')


kari = Person('Kari', 'Normann', 'Tullevei 9', '9876 Tøysedal', 98765432)
per = Person('Per', 'Hansen', 'Nedvei 5', '9855 Oppberg', 99778891)
liv = Person('Liv', 'Larsen', 'Skolegata 1', '9887 Småby', 55664499)
bil1 = Bil('ab49218', kari)
bil2 = Bil('el81331', liv)
bil3 = Bil('yz54321', per)
bil4 = Bil('st87654', kari)
biler = [bil1, bil2, bil3, bil4]


# kari.skriv()
# for bil in biler:
#     bil.skriv()


# Oppgave 3
class KapasitetVakt:
    kapasitet = 0
    max_cap = 0

    def __init__(self, kapasitet):
        self.kapasitet = kapasitet
        self.max_cap = self.kapasitet

    def kommer(self, kommer):
        if kommer > self.kapasitet:
            print(f'For mange! slipp inn {self.kapasitet}')
            kommer = self.kapasitet
        self.kapasitet -= kommer

    def går(self, går):
        current_people = self.max_cap - self.kapasitet
        if går > current_people:
            print(f'hvordan kom det flere enn {self.max_cap}, det er jo maks capasitet')
            går = current_people
        self.kapasitet += går

    def ledig(self):
        print(self.kapasitet)


lokale1 = KapasitetVakt(10)
lokale2 = KapasitetVakt(15)


# lokale1.kommer(4)
# lokale2.kommer(5)
# lokale2.kommer(2)
# lokale1.ledig()
# lokale2.ledig()
# lokale1.kommer(9)
# lokale1.ledig()
# lokale1.går(5)
# lokale1.ledig()

# Oppgave 4a
class Konto:
    kontonummer = None
    innehaver = None
    saldo = None
    rentesats = None

    def __init__(self, kontoNr, innehaver, saldo=0, rentesats=1.5):
        self.kontonummer = kontoNr
        self.innehaver = innehaver
        self.saldo = saldo
        self.rentesats = rentesats

    def skriv(self):
        print(self.kontonummer, '(' + str(self.rentesats) + '):',
              self.saldo, ', Innehaver: ' + self.innehaver)

    def innskudd(self, beløp):
        self.saldo = self.saldo + beløp

    def uttak(self, beløp):  # returnerer False dersom det ikke er dekning.
        if beløp > self.saldo:
            print('Ikke dekning')
            return False
        else:
            self.saldo = self.saldo - beløp
            return True

    def endre_rentesats(self, ny_sats):
        self.rentesats = ny_sats
        print(f'sats er nå {ny_sats}')

    def rente_oppgjøret(self):
        renteverdi = self.saldo * self.rentesats
        self.saldo = renteverdi
        return renteverdi

    def overfør(self, mengde, destinasjon):
        if mengde > self.saldo:
            print('F')
            return
        self.saldo -= mengde
        destinasjon.saldo += mengde


konto1 = Konto(123, 'tomtom', 500, 1.5)
konto2 = Konto(321, 'temtem', 500, 1.5)


# konto1.skriv()
# konto2.skriv()
# konto2.overfør(600, konto1)
# konto1.skriv()
# konto2.skriv()

# Oppgave 4b
class Bank:
    antall_kontoer = 0
    bank_navn = None
    kontoer = []
    innskudd_rente = None

    def __init__(self, bank_navn, kontoliste=[], rente=1.0):
        self.bank_navn = bank_navn
        self.kontoer = kontoliste
        self.innskudd_rente = rente

    def skriv(self):
        print(f'{self.bank_navn} ({str(self.innskudd_rente)}). Kontoer:')
        for k in self.kontoer:
            k.skriv()

    def sett_rente(self, ny_rente):
        self.innskudd_rente = ny_rente

    def ny_konto(self, innehaver, saldo):
        self.antall_kontoer += 1
        self.kontoer.append(Konto(self.antall_kontoer, innehaver, saldo, self.innskudd_rente))

    def fjern_konto(self, konto_nr):
        self.kontoer.remove(konto_nr)

    def renteoppgjør(self):
        for i in self.kontoer:
            self.saldo *= self.innskudd_rente

    def overfør(self, mengde, destinasjon):
        if mengde > self.saldo:
            print('F')
            return
        self.saldo -= mengde
        destinasjon.saldo += mengde


# Oppgave 5
class kø:
    waitinglist = []

    def sett_inn(self, navn):
        self.waitinglist.append(navn)

    def skriv(self):
        for i in self.waitinglist:
            print(i)

    def ta_ut(self):
        if not self.waitinglist:
            print('Køen er tom')
        else:
            print(f'Tar ut {self.waitinglist.pop(0)} fra køen')

    def neste(self):
        if not self.waitinglist:
            print('ingen i køen lol')
        else:
            print(self.waitinglist[0])


# venteliste = kø()
# venteliste.sett_inn('Per')
# venteliste.sett_inn('Kari')
# venteliste.sett_inn('Liv')
# venteliste.skriv()
# venteliste.ta_ut()
# venteliste.sett_inn('Cum')
# venteliste.skriv()
# venteliste.ta_ut()
# venteliste.neste()
# venteliste.ta_ut()
# venteliste.skriv()
# venteliste.ta_ut()
# venteliste.ta_ut()
# venteliste.neste()
# venteliste.neste()


# Oppgave 6
class Fibb:
    fibb1 = 1
    fibb2 = 0

    def neste(self):
        result = self.fibb1

        b = self.fibb1 + self.fibb2
        self.fibb2 = self.fibb1
        self.fibb1 = b

        return result


# c = Fibb()
# for i in range(10):
#     print(c.neste())

# Oppgave 7
class person:
    navn = None
    far = None
    mor = None

    def __init__(self, navn, far=None, mor=None):
        self.navn = navn
        self.far = far
        self.mor = mor

    def skriv(self):
        print(self.navn)


def forgjenere(person, kjede: str):
    for f in kjede:
        match f:
            case 'F':
                if person.far == None:
                    print('kjeden er for lang')
                    break
                person = person.far
            case 'M':
                if person.mor == None:
                    print('kjeden er for lang')
                    break
                person = person.mor
            case _:
                print('Ikke gyldig input')
                break
        person.skriv()


##testdata
anders = person('Anders')
anna = person('Anna')
tor = person('Tor')
guri = person('Guri')
kjell = person('Kjell')
olaug = person('Olaug')
arne = person('Arne')
solveig = person('Solveig')
jens = person('Jens', anders, anna)
liv = person('Liv', tor, guri)
petter = person('Petter', kjell, olaug)
sara = person('Sara', arne, solveig)
ola = person('Ola', jens, liv)
kari = person('Kari', petter, sara)
per = person('Per', ola, kari)

forgjenere(per, 'MFF')