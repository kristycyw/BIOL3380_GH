#Question 2

#source("https://bioconductor.org/biocLite.R")
#biocLite("DESeq2")

#source("https://bioconductor.org/biocLite.R")
#biocLite("tximport")

library(tximport)
library(DESeq2)

files=c("/home/kristy/Desktop/BIOL3380/Pset8/SNF2_1/abundance.tsv","/home/kristy/Desktop/BIOL3380/Pset8/SNF2_2/abundance.tsv","/home/kristy/Desktop/BIOL3380/Pset8/SNF2_3/abundance.tsv","/home/kristy/Desktop/BIOL3380/Pset8/SNF2_4/abundance.tsv","/home/kristy/Desktop/BIOL3380/Pset8/SNF2_5/abundance.tsv","/home/kristy/Desktop/BIOL3380/Pset8/WT_1/abundance.tsv","/home/kristy/Desktop/BIOL3380/Pset8/WT_2/abundance.tsv","/home/kristy/Desktop/BIOL3380/Pset8/WT_3/abundance.tsv","/home/kristy/Desktop/BIOL3380/Pset8/WT_4/abundance.tsv","/home/kristy/Desktop/BIOL3380/Pset8/WT_5/abundance.tsv")
names(files)=c("SNF2_1","SNF2_2","SNF2_3","SNF2_4","SNF2_5","WT_1","WT_2","WT_3","WT_4","WT_5")
files

txdat=tximport(files,type="kallisto",txOut=TRUE)

coldata= data.frame(condition=c("SNF2", "SNF2", "SNF2", "SNF2", "SNF2", "WT", "WT", "WT", "WT","WT"))
rownames(coldata)=names(files)
coldata

dds= DESeqDataSetFromTximport(txdat, colData= coldata, design=~ condition)

dds=DESeq(dds)

res = results(dds)
res

#log2 fold change (MAP): condition WT vs SNF2 
#Wald test p-value: condition WT vs SNF2 
#DataFrame with 6713 rows and 6 columns
#baseMean log2FoldChange     lfcSE       stat       pvalue         padj
#<numeric>      <numeric> <numeric>  <numeric>    <numeric>    <numeric>
#  YHR055C    33.98424      0.4094874 0.2131269  1.9213318 0.0546898963 0.1472053829
#YPR161C    85.07459      0.2103599 0.1562426  1.3463673 0.1781840948 0.3437957246
#YOL138C    80.34866     -0.1025490 0.1400451 -0.7322573 0.4640115461 0.6413788366
#YDR395W   111.94287      0.6965943 0.1641389  4.2439309 0.0000219638 0.0002076309
#YGR129W    19.15463      0.1951869 0.2660162  0.7337404 0.4631069908 0.6406794752
#...             ...            ...       ...        ...          ...          ...
#YCL074W   0.0000000             NA        NA         NA           NA           NA
#YIL080W 106.9537577     -0.4669895 0.1825473 -2.5581826   0.01052208   0.03999167
#YLL017W   6.8527544     -0.3039407 0.3639545 -0.8351063   0.40365785   0.58988071
#YIL168W   5.9560315      0.3644487 0.3906599  0.9329054   0.35086883   0.53859150
#YAR061W   0.4610622     -0.3868490 0.3423070 -1.1301232   0.25842433           NA

#Question 3
plotMA(res)
plotDispEsts(dds) #DDS has more information including dispersion estimates

pval=res$pvalue
sumpval=sum(pval<0.05, na.rm=TRUE)
sumpval
#2250

padj=res$padj
sumpadj=sum(padj<0.05, na.rm=TRUE)
sumpadj
#1712

#different

