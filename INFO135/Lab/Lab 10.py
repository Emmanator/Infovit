# Exercise 1
def detailed_knap_sack(capacity, weights, values, n):
    sack = []
    grid = [[0 for x in range(capacity + 1)]
            for x in range(n + 1)]

    for item in range(n + 1):
        for cap in range(capacity + 1):

            if item == 0 or cap == 0:
                grid[item][cap] = 0

            elif weights[item - 1] <= cap:
                grid[item][cap] = max(values[item - 1] +
                                      grid[item - 1][cap - weights[item - 1]],
                                      grid[item - 1][cap])
            else:
                grid[item][cap] = grid[item - 1][cap]
    res = grid[len(weights)][capacity]

    w = capacity
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == grid[i - 1][w]:
            continue
        else:
            sack.append(weights[i - 1])
            res = res - values[i - 1]
            w = w - weights[i - 1]

    return f'${grid[n][capacity]} weights used: {sack}'


values = [120, 200, 150, 350, 100, 90]
weights = [15, 20, 40, 50, 20, 10]
capacity = 100

print(detailed_knap_sack(capacity, weights, values, len(values)))


# Exercise 2
class Car:

    def __init__(self, model, year, price, speed):
        self.model = model
        self.year = year
        self.price = price
        self.speed = speed

    def start(self):
        print('car started')

    def brake(self):
        print('car slow')

    def accelerate(self):
        print('car speedup')

    def get_price(self):
        print(f'price of car is {self.price}')


car = Car('6969', '20019', '30000', '400kph')
car.get_price()
car.start()
car.brake()
car.accelerate()

# Exercise 3
