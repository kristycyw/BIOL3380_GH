library(tximport)
library(DESeq2)

files=c("/home/kristy/Desktop/BIOL3380/Project/Scer_RNA_seq1/abundance.tsv","/home/kristy/Desktop/BIOL3380/Project/Scer_RNA_seq2/abundance.tsv","/home/kristy/Desktop/BIOL3380/Project/Spar_RNA_seq1/abundance.tsv","/home/kristy/Desktop/BIOL3380/Project/Spar_RNA_seq2/abundance.tsv")
names(files)=c("Scer_RNA1","Scer_RNA2","Spar_RNA1","Spar_RNA2")
files

txdat=tximport(files,type="kallisto",txOut=TRUE)

coldata= data.frame(condition=c("Scer","Scer","Spar","Spar"))
rownames(coldata)=names(files)
coldata

dds= DESeqDataSetFromTximport(txdat, colData= coldata, design=~ condition)

dds=DESeq(dds)

res = results(dds)
res
#log2 fold change (MAP): condition Spar vs Scer 
#Wald test p-value: condition Spar vs Scer 
#DataFrame with 5474 rows and 6 columns
#baseMean log2FoldChange     lfcSE         stat       pvalue         padj
#<numeric>      <numeric> <numeric>    <numeric>    <numeric>    <numeric>
#  YHR055C   17.71642  -1.7464779488 0.5758112 -3.033074171 2.420761e-03 8.427720e-03
#YPR161C  403.84449  -0.1002890751 0.2231430 -0.449438604 6.531153e-01 7.685871e-01
#YOL138C  220.42518  -0.0005378971 0.2499054 -0.002152403 9.982826e-01 9.987184e-01
#YDR395W 1546.32346   1.1720061061 0.1773119  6.609854443 3.846981e-11 7.748104e-10
#YGR129W   48.82994   0.4171984203 0.3908266  1.067476901 2.857565e-01 4.274949e-01
#...            ...            ...       ...          ...          ...          ...
#YNL332W   15.95234     -0.4162609 0.5616534   -0.7411348 4.586117e-01 6.056169e-01
#YOR133W  580.00964     -4.9626481 0.5510591   -9.0056553 2.143816e-19 1.253556e-17
#YML057W  558.48139     -0.1749134 0.2347511   -0.7451016 4.562103e-01 6.036184e-01
#YML056C 4869.33317      2.1712813 0.1698030   12.7870594 1.936641e-37 5.850807e-35
#YNL030W 1173.67292     -0.3735552 0.2105244   -1.7744035 7.599643e-02 1.521340e-01


plotMA(res)
plotDispEsts(dds)

pval=res$pvalue
sumpval=sum(pval<0.1, na.rm=TRUE)
sumpval
#2884

padj=res$padj
sumpadj=sum(padj<0.1, na.rm=TRUE)
sumpadj
#2469