# Oppgave 1
def antall_vokaler(tekst: str):
    teller = 0
    for i in tekst:
        if i in "aeiouyæøåAEIOUYÆØÅ":
            teller += 1
    return teller

# Oppgave 2
