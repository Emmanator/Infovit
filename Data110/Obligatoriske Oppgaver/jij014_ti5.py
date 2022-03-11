# Oppgave 1
def antall_vokaler(tekst: str):
    teller = 0
    for i in tekst:
        if i in "aeiouyæøåAEIOUYÆØÅ":  # skjekker bare om i er i vokal lista og legger til +1 til teller
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


def verv(navn: str):
    split = list(TV.splitlines())   # splitter for hver line i mutli-line stringen ovenfor
    roller = []                     # list variabel for å appende til
    for i in split:                 # siden split gjør det om til en liste er "i" hver linje i TV
        if i.endswith(navn):        # skjekker for linjer som slutter med navn
            jobb = i.split(':')     # splitter på kolon tegnet
            roller.append(jobb[0])  # legger til det venstre elementet fra forrige splitt
    return roller


print(verv('Liv'))
