#!/usr/bin/python

import gffutils

db = gffutils.FeatureDB("saccharomyces_cerevisiae.db")

for type in db.featuretypes(): print type

mRNAlist=[]
mRNA_wIntron=[]
for mRNA in db.features_of_type("mRNA"):
	mRNAlist.append(mRNA["Name"])
	for intron in db.children(mRNA, featuretype="intron"):
		#print mRNA["Name"], intron.start, intron.stop
		mRNA_wIntron.append(mRNA["Name"])
#print mRNA_wIntron
Total=len(mRNAlist)
#print Total
f_mRNA_wIntron = [val for sublist in mRNA_wIntron for val in sublist]
#print f_mRNA_wIntron
list_wIntron=list(set(f_mRNA_wIntron))
wIntron=len(f_mRNA_wIntron)
print "Fraction of mRNA with introns=", float(wIntron)/Total
print "List of mRNA with Introns=", list_wIntron

out_genelen=open("genelength.txt","w")
for mRNA in db.features_of_type("mRNA"):
	mRNA_length=0
	for CDS in db.children(mRNA, featuretype="CDS"):
		CDS_length=CDS.stop-CDS.start+1
		mRNA_length+=CDS_length
	out_genelen.write("%s\t%i\n" % (mRNA["Name"], mRNA_length))

