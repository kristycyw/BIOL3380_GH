#!/usr/bin/python

#import sys 
#with open(sys.argv[1]) as fasta_file

fastafile=open('/home/kristy/Desktop/BIOL3380/Pset2/test.fasta',"r")
outfile=open('/home/kristy/Desktop/BIOL3380/Pset2/Final/N_x.txt',"w")
#listfile=open('/home/...',"w") #write your output to a file

def fastadict(fasta_file):
	fasta={}
	for line in fasta_file:
		line=line.strip()
		if not line:
			continue
		if line.startswith(">"):
			seqname = line[1:]
			if seqname not in fasta:
				fasta[seqname]=[]
			continue
		fasta[seqname].append(line)
	print fasta

fastadict(fastafile)
#listfile.write(fastadict(fastafile))
#testfile.close
#listfile.close
#fastafile=open('/home/kristy/Desktop/BIOL3380/Pset2/test.fasta',"r")

fastafile.seek(0)

fastalen=[]
for line2 in fastafile:
	if line2.startswith(">"):
		continue
	fastalen.append(len(line2)-1)
print fastalen
sortedfastalen=sorted(fastalen)

growinglist=[]
for i in fastalen:
	for x in range(i):
		growinglist.append(i)
print growinglist

import numpy as np
#quantile=np.percentile(growinglist, 50) #return 50th percentile
#print quantile
for z in range(5, 100, 5):
	quantile = np.percentile(growinglist, z)
	print "The N(",z,") is", quantile
	outfile.write("The N(%i) is %i \n" %(z,quantile))

#def percentile(N, P):
#    n = max(int(round(P * len(N) + 0.5)), 2)
#    return N[n-2]
#parameter N - A list of values.  N must be sorted.
#parameter P - A float value from 0.0 to 1.0

#for z in range(5, 100, 5):
#	quantile=np.percentile(growinglist, float(z)/100)
#	print "The N(",z,") is", quantile		
