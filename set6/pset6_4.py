#!/usr/bin/python

import gffutils
import pysam
import numpy as np
import scipy.stats as st

db = gffutils.FeatureDB("saccharomyces_cerevisiae.db")
BY_bam=pysam.AlignmentFile("s_cerevisiae_BY.sorted.bam","rb")
RM_bam=pysam.AlignmentFile("s_cerevisiae_RM.sorted.bam","rb")

out_pvalue=open("differentialexp.txt","w")

Ci_BY=[]
Ci_RM=[]
names=[]
for mRNA in db.features_of_type("mRNA"):
	names.append(mRNA["Name"])
	if mRNA.chrom == 'chrmt':
		continue
	Ci_BY.append(BY_bam.count(mRNA.chrom,mRNA.start,mRNA.stop))
	Ci_RM.append(RM_bam.count(mRNA.chrom,mRNA.start,mRNA.stop))
	
total_BY=sum(Ci_BY)
total_RM=sum(Ci_RM)
pvalue=[]
for i in range(len(Ci_BY)):
	lambdaRM=float(Ci_RM[i])/total_RM
	lambdaBY=float(Ci_BY[i])/total_BY
	lambda1=(lambdaRM+lambdaBY)/2
	prob_null=st.poisson.pmf(Ci_RM[i],total_RM*lambda1)*st.poisson.pmf(Ci_BY[i],total_BY*lambda1)
	prob_alt=st.poisson.pmf(Ci_RM[i],total_RM*lambdaRM)*st.poisson.pmf(Ci_BY[i],total_BY*lambdaBY)
	LRT=2*(np.log(prob_alt)-np.log(prob_null))
	p_value=st.chi2.sf(LRT,df=1)
	pvalue.append(p_value)
for y in range(len(pvalue)):
	out_pvalue.write("%s\t%i\t%i\t%f\n" % (names[y][0],Ci_BY[y],Ci_RM[y],pvalue[y]))
