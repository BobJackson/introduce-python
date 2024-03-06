import multiprocessing
import time
import os


def whoami(what):
    print('Process %s says: %s' % (os.getpid(), what))


def loopy(name):
    whoami(name)
    start = 1
    stop = 100_0000
    for num in range(start, stop):
        print("\tNumber %s of %s. Honk!" % (num, stop))
        time.sleep(1)


if __name__ == '__main__':
    whoami("I'm main")
    p = multiprocessing.Process(target=loopy, args=("I'm loopy",))
    p.start()
    time.sleep(5)
    p.terminate()
