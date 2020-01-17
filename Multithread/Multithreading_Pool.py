import logging
# Pool, more efficient to use than traditional thread or queues, can apply lambda operators
# using apply, map, async_apply, then connect using .join()
import multiprocessing as mp

from fib import fibonacciNotRecursive


format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

if __name__ == "__main__":

    pool = mp.Pool(processes=4)
    logging.info("Processing start")

    results = [pool.apply(fibonacciNotRecursive, args=(x,)) for x in range(1, 10000)]
    print(len(results))
    with open('fNumbers','w') as f :
        for item in results:
            f.write(f"{item}")
    logging.info("Processing ended")
    f.close()
