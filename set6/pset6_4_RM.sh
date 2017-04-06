#!/usr/bin/bash

bowtie2 -x chromFa_index -U RM.fastq.gz -S s_cerevisiae_RM.sam

#1250000 reads; of these:
#  1250000 (100.00%) were unpaired; of these:
#    1106305 (88.50%) aligned 0 times
#    52835 (4.23%) aligned exactly 1 time
#    90860 (7.27%) aligned >1 times
#11.50% overall alignment rate

samtools view -bS s_cerevisiae_RM.sam > s_cerevisiae_RM.bam

samtools sort s_cerevisiae_RM.bam -o s_cerevisiae_RM.sorted.bam

samtools index s_cerevisiae_RM.sorted.bam


