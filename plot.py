#!/usr/bin/python

import matplotlib.pyplot as plt
import csv, sys, re, random, os, time

I = {}

M = []

plt.figure(figsize=(10,8))

rowNum = 0
with open('results.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=' ', quotechar='"')
    for row in csvreader:
        rowNum += 1
        if (rowNum == 1):
            for i in range(len(row)):
                I[row[i]] = i
            continue
        else:
            M.append(row)


load_col = list(map(lambda r: r[I['Load']], M))
load_col = list(map(lambda x: float(x), load_col))
throughput_col = list(map(lambda r: r[I['Throughput']], M))
throughput_col = list(map(lambda x: float(x), throughput_col))
rt_col = list(map(lambda r: r[I['RT']], M))
rt_col = list(map(lambda x: float(x), rt_col))

plt.subplot(2, 1, 1);
plt.plot(load_col, throughput_col, ls='solid', color='blue', marker='o', markersize=9, mew=2, linewidth=2)
plt.xlabel('Load')
plt.ylabel('Throughput')
plt.grid()

plt.subplot(2, 1, 2);
plt.plot(load_col, rt_col, ls='solid', color='blue', marker='o', markersize=9, mew=2, linewidth=2)
plt.xlabel('Load')
plt.ylabel('Response Time')
plt.grid()

plt.savefig("output.png")