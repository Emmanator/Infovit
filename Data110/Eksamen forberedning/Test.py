def f(x):  # tar altid in x og plusser det med y, uansett hva
    return x + y


def g(x, y):
    print(x - y)
    print(f(x - y))  # x - y er bare lokale variabler


x = 2
y = 3
g(y, x)  # følg nøye med hva argumentene er på eksamen
