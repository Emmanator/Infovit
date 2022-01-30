# Oppgave 1 Eksempel 1:
# Kan skrive navn her
# Vurderte å brukebruke "input()" funksjon for dette, men Siden dere ønsker alt samlet i en fil
# så har jeg skrevet variabler for fornavn, mellomnavn og etternavn på forhånd
# fornavn = input('Enter first name:')
# mellomnavn = input('Enter middle name (if applicable):')
# etternavn = input('Enter your last name:')
fornavn = "Jakob"
mellomnavn = ""
etternavn = "Andreassen"

# Om mellomnavn er tomt så blir denne printet
if mellomnavn == "":
    print(fornavn, etternavn, sep='\n')

# Om mellom navn ikke er tomt så blir denne printet
else:
    print(fornavn, mellomnavn, etternavn, sep='\n')

# Oppgave 1 Eksempel 2:
# Hvorfor må vi gjøre den samme oppgaven flere ganger? :v
# Jeg har ikke mellomnavn så fjernet den variabelen i dette eksemplet av å printe for/etternavn
print(fornavn, etternavn, sep='\n')

# Oppgave 1 Eksempel 3:
# Benytter """""" for multiline string print
print("""Jakob
Andreassen""")

# Oppgave 1 Eksempel 4:
# Enkel metode for å printe flere strings samtidig.
print("Jakob", "Andreassen", sep='\n')

# Oppgave 2:
# Bruker """""" for multiline string print
print("""
    *       *      *  *   ***   ****
    *      * *     * *   *   *  *   *
    *     *****    **    *   *  ****
*   *    *     *   * *   *   *  *   *
 ***    *       *  *  *   ***   * **
    """)

# Oppgave 3a:
# Kroner til Euro/Dollar kurs 28.01.2022 (finn.no valutakalkulator)
kroner = 250
euro_kurs = 0.099
dollar_kurs = 0.111

# Definerer konverterte variabler
nok_til_euro = kroner * euro_kurs
nok_til_dollar = kroner * dollar_kurs

# Print hva X kroner er i euro og dollar etter kurs variabel
# Bruker print(f'{tekst:.2f}') for å få med 2 desimaler siden det er det som står i oppgaveteksten
print(f'{kroner} kroner tilsvarer {nok_til_euro:.2f} Euro og {nok_til_dollar:.2f} Dollar.')
# Oppgave 3b:
print(f'{kroner} NOK tilsvarer {nok_til_euro:.2f}\N{euro sign} og {nok_til_dollar:.2f}\N{dollar sign}.')
