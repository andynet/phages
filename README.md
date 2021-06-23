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
[2021-06-23] \
Downloaded `data/sequences.fasta` and `data/sequences.csv` with all possible columns, without accession version. \
Downloaded `data/NC_001416.fasta`.

```
conda create -n phages
conda activate phages
conda install -c bioconda blast
conda env export --from-history > phages.yaml

makeblastdb -in data/sequences.fasta -out data/db -dbtype nucl
blastn -db data/db -query data/NC_001416.fasta -outfmt "6 qseqid sseqid qlen slen length pident" -qcov_hsp_perc 10 \
        > data/NC_001416.blast

python scripts/get_related_fastas.py

```
