# Kroner til Euro/Dollar kurs 25.01.2022
euro_kurs = 0.098
dollar_kurs = 0.11
kroner = 250

# Definerer konverterte variabler
euro_kon = kroner * euro_kurs
dollar_kon = kroner * dollar_kurs

# Print hva X kroner er i euro og dollar etter kurs variabel
# Hadde lyst til å få med 2 desimaler siden det er det som står i oppgaveteksten
print(f'{kroner} kroner tilsvarer {euro_kon:.2f} Euro og {dollar_kon:.2f} Dollar.')
print(f'{kroner} NOK tilsvarer {euro_kon:.2f}\N{euro sign} og {dollar_kon:.2f}\N{dollar sign}.')
