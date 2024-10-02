# https://stackoverflow.com/questions/7542957/is-python-capable-of-running-on-multiple-cores




#!/usr/bin/env python3

# Compare single proc vs multiple procs execution for cpu bound operation

"""
Typical Result:
  Starting 1000000 cycles of cpu-only processing
  Sequential run time: 9.24 seconds
  4 procs Parallel - run time: 2.59 seconds
  2 procs Parallel twice - run time: 4.76 seconds
"""
import time
import multiprocessing as mp

# how many cycles
cycles = 1000 * 1000 * 300



def t():
    for x in range(cycles):
        fdivision = cycles / 2.0
        fcomparison = (x > fdivision)
        faddition = fdivision + 1.0
        fsubtract = fdivision - 2.0
        fmultiply = fdivision * 2.0

if __name__ == '__main__':


    # four procs
    start_time = time.time()
    p1 = mp.Process(target=t)
    p2 = mp.Process(target=t)
    p3 = mp.Process(target=t)
    p4 = mp.Process(target=t)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    print("  4 procs Parallel - run time: %.2f seconds" % (time.time() - start_time))




