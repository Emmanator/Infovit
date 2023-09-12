import pandas as pd

# Oppgave 1
dataA = pd.DataFrame({'Emnekode': ['DATA110', 'DATA120', 'DATA130', 'DATA140', 'DATA150'],
                      'Tittel': ['Innføring i programmering', 'Databaser', 'Strukrert Data', 'Rå-Data', 'Datasett'],
                      'Studiepoeng': [10, 5, 5, 5, 5]})

dataB = dataA.set_index('Emnekode')

print(dataA)
print(dataB)

# c)
a = dataA.at[4, 'Studiepoeng']
b = dataB.at['DATA150', 'Studiepoeng']
print(a)
print(b)

# d)
dataA['Karakter'] = ['A', 'B', 'C', 'D', 'A']
dataA.drop(columns='Studiepoeng', inplace=True)
print(dataA)

# e)
dataB.drop(index='DATA150', inplace=True)
dataB.loc['DATA170'] = ['Innføring i R', 5]
print(dataB)

# f)
dataB['Studiepoeng'] = dataB['Studiepoeng'] + 5
print(dataB)

# g)
dataB.loc['DATA120', 'Tittel'] = 'Tabelldata'
print(dataB)

# h)
print(dataA['Karakter'].nunique())

# i)
print(dataA['Karakter'].value_counts())

# j)
dataA['Karakter'] = dataA['Karakter'].str.replace('A', 'Hurra')
# (dataA)
