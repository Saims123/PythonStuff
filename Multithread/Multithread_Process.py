# Multi-threading
# M.Threading : Shared heap memory with multiple threads running within 1 process
# Requires Global Interpreter Lock, prevents conflict between Ts, execute one at a time
###

import logging
import threading
import time
# Multi-threading sample
from fib import fibonacci, fibonacciNotRecursive

def print_fibonacci_output(n, isRecursive: bool):
    if isRecursive:
        print(f'Recursive algorithm : {fibonacci(n)}')
    else :
        print(f'Non-recursive algorithm : {fibonacciNotRecursive(n)}')

def thread_function(name):
    print("Initiate threading : ")
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    number = 10

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=('Special',), daemon=True)
    x.start()
    logging.info("Main    : before running thread")

    logging.info("Main    : wait for the thread to finish")

    logging.info("Main    : all done")

    thread1 = threading.Thread(target=print_fibonacci_output, args=(number,True,))
    thread2 = threading.Thread(target=print_fibonacci_output, args=(number,False,))
    # Run in Parallel
    thread1.start()
    thread2.start()

    # Join+Run in Parent process
    thread1.join()
    x.join()
    thread2.join()
