# Exercise 1
# a) <- Is the answer
from abc import ABC, abstractmethod


# Exercise 2
class QuizGift:

    def compute_result(self):
        capacity = 100
        weights = [15, 20, 40, 50, 20, 10]
        values = [120, 200, 150, 350, 100, 90]
        n = len(values)

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

        return grid[n][capacity]

    def print_result(self):
        print(f'Points: {self.compute_result()}')
        if self.compute_result() < 250:
            print('Sara obtains watch! :(')
        elif self.compute_result() <= 750:
            print('Sara obtains smartphone! :)')
        else:
            print('Sara obtains laptop! :D')


p = QuizGift()
p.print_result()


# Exercise 3
class Shape(ABC):

    @abstractmethod
    def compute_area(self):
        pass


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def compute_area(self):
        return self.side * self.side


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return 3.14 * self.radius * self.radius


class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def compute_area(self):
        s = (self.a + self.b + self.c) / 2
        area = s * (s - self.a) * (s - self.b) * (s - self.c)
        return area ** 0.5


square1 = Square(2)
print(square1.compute_area())

circle1 = Circle(2)
print(circle1.compute_area())

triangle1 = Triangle(3, 4, 5)
print(triangle1.compute_area())

# Exercise 4
class House:
    count = 0

    def __init__(self, owner, price, condition):
        self.owner = owner
        self.price = price
        self.condition = condition
        self.cost = 0
        self.sold = False
        House.count += 1

    def sell(self, new_owner):
        self.owner = new_owner
        self.sold = True
        print(f'Profit = {self.price - self.cost}')

    def change_price(self, new_price):
        if self.sold:
            print('House has been sold! :(')
        else:
            self.price = new_price

    def renovate(self, expense, new_condition):
        self.cost = self.cost + expense
        self.condition = new_condition
        print('House renovated! :)))')

    def print_info(self):
        print(f'Owner: {self.owner}, Condition: {self.condition}, Price: {self.price} [$]')

house1 = House('John', 100000, 'Good')
house2 = House('Sara', 250000, 'Bad')

house1.renovate(100000, 'Bad')
house1.sell('Carl')

house1.print_info()
house2.print_info()
print(f'Total houses: {House.count}')