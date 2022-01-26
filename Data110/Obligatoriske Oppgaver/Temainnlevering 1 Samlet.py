# Oppgave 1
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

# Oppgave 1 V2
# Hvorfor må vi gjøre den samme oppgaven 2 ganger? :v
# Jeg har ikke mellomnavn så fjernet den variabelen i dette eksemplet av å printe for/etternavn
print(fornavn, etternavn, sep='\n')

# Oppgave 2
# Bruker """""" for multiline string print
print(
"""
    *       *      *  *   ***   ****
    *      * *     * *   *   *  *   *
    *     *****    **    *   *  ****
*   *    *     *   * *   *   *  *   *
 ***    *       *  *  *   ***   * **
""")


# Oppgave 3
# Kroner til Euro/Dollar kurs 25.01.2022
euro_kurs = 0.098
dollar_kurs = 0.11
kroner = 250

# # Definerer konverterte variabler
euro_kon = kroner * euro_kurs
dollar_kon = kroner * dollar_kurs

# Print hva X kroner er i euro og dollar etter kurs variabel
# Hadde lyst til å få med 2 desimaler siden det er det som står i oppgaveteksten
print(f'{kroner} kroner tilsvarer {euro_kon:.2f} Euro og {dollar_kon:.2f} Dollar.')
print(f'{kroner} NOK tilsvarer {euro_kon:.2f}\N{euro sign} og {dollar_kon:.2f}\N{dollar sign}.')

