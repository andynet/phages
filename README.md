# data sources

[resource](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&VirusLineage_ss=Bacteriophage,%20all%20taxids&Completeness_s=complete&EnvSample_s=exclude&Proviral_s=exclude)

Filters:
- Virus = Bacteriophage, all taxids
- Nucleotide Completeness = complete
- Provirus = Exclude
- Environmental Source = Exclude

# model phages

| accession | phage name | length    |
|-----------|------------|-----------|
| NC_001422 | phi-X174   | 5386 bp   |
| NC_001416 | lambda     | 48502 bp  |
| NC_000866 | T4         | 168903 bp |

# log
[2021-06-23 - 2021-06-25] \
Downloaded `data/sequences.fasta` and `data/sequences.csv` with all possible columns, without accession version. \
Downloaded `data/NC_001416.fasta`.

some how-to guides:
- http://genomewiki.ucsc.edu/index.php/Whole_genome_alignment_howto
- http://www.bx.psu.edu/miller_lab/dist/tba_howto.pdf
- http://pipmaker.bx.psu.edu/dist/tba.pdf
- https://anaconda.org/bioconda/multiz

```
conda create -n phages
conda activate phages
conda install -c bioconda blast
conda install -c anaconda -c conda-forge spyder pandas biopython
conda install -c bioconda multiz lastz igv seqkit
conda env export --from-history > envs/phages.yaml

seqkit rmdup -s -d duplicates.fasta < sequences.fasta > unique.fasta

makeblastdb -in data/unique.fasta -out data/unique -dbtype nucl
blastn -db data/unique -query data/NC_001416.fasta -outfmt "6 qseqid sseqid qlen slen length pident" -qcov_hsp_perc 10 \
        > data/NC_001416.blast

python scripts/get_related_fastas.py

sed '2q'        NC_001416_related.fasta > s1
sed '1,2d;4q'   NC_001416_related.fasta > s2
...
sed '1,10d;12q' NC_001416_related.fasta > s6

# edit the fasta descriptions

all_bz + "(s1 (s2 (s3 (s4 (s5 s6)))))"
tba "(s1 (s2 (s3 (s4 (s5 s6)))))" *.*.maf tba.maf
maf_project tba.maf s1 > s1_projected.maf

```
