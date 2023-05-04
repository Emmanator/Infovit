# Concurrency
# Multi-threading

import time
from threading import Thread


def my_function(sleep_time):
    print('a')
    time.sleep(sleep_time)
    print('a')


my_thread = Thread(group=None, target=None, name=None, args=(), kwargs={})

thread1 = Thread(target=my_function, args=[1])
thread2 = Thread(target=my_function, args=[1])

start = time.perf_counter()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end = time.perf_counter()
print(round(end - start, 1))

# Process
from multiprocessing import Process

my_process = Process(group=None, target=None, name=None, args=(), kwargs={})

if __name__ == '__main__':
    my_process.start()
    my_process.join()
