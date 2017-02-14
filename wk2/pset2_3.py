#!/usr/bin/python

import matplotlib.pyplot as plt
#import matplotlib.mlab as mlab
import os

fastq=open('/home/kristy/Desktop/BIOL3380/Pset2/I1303.1240k.fastq',"r")
#output=open('/home/kristy/Desktop/BIOL3380/Pset2/fastq_out.txt',"w")

seqlistln=[]
seqlist=[]
qualist=[]

while True:
	name = fastq.readline()
	if name == "":
		break
	seq=fastq.readline().strip()
	name2 = fastq.readline()
	qual = fastq.readline().strip()
	seqlistln.append(len(seq))
	seqlist.append(seq)
	qualist.append(qual)
#print qualist
print seqlistln
#print seqlist



aplot=plt.hist(seqlistln, bins=100)
plt.title("Frequency of Sequence Lengths")
plt.xlabel("Sequence Length")
plt.ylabel("Frequency")
plt.savefig("seqlenfreq.jpg")
plt.show(aplot)
plt.clf()



def countbase(sequence):
	seqdict={}
	for base in sequence:
		seqdict[base]=0
	for base in sequence:
		seqdict[base]+=1
	return seqdict
	print total
#print countbase('ATCGGCTAG')

composition=[]
for i in seqlist:
	count=countbase(i)
	total=sum(count.values())
	for key, value in count.items():
		count[key] = float(value)/total
	composition.append(count)
print composition



readno=range(1,len(seqlist)+1)
#print readno
A=[]
T=[]
C=[]
G=[]
for ndict in composition:
	Aval=ndict.get('A','0')
	Tval=ndict.get('T','0')
	Cval=ndict.get('C','0')
	Gval=ndict.get('G','0')
	A.append(Aval)
	T.append(Tval)
	C.append(Cval)
	G.append(Gval)
#print A
plt.plot(readno, A, 'r-o', label="A")
plt.plot(readno, T, 'b-o', label="T")
plt.plot(readno, C, 'g-o', label="C")
plt.plot(readno, G, 'y-o', label="G")
plt.xlabel("read number")
plt.ylabel("base composition")
plt.title("Plot of base composition along reads")
plt.legend()
plt.savefig("basecomp_acrossreads.jpg")
plt.show()
plt.clf()



qualityscore=[]
for y in qualist:
	qualityread=[]
	for x in y:
		qualities = ord(x) - 33
		qualityread.append(qualities)
	qualityscore.append(qualityread)
print qualityscore



#print "plots the quality score along every base position for each read separately, please check qscore folder for plots"
#print "prints more than 205 500 plots (it was still runnng when my com was dead) 100 plots are included in the file 'qscore(example)', please comment out the lines 104-118 to skip the following script"
#newpath=r'qscore'
#if not os.path.exists(newpath):
#	os.makedirs(newpath)
#z=0
#for nested in qualityscore:
#	x=range(1,len(nested)+1,1)
#	y=nested
#	bplot=plt.plot(x,y,'bo',x,y,'k')
#	plt.title("Quality score along read")
#	plt.xlabel("Base position")
#	plt.ylabel("Quality Score")
#	z+=1
#	plt.savefig("qscore/qscoreplot{z}.jpg".format(z=z))
#	plt.show(bplot)
#	plt.clf()


avgreadqscore=[]
for nested in qualityscore:
	mean=float(sum(nested))/len(nested)
	avgreadqscore.append(mean)
#print avgreadqscore
a=seqlistln
b=avgreadqscore
cplot=plt.plot(a, b, "o")
plt.title("Quality score against Read length")
plt.xlabel("Read length")
plt.ylabel("Average Quality Score")
plt.savefig("readln_readscore.jpg")
plt.show(cplot)
