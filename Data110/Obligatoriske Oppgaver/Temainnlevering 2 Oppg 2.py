# Oppgave 2
# benytter len() for å få en variabel som leser hvor mange bokstaver det er i sentence
sentence = str(input('Enter a sentence: '))
input_lengde = len(sentence)
guess = int(input('Guess the number of characters in previous input: '))

# Benytter if else statement til å se om du gjetter riktig.
if guess == input_lengde:
    print("That's correct!")
else:
    print("That's false!")

