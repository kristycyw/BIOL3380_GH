#!/usr/bin/bash

samtools mpileup -f chromFa.fasta mapped_181_Sc_BC187.sorted.bam > mapped_181_Sc_BC187.mpileup

samtools mpileup -ugf chromFa.fasta mapped_181_Sc_BC187.sorted.bam | bcftools call -vmO z -o mapped_181_Sc_BC187.vcf.gz

