library(data.table)

mRNA_abund=read.table("/home/kristy/Desktop/BIOL3380/Project/mRNA_abundance_all.txt")
TE=read.table("/home/kristy/Desktop/BIOL3380/Project/translational_efficiency_all.txt")

plot(mRNA_abund[,2],TE[,2],main="Logfoldchange in MRNA abundance against logfoldchange in translational efficiency", xlab="log2foldchange in mRNA abundance",ylab="log2foldchange in Translational Efficiency")
#plot(TE[,2], mRNA_abund[,2],main="Logfoldchange in MRNA abundance against logfoldchange in translational efficiency", xlab="log2foldchange in TE",ylab="log2foldchange in mRNA")

combined_all=as.data.table(merge(mRNA_abund,TE,by="V1"))
combined_all

Mup_TEup_all=length(which(combined_all[,2]>0&combined_all[,3]>0))
Mup_TEdown_all=length(which(combined_all[,2]>0&combined_all[,3]<0))
Mdown_TEup_all=length(which(combined_all[,2]<0&combined_all[,3]>0))
Mdown_TEdown_all=length(which(combined_all[,2]<0&combined_all[,3]<0))

row1=c('','mRNA_abundance_increase','mRNA_abundance_decrease')
c11=c('TE_increase',Mup_TEup_all,Mdown_TEup_all)
c21=c('TE_decrease',Mup_TEdown_all,Mdown_TEdown_all)
etable_all=data.frame(row1,c11,c21)
etable_all
write.table(etable_all,file="/home/kristy/Desktop/BIOL3380/Project/etable_all.txt",col.names = FALSE,row.names = FALSE)

mRNA_abund_sig=read.table("/home/kristy/Desktop/BIOL3380/Project/mRNA_abundance_sig.txt")
TE_sig=read.table("/home/kristy/Desktop/BIOL3380/Project/translational_efficiency_sig.txt")

combined_sig=as.data.table(merge(mRNA_abund_sig,TE_sig,by="V1", all=FALSE))
combined_sig

Mup_TEup_sig=length(which(combined_sig[,2]>0&combined_sig[,3]>0))
Mup_TEdown_sig=length(which(combined_sig[,2]>0&combined_sig[,3]<0))
Mdown_TEup_sig=length(which(combined_sig[,2]<0&combined_sig[,3]>0))
Mdown_TEdown_sig=length(which(combined_sig[,2]<0&combined_sig[,3]<0))

row=c('','mRNA_abundance_increase','mRNA_abundance_decrease')
c1=c('TE_increase',Mup_TEup_sig,Mdown_TEup_sig)
c2=c('TE_decrease',Mup_TEdown_sig,Mdown_TEdown_sig)
etable_sig=data.frame(row,c1,c2)
etable_sig
write.table(etable_sig,file="/home/kristy/Desktop/BIOL3380/Project/etable_sig.txt",col.names = FALSE,row.names = FALSE)
