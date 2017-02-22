#!/usr/bin/python

import os
import string
import numpy

fasta_file=open('my_test.fa',"r")
output=open('fasta_temp.fasta',"w")

temp=[]
seq =""
for line in fasta_file:
	if line.startswith(">"):
		if seq != "":
			temp.append(seq)
			seq=""
		seq += '\n'+line     
	else:
		seq += line.strip().replace('\n', '')
else: 
	if seq != "":
		temp.append(seq)
		seq=""
temp[0] = temp[0].strip()
for item in temp:
	output.write("%s" % item)
output.close()
out=open('fasta_temp.fasta', "r")
fasta={}
for line2 in out:
	line2=line2.strip()
	if line2.startswith(">"):
		seqname = line2[1:]
		fasta[seqname]=[]
		seqs=''
	else:
		seqs=seqs+line2
		fasta[seqname].append(line2)
fasta_file.close()
out.close()
os.remove("fasta_temp.fasta")
#print fasta

filenames=[]
SALIST=[]
bwtlist=[]
for seqnm, seq in fasta.items():
	filenames.append(seqnm)
	#print filenames
	salist=[]
	suffix=[]
	for i in seq:
		i=i+'$'
		suffix.append(i)
		stlen=len(i)
		for a in range(0, len(i)-1):
			newstr=i[1:]+i[0]
			i=newstr
			#print newstr
			suffix.append(i)
		sa = numpy.argsort(suffix)
		#print suffix
		#this is the order of the sort
#position i in SA correpsonds to position in the BWT and SA[i] is the position of that element of the BWT in the original string
		for a in sa:
			salist.append(a)
		SALIST.append(salist)
#print SALIST 
	#print salist
	BWT=[]
	for b in salist:
		#print suffix[b][-1]
		BWT.append(suffix[b][-1])
	BWT = ''.join(BWT)
	#print BWT
	bwtlist.append(BWT)
#print bwtlist
for bwt1, filenames1 in zip(bwtlist,filenames):
	with open(filenames1+'.txt', 'w') as output:
		output.write(bwt1 + '\n')

for seqnm1, seq1 in fasta.items():
	for c in seq1:
		#for x in range(0, len(c), 10):
			#print x, salist[x], BWT[x]
		with open(seqnm1+'_SA.txt','w') as out_sa:
			for x in range(0, len(c), 10):
				out_sa.write("%s \t %i \t %i \n"%(BWT[x], x, salist[x]))
		with open(seqnm1+'_c.txt','w') as out_c:
			for x in range(0, len(c), 10):
				out_c.write("%i \t A:%i \t T:%i \t C:%i \t G:%i \n"%(x,BWT[x].count('A'),BWT[x].count('T'),BWT[x].count('C'),BWT[x].count('G')))
		with open(seqnm1+'_occ.txt','w') as out_occ:
			for x in range(0, len(c), 10):
				out_occ.write("%i \t A:%i \t T:%i \t C:%i \t G:%i \n"%(x,BWT[0:x].count('A'),BWT[0:x].count('T'),BWT[0:x].count('C'),BWT[0:x].count('G')))
				
