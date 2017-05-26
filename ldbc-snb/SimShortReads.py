#!/usr/bin/python

import random

dissipationFactor = 0.2
trials = 1000000
results = []

for i in range(0,trials):
    if random.random() < 0.5:
        personSeries = True
    else:
        personSeries = False

    shortReads = 0
    P = 1.0
    while True:
        if random.random() < P:
            if personSeries:
                shortReads += 3
            else:
                shortReads += 4

            personSeries = ~personSeries
            P -= dissipationFactor
        else:
            break

    results.append(shortReads)

print float(sum(results))/float(len(results))

