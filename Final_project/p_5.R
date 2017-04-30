library(tximport)
library(DESeq2)

files=c("/home/kristy/Desktop/BIOL3380/Project/Scer_RNA_seq1/abundance.tsv","/home/kristy/Desktop/BIOL3380/Project/Scer_RNA_seq2/abundance.tsv","/home/kristy/Desktop/BIOL3380/Project/Spar_RNA_seq1/abundance.tsv","/home/kristy/Desktop/BIOL3380/Project/Spar_RNA_seq2/abundance.tsv","/home/kristy/Desktop/BIOL3380/Project/Scer_ribo_seq1/abundance.tsv","/home/kristy/Desktop/BIOL3380/Project/Scer_ribo_seq2/abundance.tsv","/home/kristy/Desktop/BIOL3380/Project/Spar_ribo_seq1/abundance.tsv","/home/kristy/Desktop/BIOL3380/Project/Spar_ribo_seq2/abundance.tsv")
names(files)=c("Scer_RNA1","Scer_RNA2","Spar_RNA1","Spar_RNA2","Scer_ribo1","Scer_ribo2","Spar_ribo1","Spar_ribo2")
files

txdat=tximport(files,type="kallisto",txOut=TRUE)

coldata<-matrix(nrow=8,ncol=3)
coldata= data.frame(condition=c("Scer","Scer","Spar","Spar"),assay=c(rep("RNA",4),rep("ribo",4)))
coldata$group<-paste(coldata$condition,coldata$assay)
rownames(coldata)=names(files)
coldata

dds= DESeqDataSetFromTximport(txdat, colData= coldata, design=~ group)

dds=DESeq(dds)

res = results(dds)
res
#log2 fold change (MAP): group Spar RNA vs Scer ribo 
#Wald test p-value: group Spar RNA vs Scer ribo 
#DataFrame with 5474 rows and 6 columns
#baseMean log2FoldChange     lfcSE        stat       pvalue         padj
#<numeric>      <numeric> <numeric>   <numeric>    <numeric>    <numeric>
#  YHR055C    4.489798    -0.72750527 0.7990058  -0.9105131   0.36255195    0.4766245
#YPR161C  125.202070     0.01929077 0.2811041   0.0686250   0.94528812    0.9625991
#YOL138C   58.527450     0.63017467 0.3773891   1.6698274   0.09495352    0.1659385
#YDR395W  633.206895     0.11656205 0.1970091   0.5916583   0.55407940    0.6610758
#YGR129W   14.692493     0.60132937 0.5961304   1.0087211   0.31310839    0.4256457
#...             ...            ...       ...         ...          ...          ...
#YNL332W    5.298204      0.4328857 0.7789012   0.5557645 5.783719e-01 6.827348e-01
#YOR133W  705.665556     -7.7972957 0.5952414 -13.0993833 3.319438e-39 6.940281e-37
#YML057W  188.070485     -0.2827990 0.2759072  -1.0249788 3.053732e-01 4.180685e-01
#YML056C 1675.518420      0.9561109 0.2152821   4.4411999 8.945866e-06 6.092772e-05
#YNL030W  442.540071     -0.7984624 0.2861634  -2.7902325 5.267020e-03 1.472231e-02

plotMA(res)
plotDispEsts(dds)

pval=res$pvalue
sumpval=sum(pval<0.1, na.rm=TRUE)
sumpval
#3028

padj=res$padj
sumpadj=sum(padj<0.1, na.rm=TRUE)
sumpadj
#2683

