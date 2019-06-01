#!/usr/bin/env python

from __future__ import division, print_function
from sys import argv,exit
import re

def read_csv_into_list(filename, fs):
    """
    Read a csv file of floats, concatenate them all into a flat list and return
    them.
    """
    numbers = []
    for line in open(filename, 'r'):
        parts = line.split()
        numbers.append(parts)
    return numbers
    
def percentify(filename, column, fs):
    # Read the file into an array of numbers.
    numbers = read_csv_into_list(filename, fs)

    acc = 0
    for row in numbers:
      acc += float(row[column-1])

    for row in numbers:
      i = 0
      for col in row:
        if i == column-1:
          print("%f "  % (float(row[i])/acc), end='')
        else:
          print(row[i] + " ", end='')
        i += 1
      
      print()



def usage():
    doc = """
    Usage: ./percentify.py <input-file> <column> <field_separator>

    Percentify the values in a given column in a csv file. Replaces values 
    with their relative weight in the sum of the values in the column.

    Sample Input File:
    8       1
    10      14
    12      29
    14      34
    16      23
    18      4

    ./percentify.py input.txt 2 " "

    Sample Output:
    8       0.0095
    10      0.1333
    12      0.2762
    14      0.3238
    16      0.2190
    18      0.0381

    """ 
    print(doc)
    exit(0)

if __name__ == '__main__': 
    if len(argv) < 4: 
       usage()
    percentify(argv[1], int(argv[2]), argv[3])
