library(tximport)
library(DESeq2)
library(data.table)

files=c("/home/kristy/Desktop/BIOL3380/Project/Scer_ribo_seq1/abundance.tsv","/home/kristy/Desktop/BIOL3380/Project/Scer_ribo_seq2/abundance.tsv","/home/kristy/Desktop/BIOL3380/Project/Spar_ribo_seq1/abundance.tsv","/home/kristy/Desktop/BIOL3380/Project/Spar_ribo_seq2/abundance.tsv")
names(files)=c("Scer_ribo1","Scer_ribo2","Spar_ribo1","Spar_ribo2")
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
#baseMean log2FoldChange     lfcSE        stat       pvalue         padj
#<numeric>      <numeric> <numeric>   <numeric>    <numeric>    <numeric>
#  YHR055C   0.9971159   -0.007433859 0.5310730 -0.01399781    0.9888317           NA
#YPR161C  38.4581145   -0.433633381 0.4130877 -1.04973680    0.2938391    0.6827815
#YOL138C  14.3096182   -0.136576492 0.5504466 -0.24811941    0.8040420    0.9539625
#YDR395W 252.1133954    0.268474256 0.2745298  0.97794230    0.3281029    0.7105605
#YGR129W   4.3566309   -0.036529083 0.6503145 -0.05617141    0.9552053    0.9921823
#...             ...            ...       ...         ...          ...          ...
#YNL332W    1.761419      0.6128318 0.5959369    1.028350 3.037851e-01           NA
#YOR133W  414.013757     -5.1402264 0.5486205   -9.369366 7.296926e-21 3.894126e-18
#YML057W   63.368622     -0.4693893 0.3586255   -1.308856 1.905830e-01 5.771321e-01
#YML056C  577.002714      0.5001016 0.2666685    1.875368 6.074213e-02 3.033868e-01
#YNL030W  165.164756     -0.7617839 0.3282231   -2.320933 2.029044e-02 1.487862e-01

plotMA(res)
plotDispEsts(dds)

pval=res$pvalue
sumpval=sum(pval<0.1, na.rm=TRUE)
sumpval
#1178

padj=res$padj
sumpadj=sum(padj<0.1, na.rm=TRUE)
sumpadj
#563

res_dt = as.data.table(as.data.frame(res), keep.rownames="id")
res_print=res_dt[padj<.1,.(id,log2FoldChange)]
write.table(res_print, file="/home/kristy/Desktop/BIOL3380/Project/ribosomal_occupancy_sig.txt", col.name=FALSE, row.name=FALSE)