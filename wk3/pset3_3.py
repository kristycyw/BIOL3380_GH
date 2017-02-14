#!/usr/bin/python

import os
import string
import re

fasta_file=open('my_genome.fa',"r")
fastq_file=open('my_reads.fastq', "r")
output=open('fasta_temp.fasta',"w")
listfindout=open('output_dict.txt', "w")


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
#print fasta
os.remove("fasta_temp.fasta")

newfasta={}
for key, value in fasta.items():
#       print value
	newfasta[key]={}
	for i in value:
                intab="ATGC"
                outab="TACG"
                transtable=string.maketrans(intab, outab)
                comp=i.translate(transtable)
                newfasta[key]['+']=i
		newfasta[key]['-']=comp
#print newfasta


rname=[]
rseq=[]
while True:
	fqname = fastq_file.readline().strip()
	if fqname == "":
		break
	fqseq=fastq_file.readline().strip()
	name2 = fastq_file.readline()
	qual = fastq_file.readline().strip()
	rname.append(fqname)
	rseq.append(fqseq)
rdict={}
for a in range(0, len(rname)):
	rdict[rname[a]]=rseq[a]
#print rdict

hashdict={}
for chromosome, value1 in newfasta.items():
	for complement, genome in value1.items():
		n=len(genome)
		#print n, 'genome'
		for readnm, read in rdict.items():
			m=len(read)
			#print m, 'read'
			for x in range(n):
				hashdict[genome[x:(x+m)]]=[x, chromosome, complement]
#print hashdict

print "occurence of read in dictionary of possible reads outputs in output_dict.txt"
#def findread(shortstring, dicthashes):
for poss, count in hashdict.items():
	for rdnm,rd in rdict.items():
		if rd in poss:
			listfindout.write("read name: %s, chromosome: %s, strand: %s, position: %s \n" %(rdnm,count[1],count[2],count[0]))
#		listfindout.write("read name: %s, chromosome: %s, strand: %s, position: %s \n" %(rdnm,count[1],count[2],None))

				
