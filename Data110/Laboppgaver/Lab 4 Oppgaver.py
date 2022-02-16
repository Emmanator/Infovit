# Oppgave 1
# a)
# def myndig(alder):
#     if alder >= 18:
#         print('you can drink')
#     else:
#         print("you can't drink")

# b)
def myndig(alder):
    return alder >= 18

if myndig(17):
    print('you can drink')
else:
    print("you can't drink")

# Oppgave 2
def siffer(tall, n):
    return int(str(tall)[n - 1])

# Oppgave 3
def fullname(firstname, lastname, middlename = None):
    if middlename is None:
        print(firstname, lastname)
    else:
        print(firstname, middlename, lastname)

# Oppgave 4
