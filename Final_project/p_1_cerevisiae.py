#!/bin/python

def read_fasta(fastaFile):
	fastaDict = {}
	chromNum = 0
	for line in fastaFile:
		if line[0] == ">":
			chromNum+=1
			fastaDict[chromNum] = []
		else:
			fastaDict[chromNum].append(line.strip())
	for chrom in fastaDict:
		fastaDict[chrom] = ''.join(fastaDict[chrom])
	return fastaDict

fasta_file=open("S_cerevisiae.fa","r")
genome=read_fasta(fasta_file)

bedfile=open("S_cerevisiae_genes.bed","r")
out_genelist=open("S_cerevisiae_genelist.fa","w")

for line in bedfile:
	line=line.strip().split()
	if line[0] == "chrI":
		line.insert(0,1)
	if line[0] == "chrII":
                line.insert(0,2)
	if line[0] == "chrIII":
                line.insert(0,3)
	if line[0] == "chrIV":
                line.insert(0,4)
	if line[0] == "chrV":
                line.insert(0,5)
	if line[0] == "chrVI":
                line.insert(0,6)
	if line[0] == "chrVII":
                line.insert(0,7)
	if line[0] == "chrVIII":
                line.insert(0,8)
	if line[0] == "chrIX":
                line.insert(0,9)
	if line[0] == "chrX":
                line.insert(0,10)
	if line[0] == "chrXI":
                line.insert(0,11)
	if line[0] == "chrXII":
                line.insert(0,12)
	if line[0] == "chrXIII":
                line.insert(0,13)
	if line[0] == "chrXIV":
                line.insert(0,14)
	if line[0] == "chrXV":
                line.insert(0,15)
	if line[0] == "chrXVI":
                line.insert(0,16)
	gene_nm=line[4]
	gene=genome[line[0]][int(line[2]):int(line[3])+1]
	out_genelist.write(">%s\n%s\n"%(gene_nm,gene))
