# Oppgave 1.1
# Kan skrive navn her
fornavn = input('Enter first name:')
mellomnavn = input('Enter middle name (if applicable):')
etternavn = input('Enter your last name:')

# Om mellomnavn er tomt så blir denne printet
if mellomnavn == "":
    print(
        fornavn,
        etternavn,
        sep='\n')

# Om mellom navn ikke er tomt så blir denne printet
else:
    print(
        fornavn,
        mellomnavn,
        etternavn,
        sep='\n')