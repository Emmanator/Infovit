class MyCar:
    brand = 'BMW'  # class variable

    def __init__(self, color):
        self.color = color  # Instance variable


class MyClass:

    def my_method(self):
        print('instance method', self)

    @classmethod
    def class_method(cls):
        print('class method', cls)

    @staticmethod
    def static_method():
        print('static method')


class Flight:
    total_num_of_pass = 0
    total_num_of_flight = 0

    def __init__(self, airline, num_of_pass):
        self.airline = airline
        self.num_of_pass = num_of_pass
        Flight.total_num_of_pass += num_of_pass
        Flight.total_num_of_flight += 1

    def print_num_of_pass(self):
        print(f'{self.airline}: {self.num_of_pass}')

    @classmethod
    def print_total_num(cls):
        print(f'{cls.total_num_of_pass}')

    @classmethod
    def print_avg_num_pass(cls):
        print(f'{cls.total_num_of_pass / cls.total_num_of_flight}')


class BankAccount:

    def __init__(self, number):
        self.number = number
        self.balance = 0
        # variabls that describe the state of the object

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class BankAccount2:

    def __init__(self, number):
        self.__number = number
        self.__balance = 0

    def get_number(self):  # Accessor (getter)
        return self.__number

    def set_number(self, new_number):  # Mutator (setter)
        self.__number = new_number


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        print(f'happy birthday, you were {self.age}')
        self.age += 1
        print(f'you are now {self.age}')


class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id

    def pay(self, hours):
        rate_of_pay = 7.5
        if self.age >= 21:
            rate_of_pay += 2.5
        return hours * rate_of_pay


class SalesPerson(Employee):
    def __init__(self, name, age, id, region, sales):
        super().__init__(name, age, id)
        self.region = region
        self.sales = sales

    def bonus(self):
        return self.sales * 0.5


my_person = Person('John', 20)
my_person.birthday()

my_employee = Employee('Sara', 22, 7766)
my_employee.birthday()

my_s_person = SalesPerson('David', 19, 9090, 'UK', 10000)
my_s_person.birthday()
print('paymen: ', my_s_person.pay(40))
print('bonus: ', my_s_person.bonus())


