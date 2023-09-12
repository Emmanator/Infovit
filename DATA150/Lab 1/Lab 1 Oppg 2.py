import pandas as pd

gutter = pd.read_csv('guttenavn.csv', sep=';')
juni = pd.read_csv("juni.csv", sep='\t')

# a)
jenter = pd.read_csv("jentenavn.csv", sep=';')
# print(jenter)

# b)
a = jenter.shape
antallK = a[1]
antallR = a[0]


# c)
# print(jenter.iloc[[0, -1]])

# d)
# print(jenter[['fornavn', '2000']])


# e)
def skrivSerie(s):
    verdier = s.values.tolist()
    linje = ''
    for v in verdier:
        linje = linje + ' ' + str(v)
    print(linje, sep=' ', end='\n')


def skrivRamme(r):
    kol = r.columns.tolist()
    overskrift = ''
    for k in kol: overskrift = overskrift + ' ' + str(k)
    print(overskrift)
    for i in range(0, r.shape[0]):
        skrivSerie(r.iloc[i])

skrivSerie(jenter.iloc[0])
skrivRamme(jenter[:10])

# f)

