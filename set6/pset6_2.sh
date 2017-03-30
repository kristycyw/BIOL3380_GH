#!/usr/bin/bash

#cat /chromFa/*.fa > chromFa.fasta

bowtie2-build chromFa.fasta chromFa_index

bowtie2 -x chromFa_index -U SRR1177156_1_1000000.fastq -S s_cerevisiae.sam

#250000 reads; of these:
#  250000 (100.00%) were unpaired; of these:
#    227129 (90.85%) aligned 0 times
#    7789 (3.12%) aligned exactly 1 time
#    15082 (6.03%) aligned >1 times
#9.15% overall alignment rate

samtools view -bS s_cerevisiae.sam > s_cerevisiae.bam

samtools sort s_cerevisiae.bam -o s_cerevisiae.sorted.bam

samtools index s_cerevisiae.sorted

