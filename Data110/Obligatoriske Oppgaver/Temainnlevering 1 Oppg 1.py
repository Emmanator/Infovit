# Kan skrive navn her
fornavn = "Jakob"
mellomnavn = ""
etternavn = "Andreassen"

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
