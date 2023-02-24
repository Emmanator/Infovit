import pandas as pd

df = pd.DataFrame(pd.read_csv("russia-investigation.csv"))
# df.apply(lambda row: print(dict(row)), axis=1)


df.shape
df.index  # ...and list(df.index)
print(df.columns)
df['name']
# print(df.president)
# print(df.loc[3])
print(df.loc[1]['name'])
c = 1


def aaaa(b):
    print(b)


def task2(row):
    return row.apply(aaaa(c), axis=1)


task2(df)
