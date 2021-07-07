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
- http://pipmaker.bx.psu.edu/dist/tba.pdf  (2004)
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

cd data
seqkit split2 -O NC_001416_related.split -s 1 NC_001416_related.fasta
cd NC_001416_related.split

phages=""
for file in $(ls); do
    sed -i 's/\(>\w\+\).*/\1/' ${file}
    tmp=$(head -n 1 ${file})
    phages="${tmp:1} ${phages}"
    mv ${file} ${tmp:1}
done;

tree=""
for id in ${phages}; do
    tree="${tree}(${id} ";
done;
for id in ${phages}; do
    tree="${tree})";
done;

all_bz + "${tree}"
tba "${tree}" *.sing.maf tba.maf
maf_project tba.maf NC_001416 > NC_001416_projected.maf

```

```
blastzWrapper MN855678.fna CP025712.fna Y=9000 H=0  | lav2maf /dev/stdin MN855678.fna CP025712.fna | maf_sort /dev/stdin MN855678.fna > MN855678.fna.CP025712.fna.orig.maf

single_cov2 NC_019723.fna.MN855678.fna.orig.maf  > NC_019723.fna.MN855678.fna.sing.maf

tba.v12: no alignment found for MN855681.fna and CP025712.fna
```