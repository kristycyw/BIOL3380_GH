#!/usr/bin/python

import pysam

BEDfile=open('Intersect_filtered_cov8_chr21_rand1000.bed',"r")
VCFfile=pysam.VariantFile('greatapes.fixedchr21.vcf.gz')

#for site in VCFfile.fetch('chr21', 14411278, 14411287):
#	print region.pos, region.contig, region.ref
#	print site.samples
		
def select_region(VCF_file,chr_reg,in_reg,out_reg):
	for site in VCF_file.fetch(chr_reg, in_reg, out_reg):
		print site	

for line in BEDfile:
	line=line.strip().split()
	select_region(VCFfile, line[0], int(line[1]), int(line[2]))
	#print line[0], int(line[1]), int(line[2])

	
	
