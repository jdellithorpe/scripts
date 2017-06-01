#!/usr/bin/env python

"""
Script which reads a CSV file of data measurements (specified on the command
line) and output stats on those numbers (sum, average, variance, standard
deviation, min, max, 50th/90th/95th/99th percentile, etc.)
"""

from __future__ import division, print_function
from sys import argv,exit
import re
import numpy as np

def read_csv_into_list(filename):
    """
    Read a csv file of floats, concatenate them all into a flat list and return
    them.
    """
    numbers = []
    for line in open(filename, 'r'):
        if not re.match('([0-9]+\.[0-9]+) ', line):
            for value in line.split(","):
                numbers.append(float(value))
    return numbers
    
def print_stats(filename):
    """
    Read data values from file given by filename, and output stats.
    """
    # Read the file into an array of numbers.
    numbers = read_csv_into_list(filename)

    numbers.sort()

    print("%12s: %12.3f" % ("Count", len(numbers)))
    print("%12s: %12.3f" % ("Sum", np.sum(numbers)))
    print("%12s: %12.3f" % ("Min", np.min(numbers)))
    print("%12s: %12.3f" % ("Max", np.max(numbers)))
    print("%12s: %12.3f" % ("Mean", np.mean(numbers)))
    print("%12s: %12.3f" % ("Median", np.median(numbers)))
    print("%12s: %12.3f" % ("Std Dev", np.std(numbers)))
    print("%12s: %12.3f" % ("Variance", np.var(numbers)))
    print("%12s: %12.3f" % ("50th", np.percentile(numbers, 50)))
    print("%12s: %12.3f" % ("90th", np.percentile(numbers, 90)))
    print("%12s: %12.3f" % ("95th", np.percentile(numbers, 95)))
    print("%12s: %12.3f" % ("99th", np.percentile(numbers, 99)))

def usage():
    doc = """
    Usage: ./NumStats.py <input-file>

    Sample Input File:
    26414, 32673, 19516, 13604, 10851, 8692, 7015, 18643, 32390
    29147, 6133, 21279, 21767, 12829, 26203, 23933, 20339, 25405
    14505, 12789, 736, 7295, 20254, 17506, 26524, 14384, 19251
    27318, 21041, 1713, 7313, 26872, 1170, 6430, 27061, 17094
    20685, 28623, 8898, 23577, 1430, 25555, 32735, 16790, 31273
    ...

    Sample Output:

         Min:      736.000
         Max:    32735.000
        Mean:    18125.667
      Median:    19516.000
     Std Dev:     9203.631
    Variance: 84706824.578
        50th:    19516.000
        90th:    28937.400
        95th:    32166.600
        99th:    32707.720
    """ 
    print(doc)
    exit(0)

if __name__ == '__main__': 
    if len(argv) < 2: 
       usage()
    for x in argv[1:]:
        print_stats(x)
