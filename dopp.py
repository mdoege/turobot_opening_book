#!/usr/bin/env python

tsv = open("all.tsv")
of = open("filtered.tsv", "w")

a = []
n = 0

for l in tsv.readlines():
	l = l.strip()
	x = l.split("\t")
	if x[5] in a:
		n += 1
	else:
		a.append(x[5])
		of.write(l + "\n")
print(n, "duplicate positions dropped")

