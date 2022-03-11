# Oppgave 1
def antall_vokaler(tekst: str):
    teller = 0
    for i in tekst:
        if i in "aeiouyæøåAEIOUYÆØÅ":
            teller += 1
    return teller


# Oppgave 2
TV = \
"""
Tulleveien Velforening
leder: Kari
kasserer: Ole
IT-ansvarlig: Liv
parkeringsansvarlig: Kari
arrangementsansvarlig: Liv
hagekonsulent: Kari
brannansvarlig: Kari
"""
# Hadde det ikke vært mye bedre og lagret vervene som en variabel og navn som en variabel
# 

def verv(navn: str):
    split = list(TV.splitlines())
    roller = []
    for i in split:
        if i.endswith(navn):
            jobb = i.split(':')
            roller.append(jobb[0])
    return roller


print(verv('Liv'))
