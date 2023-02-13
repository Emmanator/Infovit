# MAD Hashing
from random import randrange


def mad_hash(key):
    m = 12000
    p = 10934511
    a = 1 + randrange(p - 1)
    b = randrange(p)
    return (a * key + b) % p % m


class Employee:
    def __init__(self, id_number):
        self.id_number = id_number

    def __eq__(self, other):
        return self.id_number == other.id_number

    def __hash__(self):
        return hash(self.id_number)


employee1 = Employee('i8123786')
employee2 = Employee('1i82383')


# print(employee1.__hash__())


# Bad Hashing model
class Car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def __eq__(self, other):
        return self.model == other.model \
            and self.brand == other.brand

    def __hash__(self):
        return self.model \
            * ord(self.brand[0]) \
            * ord(self.brand[1]) \
            * ord(self.brand[2]) \
            * ord(self.brand[3])


# SHA Hashing
import hashlib as hl


def hash_it_by_shal(user_str):
    hash_str = hl.sha1(user_str.encode()).hexdigest()
    return hash_str
