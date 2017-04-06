#!/usr/bin/bash

bowtie2 -x chromFa_index -U BY.fastq.gz -S s_cerevisiae_BY.sam

#1250000 reads; of these:
# 1250000 (100.00%) were unpaired; of these:
#    1137461 (91.00%) aligned 0 times
#    38463 (3.08%) aligned exactly 1 time
#    74076 (5.93%) aligned >1 times
#9.00% overall alignment rate

samtools view -bS s_cerevisiae_BY.sam > s_cerevisiae_BY.bam

samtools sort s_cerevisiae_BY.bam -o s_cerevisiae_BY.sorted.bam

samtools index s_cerevisiae_BY.sorted.bam





