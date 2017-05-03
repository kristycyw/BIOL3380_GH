library(tximport)
library(DESeq2)
library(data.table)

files=c("/home/kristy/Desktop/BIOL3380/Project/Scer_ribo_seq1/abundance.tsv","/home/kristy/Desktop/BIOL3380/Project/Scer_ribo_seq2/abundance.tsv","/home/kristy/Desktop/BIOL3380/Project/Spar_ribo_seq1/abundance.tsv","/home/kristy/Desktop/BIOL3380/Project/Spar_ribo_seq2/abundance.tsv","/home/kristy/Desktop/BIOL3380/Project/Scer_RNA_seq1/abundance.tsv","/home/kristy/Desktop/BIOL3380/Project/Scer_RNA_seq2/abundance.tsv","/home/kristy/Desktop/BIOL3380/Project/Spar_RNA_seq1/abundance.tsv","/home/kristy/Desktop/BIOL3380/Project/Spar_RNA_seq2/abundance.tsv")
names(files)=c("Scer_ribo1","Scer_ribo2","Spar_ribo1","Spar_ribo2","Scer_RNA1","Scer_RNA2","Spar_RNA1","Spar_RNA2")
files

txdat=tximport(files,type="kallisto",txOut=TRUE)

coldata<-matrix(nrow=8,ncol=3)
coldata= data.frame(condition=c("Scer","Scer","Spar","Spar","Scer","Scer","Spar","Spar"),assay=c(rep("ribo",4), rep("RNA",4)))
rownames(coldata)=names(files)
coldata

dds= DESeqDataSetFromTximport(txdat, colData= coldata, design= ~ assay + condition + assay:condition)
dds= DESeq(dds, test="LRT", reduced= ~ assay + condition)

res = results(dds)
res
#log2 fold change (MLE): assayRNA.conditionSpar 
#LRT p-value: '~ assay + condition + assay:condition' vs '~ assay + condition' 
#DataFrame with 5474 rows and 6 columns
#baseMean log2FoldChange     lfcSE         stat       pvalue         padj
#<numeric>      <numeric> <numeric>    <numeric>    <numeric>    <numeric>
# YHR055C    4.489798     -2.2574583 1.7607210    1.6914612  0.193408462   0.61109355
#YPR161C  125.202070      0.3591842 0.3960443    0.8206842  0.364980192   0.77864350
#YOL138C   58.527450      0.2221486 0.5363224    0.1723290  0.678050211   0.90672240
#YDR395W  633.206895      0.9009525 0.2759564   10.6543744  0.001098109   0.03062316
#YGR129W   14.692493      0.4962123 0.9501327    0.2653133  0.606493111   0.88320773
#...             ...            ...       ...          ...          ...          ...
#YNL332W    5.298204     -2.6584856 1.7257003  2.699914778 1.003536e-01 4.578213e-01
#YOR133W  705.665556      0.3420778 2.0571370  0.008172225 9.279691e-01 9.894698e-01
#YML057W  188.070485      0.3116729 0.3924157  0.630420053 4.272013e-01 8.094497e-01
#YML056C 1675.518420      1.6628637 0.3086858 28.656254290 8.643438e-08 1.807808e-05
#YNL030W  442.540071      0.4084571 0.4147565  0.966409749 3.255772e-01 7.448418e-01

plotMA(res)
plotDispEsts(dds)

pval=res$pvalue
sumpval=sum(pval<0.1, na.rm=TRUE)
sumpval
#1188 nominal pvalue, inflated by multiple testing

padj=res$padj
sumpadj=sum(padj<0.1, na.rm=TRUE)
sumpadj
#332

res_dt = as.data.table(as.data.frame(res), keep.rownames="id")
res_raw_print=res_dt[,.(id,log2FoldChange)]
write.table(res_raw_print, file = "/home/kristy/Desktop/BIOL3380/Project/translational_efficiency_all.txt", col.name=FALSE, row.name=FALSE)
res_print=res_dt[padj<.1,.(id,log2FoldChange)]
write.table(res_print, file="/home/kristy/Desktop/BIOL3380/Project/translational_efficiency_sig.txt", col.name=FALSE, row.name=FALSE)

