# Oppgave 1
def faktorial1(n):  # Rekursiv funksjon
    if n <= 1:
        return 1
    else:
        return faktorial1(n - 1) * n


def faktorial2(n):  # for-løkke
    fak = 1
    for i in range(1, n + 1):
        fak *= i
    return fak


def faktorial3(n):  # while-løkke
    fak = 1
    while n != 1:
        fak *= n
        n -= 1
    return fak


# Oppgave 2
class Monark:
    nasjon = None
    navn = None
    fra = None
    etterkommer = None

    def __init__(self, nasjon, navn, fra, etterkommer=None):   # Etterkommer trenger et argument eller så krasjer det
        self.nasjon = nasjon                                   # når det ikke er en etterkommer.
        self.navn = navn
        self.fra = fra
        self.etterkommer = etterkommer

    def settEtterfølger(self, neste):   # Funksjon som lar deg endre hvem etterfølgeren er, tar neste argumentet slik
        self.etterkommer = neste        # haakon.settEtterfølger(olav) og endrer etterkommer til ny verdi

    def skriv(self):  # hele denne greia er mega jank, men gjør hva som ønskes av oppgaven.
        if self.etterkommer is None:
            print(f'{self.navn} av {self.nasjon}, tiltrådt: {self.fra}')
        else:
            print(f'{self.navn} av {self.nasjon}, tiltrådt: {self.fra}, etterfølger: {self.etterkommer.navn}')


harald = Monark("Norge", "Kong Harald V", 1991)
olav = Monark("Norge", "Kong Olav V", 1957, harald)
haakon = Monark("Norge", "Kong Haakon VII", 1905, olav)
kongerekke = [haakon, olav, harald]

for m in kongerekke:
    m.skriv()
