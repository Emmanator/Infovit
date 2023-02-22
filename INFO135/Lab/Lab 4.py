import math

# Exercise 1

n = 8949
# a)
print(n)


# b)
# c)

# Exercise 2
def one_pass(liste, index):
    sub_liste = liste[index:]
    smallest = min(sub_liste)
    smallest_index = sub_liste.index(smallest) + index
    liste[index], liste[smallest_index] = liste[smallest_index], liste[index]
    return liste


def more_pass(liste):
    for i in range(len(liste) - 1):
        one_pass(liste, i)
    return liste


liste = [-4, 0, 1, 9, 0]

# liste = [1]
print(more_pass(liste))

# Exercise 3
nuts = ['@', '#', '$', '%', '^', '&']
bolts = ['$', '%', '&', '^', '@', '#']


def nuts_and_bolts(a, b):
    nuts = []
    bolts = []
    for i in a:
        for j in b:
            if i == j:
                nuts.append(i)
                bolts.append(j)

    print(nuts)
    print(bolts)
    return


nuts_and_bolts(nuts, bolts)
