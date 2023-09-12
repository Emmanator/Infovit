import seaborn as sns
import matplotlib.pyplot as plt

sns.get_dataset_names()
utbrudd = sns.load_dataset('geyser')
# print(utbrudd)

# a)
plt.hist(utbrudd['duration'], bins=10)


# b)
plt.scatter(utbrudd['duration'], utbrudd['waiting'])

# c)
penguins = sns.load_dataset('penguins')
print(penguins)
penguinsM = penguins[penguins['sex']=='Female']['flipper_length_mm']
penguinsF = penguins[penguins['sex']=='Male']['flipper_length_mm']
plt.hist([penguinsM,penguinsF], bins=20, color=['blue', 'green'])

plt.show()