#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

FNAME = "data-012314/nodesNW.csv"
#FNAME = "data-012314/edges_1DNW.csv"
COL = 1

valcount = {}
with open(FNAME, "rb") as fp:
    fp.readline()
    reader = csv.reader(fp, delimiter=";")
    for row in reader:
        if row[COL] not in valcount:
            valcount[row[COL]] = 0
        valcount[row[COL]] += 1

for k, v in sorted(valcount.iteritems()):
    print "'%s'\t%d" % (k, v)
