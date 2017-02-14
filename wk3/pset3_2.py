#!/usr/bin/python

import os
import string
import re

fasta_file=open('my_genome.fa',"r")
fastq_file=open('my_reads.fastq', "r")
output=open('fasta_temp.fasta',"w")
strfindout=open('output.txt', "w")

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
print fasta
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
print newfasta

#longs='ATTCCGAGATGGGTATGAATATG'
stringeg='ATTGGTGGAGAGGGTCCTAGATACTACCATTTCCTGTATTTCAATGGCCATCCTATCATTCTGGAGGATGTTTCATAATTGAACGATATTTTAAGGAGGG'
print 'example shortstring used is @someread0 for all original chromosome seqs'
def stringfind(longstring, shortstring):
	occurloc=[]
	index=0
	if shortstring in longstring:
		pos=shortstring[0]
#		print 'pos', pos
		for m in longstring:
			if m==pos:
				if longstring[index:index+len(shortstring)]==shortstring:
					occurloc.append(index+1)
	#				return occurloc
			index+=1
#		print occurloc
	if occurloc==[]:
		occurloc=None
	return occurloc
#print stringfind(longs, stringeg)

for key1, value1 in fasta.items():
	for x in value1:
		print 'found in', key1, stringfind(x, stringeg)
					
#listall=[]
#for m in re.finditer('ATG',value1):
#	print ('found at', key, key1, m.start()+1, m.end()+1)
#found=value1.find(string, 0, len(value1))
#if found > -1:
#	list_eachseq.append(found+1)
#	found
#if found == -1:
#	list_eachseq.append(None)
#	return None
#listall.append(list_eachseq)
#print listall	

print 'output of string find algorithm in output.txt'
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

for key2, value2 in newfasta.items():
	for key3, value3 in value2.items():
		for key4, value4 in rdict.items():
			foundstr=stringfind(value3, value4)
			strfindout.write("read name: %s, chromosome: %s, strand: %s, positions: %s \n" %(key4,key2,key3,foundstr))

print "real	4m34.127s"
print "user	4m33.280s"
print "sys	0m0.304s"

