#!/bin/python

#go to file where kallisto and data are stored
#./kallisto index -i s_cerevisiae.idx Saccharomyces_cerevisiae.R64-1-1.rel81.cdna.all.fa.gz 
#./kallisto quant -i s_cerevisiae.idx -o WT_1 --single -l 180 -s 20 ERR458493.fastq.gz

import os

sample = ["ERR458493", "ERR458500", "ERR458507", "ERR458514", "ERR458521", "ERR458528", "ERR458878", "ERR458885", "ERR458892", "ERR458899"]

names = ["WT_1", "SNF2_1","SNF2_2","SNF2_3", "SNF2_4", "SNF2_5","WT_2","WT_3","WT_4","WT_5"] 

for i in range(len(sample)):
	command= "./kallisto quant -i s_cerevisiae.idx -o %s --single -l 180 -s 20 %s.fastq.gz"%(names[i], sample[i])
	print "Currently running: %s"%command
	os.system(command)
