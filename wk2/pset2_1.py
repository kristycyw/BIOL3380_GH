#!/usr/bin/python

import random as rand

print "for 10 000 reads"
alist=[]
for i in range(1000000):
	i=0
	alist.append(i)
#length=len(alist)
#print length
#print alist

for i in range(10000):
	start=rand.randint(0,1000000)
	if start < 999900:
		for x in range(start,start+100):
			alist[x] += 1
	if start > 999900:
		for x in range(start,1000000):
			alist[x] += 1

print alist

count=alist.count(0)
fractiona=float(count)/1000000
#print fractiona

print "for 50 000 reads"
blist=[]
for i in range(1000000):
	i=0
	blist.append(i)
#length=len(blist)
#print length
#print blist

for i in range(50000):
	start=rand.randint(0,1000000)
	if start < 999900:
		for x in range(start,start+100):
			blist[x] += 1
	if start > 999900:
		for x in range(start,1000000):
			blist[x] += 1

print blist

count=blist.count(0)
fractionb=float(count)/1000000
#print fractionb

print "for 100 000 reads"
clist=[]
for i in range(1000000):
	i=0
	clist.append(i)
#length=len(clist)
#print length
#print clist

for i in range(100000):
	start=rand.randint(0,1000000)
	if start < 999900:
		for x in range(start,start+100):
			clist[x] += 1
	if start > 999900:
		for x in range(start,1000000):
			clist[x] += 1

print clist

count=clist.count(0)
fractionc=float(count)/1000000
#print fractionc

print "The expected fractions of sites with no coverage under the Poisson approximation are 0.37, 0.0067, and 0.000045 for 10,000 reads, 50,000 reads and 100,000 reads, respectively."

errora=(float(abs(0.37-fractiona))/0.37)*100
errorb=(float(abs(0.0067-fractionb))/0.0067)*100
errorc=(float(abs(0.000045-fractionc))/0.000045)*100

print "For 10 000 reads, the fraction of sites with no coverage is", fractiona, ",percentage error from approximation is", errora, "%"
print "For 50 000 reads, the fraction of sites with no coverage is", fractionb, ",percentage error from approximation is", errorb, "%"
print "For 100 000 reads, the fraction of sites with no coverage is", fractionc, ",percentage error from approximation is", errorc, "%"

