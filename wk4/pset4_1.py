#!/usr/bin/python

import os
import string

fasta_file=open('someword.fa',"r")
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
bwt=[]
for seqnm, seq in fasta.items():
	filenames.append(seqnm)
	#print filenames
	temp=[]
	temp2=[]
	for i in seq:
		i=i+'$'
		temp.append(i)
		stlen=len(i)
		for a in range(0, len(i)-1):
			newstr=i[stlen-1]+i[0:stlen-1]
			i=newstr
			#print newstr
			temp.append(i)
	temp=sorted(temp, key=str.upper)
	#print temp
	for b in temp:
		lenb=len(b)
		temp2.append(b[lenb-1])
	temp2=''.join(temp2)
	#print temp2
	bwt.append(temp2)
#print bwt
for bwt1, filenames1 in zip(bwt,filenames):
	with open(filenames1, 'w') as output:
		output.write(bwt1 + '\n')
				
