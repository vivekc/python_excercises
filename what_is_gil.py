# http://www.dabeaz.com/python/UnderstandingGIL.pdf
# http://www.dabeaz.com/python/GIL.pdf
from datetime import datetime
from threading import Thread

COUNT = 100000000


def countdown(n):
    while n >= 0:
        n -= 1


def print_time_diff(func):
    def timed(*arg, **kwargs):
        t1 = datetime.now()
        func(*arg, **kwargs)
        t2 = datetime.now()
        print str(t2 - t1)
    return timed


def threaded_count():
    t1 = datetime.now()
    thread1 = Thread(target=countdown, args=(COUNT//2,))
    thread2 = Thread(target=countdown, args=(COUNT//2,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    t2 = datetime.now()
    print str(t2 - t1)


# @print_time_diff
def nonthreaded_count():
    t1 = datetime.now()
    countdown(COUNT)
    t2 = datetime.now()
    print str(t2 - t1)


if __name__ == '__main__':
    nonthreaded_count()
    threaded_count()
