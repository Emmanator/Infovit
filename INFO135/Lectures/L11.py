from abc import ABC, abstractmethod


# Example of pass for error handling
class DVDPlayer(ABC):

    @abstractmethod
    def insert_dvd(self, dvd):
        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Example of using the abstract methods
class ZiDVDPlayer(DVDPlayer):

    def __int__(self):
        self.is_playing = False

    def insert_dvd(self, dvd):
        self.dvd = dvd

    def play(self):
        self.is_playing = True

    def stop(self):
        self.is_playing = False

    def print_state(self):
        print('DVD is playing?', self.is_playing)


# Exceptions using student marks & averages
def compute_avg(marks):
    assert len(marks) != 0, "List is empty"
    return sum(marks) / len(marks)


try:
    marks_1 = [1, 5, 5, 3, 4]
    print("Average", compute_avg(marks_1))

    marks_2 = []
    print("Average:", compute_avg(marks_2))
except AssertionError as msg:
    print(msg)


# Inheritance
class Family:
    def family(self):
        print("This is my Family:")


class Parent(Family):
    def father(self):
        print(self.fathername)

    def mother(self):
        print(self.mothername)


class Child(Parent):
    def parent(self):
        print(f'Father: {self.fathername}')
        print(f'Mother: {self.mothername}')


child = Child()
child.fathername = "John"
child.mothername = "Sara"
child.parent()


class AudioFile(object):
    file_ext = ''

    def __init__(self, filename):
        if not filename.endswith(self.file_ext):
            raise Exception('Invalid Format')

        self.filename = filename


class MP3File(AudioFile):
    file_ext = 'mp3'

    def play(self):
        print(f'Playing {self.filename} as Mp3')


class WavFile(AudioFile):
    file_ext = 'wav'

    def play(self):
        print(f'Playing {self.filename} as wav')


# n x n matrix
total_sum = 0
for i in range(n):
    row_sum[i] = 0

    for j in range(n):
        row_sum[i] = row_sum[i] + matrix[i, j]

    total_sum = total_sum + row_sum[i]
