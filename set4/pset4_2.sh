#!/usr/bin/bash

#cat /chromFa/*.fa > chromFa.fasta

bowtie2-build chromFa.fasta chromFa_index

bowtie2 -x chromFa_index --un unmapped.fastq -1 181_Sc_BC187_1.fastq -2 181_Sc_BC187_2.fastq -S mapped_181_Sc_BC187.sam

#1313489 reads; of these:
#  1313489 (100.00%) were paired; of these:
#    648782 (49.39%) aligned concordantly 0 times
#    599164 (45.62%) aligned concordantly exactly 1 time
#    65543 (4.99%) aligned concordantly >1 times
#    ----
#    648782 pairs aligned concordantly 0 times; of these:
#      8701 (1.34%) aligned discordantly 1 time
#    ----
#    640081 pairs aligned 0 times concordantly or discordantly; of these:
#      1280162 mates make up the pairs; of these:
#        1204943 (94.12%) aligned 0 times
#        66291 (5.18%) aligned exactly 1 time
#        8928 (0.70%) aligned >1 times
#54.13% overall alignment rate

samtools view -bS mapped_181_Sc_BC187.sam > mapped_181_Sc_BC187.bam

samtools sort mapped_181_Sc_BC187.bam -o mapped_181_Sc_BC187.sorted

samtools index mapped_181_Sc_BC187.sorted
