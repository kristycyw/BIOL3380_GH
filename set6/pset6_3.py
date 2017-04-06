#!/usr/bin/python

import gffutils
import pysam

db = gffutils.FeatureDB("saccharomyces_cerevisiae.db")
bamfile=pysam.AlignmentFile("s_cerevisiae.sorted.bam","rb")

out_FPKM=open("FPKM.txt","w")

Ci=[]
Li=[]
names = []
for mRNA in db.features_of_type("mRNA"):
	names.append(mRNA["Name"])
	if mRNA.chrom == 'chrmt':
		continue
	print bamfile.count(mRNA.chrom,mRNA.start,mRNA.stop)
	Ci.append(bamfile.count(mRNA.chrom,mRNA.start,mRNA.stop))
	mRNA_length=0
	for CDS in db.children(mRNA, featuretype="CDS"):
		CDS_length=CDS.stop-CDS.start+1
		mRNA_length+=CDS_length
	Li.append(mRNA_length)

FPKM_list=[]
M=sum(Ci)
for x in range(len(Ci)):
        FPKM=(float(Ci[x])/(Li[x]*M))*10**9
        FPKM_list.append(FPKM)
for y in range(len(FPKM_list)):
	out_FPKM.write("%s\t%f\n" % (names[y][0],FPKM_list[y]))

		
