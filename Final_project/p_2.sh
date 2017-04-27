#!/bin/bash

#go to the file where both Kallisto and data are stored
./kallisto index -i s_cerevisiae.idx S_cerevisiae_genelist.fa
./kallisto quant -i s_cerevisiae.idx -o Scer_ribo_seq1 --single -l 180 -s 20 Scer_ribo_seq_1.fastq.gz
./kallisto quant -i s_cerevisiae.idx -o Scer_ribo_seq2 --single -l 180 -s 20 Scer_ribo_seq_2.fastq.gz
./kallisto quant -i s_cerevisiae.idx -o Scer_RNA_seq1 --single -l 180 -s 20 Scer_RNA_seq_1.fastq.gz
./kallisto quant -i s_cerevisiae.idx -o Scer_RNA_seq2 --single -l 180 -s 20 Scer_RNA_seq_2.fastq.gz
./kallisto index -i s_paradoxus.idx S_paradoxus_genelist.fa
./kallisto quant -i s_paradoxus.idx -o Spar_ribo_seq1 --single -l 180 -s 20 Spar_ribo_seq_1.fastq.gz
./kallisto quant -i s_paradoxus.idx -o Spar_ribo_seq2 --single -l 180 -s 20 Spar_ribo_seq_2.fastq.gz
./kallisto quant -i s_paradoxus.idx -o Spar_RNA_seq1 --single -l 180 -s 20 Spar_RNA_seq_1.fastq.gz
./kallisto quant -i s_paradoxus.idx -o Spar_RNA_seq2 --single -l 180 -s 20 Spar_RNA_seq_2.fastq.gz

