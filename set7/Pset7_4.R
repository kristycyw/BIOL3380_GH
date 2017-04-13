library(data.table)

gene_exp=fread("~/Desktop/BIOL3380/Pset7/gene_len_exp.txt")
gene_exp

log_fold_chge<-gene_exp[, log2(V3/V4)]
log_fold_chge

good_log_fold_change<-gene_exp[V3!=0&V4!=0, log2(V3/V4)]
good_log_fold_change

pseudo<-gene_exp[, .(V1,V2,V3=V3+1,V4=V4+1)]
pseudo

pseudo_log_fold_chge<-pseudo[, log2(V3/V4)]
pseudo_log_fold_chge

FPKM<-pseudo[, .(V3/(V2*sum(V3))*10^9, V4/(V2*sum(V4))*10^9)]
FPKM

FPKM_log_fold_chge<-FPKM[, log2(V1/V2)]
FPKM_log_fold_chge

plot(pseudo_log_fold_chge,FPKM_log_fold_chge)
abline(0,1)