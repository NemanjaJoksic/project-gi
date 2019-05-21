## Introduction
This repo contains python scripts which were used for testing off-line processing string matching algorithms. This scripts were used for performance comparation between different algorithms variation.
## Test running
Testing starts with command:
python script.py test_file_path index_struct_type pattern_1 pattern_2 ...
where index_struct_type has next values:
- 1 - sorted index
- 2 - hash table
- 3 - suffix array
- 4 - suffix tree
## Test data
Test data files were to big for uploading it on github and there are links to this files:
- [Canis lupus familiaris genom](http://ftp.ncbi.nlm.nih.gov/genomes/Canis_lupus_familiaris/CHR_01/cfa_ref_CanFam3.1_chr1.fa.gz)
- [Phoenix dactylifera genome](http://ftp.ncbi.nlm.nih.gov/genomes/Phoenix_dactylifera/CHR_Un/42345_ref_DPV01_chrUn.fa.gz)
- [Ananas comosus cultivar genome](http://ftp.ncbi.nlm.nih.gov/genomes/Ananas_comosus/CHR_01/4615_ref_ASM154086v1_chr1.fa.gz)
