#!/usr/bin/python

import pysam
import matplotlib.pyplot as plt

bamfile=pysam.AlignmentFile("mapped_181_Sc_BC187.sorted.bam", "rb")

quality=[]
for read in bamfile.fetch():
	quality.append(read.mapping_quality)
plot=plt.hist(quality,bins=50)
plt.title("Frequency of Mapping Quality")
plt.xlabel("Mapping Quality")
plt.ylabel("Frequency")
plt.savefig("freqmapqual.jpg")
#plt.show(plot)
plt.clf()

forrev=[]
for read1 in bamfile.fetch():
	forrev.append(read1.is_reverse)
total=len(forrev)
false=float(forrev.count(False))/total
true=float(forrev.count(True))/total
print 'Proportion of reads are on the reverse strand (True) is' , true
print 'Proportion of reads are on the forward strand (False) is' , false




