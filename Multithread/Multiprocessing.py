# M.Processing : Uses Multiple CPU => seperate memory space => Bypass GIL, child processes are killable
# Harder to share data between processes, larger memory footprint, inter-process communication are harder with complex overhead
# Multi Processing are more for CPU bounded bottlenecks
import multiprocessing as multiprocessing
import random
import string
import logging

threadCount = 6
random.seed(123)

# Define an output queue
output = multiprocessing.Queue()

# define a example function


def rand_string(length, output):
    """ Generates a random string of numbers, lower- and uppercase chars. """
    rand_str =  ''.join(random.choice(
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits)
        for i in range(length))
    output.put(rand_str)


if __name__ == "__main__":
    # Setup a list of processes that we want to run
    processes = [multiprocessing.Process(target=rand_string, args=(6, output)) for x in range(threadCount)]

    # Run processes
    for p in processes:
        p.start()

    # Exit the completed processes
    for p in processes:
        p.join()

# Get process results from the output queue
    results = [output.get() for p in processes]

    print(results)
