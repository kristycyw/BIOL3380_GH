#!/usr/bin/python

import os
import pysam
import math

fasta_file=open('chromFa.fasta',"r")
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
#print fasta
#print fasta['seq1'][0][0]
os.remove("fasta_temp.fasta")

bamfile=pysam.AlignmentFile("mapped_181_Sc_BC187.sorted.bam", "rb")

def nCr(n,r):
	f=math.factorial
	return f(n)/f(r)/f(n-r)
E=0.01
for pileupcolumn in bamfile.pileup():
	#print ("\ncoverage at chrom %s base %s = %s" % (pileupcolumn.reference_name,pileupcolumn.pos, pileupcolumn.n))
	nonref=0
	for pileupread in pileupcolumn.pileups:
		if not pileupread.is_del and not pileupread.is_refskip:
			#query position is None if is_del or is_refskip is set.
			#print ('\tbase in read %s = %s' % (pileupread.alignment.query_name, pileupread.alignment.query_sequence[pileupread.query_position]))
			read=pileupread.alignment.query_sequence[pileupread.query_position]
			if read is not fasta[pileupcolumn.reference_name][0][pileupcolumn.pos]:
				nonref+=1
	if nonref is not 0:
		gene_likelihood=nCr(pileupcolumn.n,nonref)*(E**nonref)*((1-E)**(pileupcolumn.n-nonref))
		print ("chrom=%s, base=%s, coverage=%s, gene likelihood=%s"%(pileupcolumn.reference_name,pileupcolumn.pos,pileupcolumn.n,gene_likelihood))		
#bamfile.close()
