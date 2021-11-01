# extract related sequences
```
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge

conda install blast seqkit seqtk cactus

seqkit rmdup -s -d duplicates.fasta < sequences.fasta > unique.fasta
makeblastdb -in unique.fasta -out unique -dbtype nucl

seqtk seq -l0 sequences.fasta | grep -A 1 NC_001422 > NC_001422.fasta
blastn -db unique -query NC_001422.fasta -outfmt "6 qseqid sseqid qlen slen length pident" -qcov_hsp_perc 10 > NC_001422.blast

less NC_001422.blast | head -n 163 | cut -f2 | sort | uniq > NC_001422.list
seqtk seq -l0 sequences.fasta | grep -A 1 --no-group-separator -f NC_001422.list > NC_001422.related.fna

seqkit split2 -O NC_001422.fna.split -s 1 NC_001422.related.fna
ls -1 NC_001422.fna.split > NC_001422.fna.list
cvtree -G NC_001422.fna.split -i NC_001422.fna.list -g fna

cp tree/Hao.fna.cv5.nwk NC_001422.cactus.txt

less NC_001422.list | sed "s/.fasta//g" | sed "s/\(.*\)/\1 \.\/NC_001422\.fna\.split\/\1\.fna/g" > NC_001422.paths
cat NC_001422.cactus.txt NC_001422.paths > NC_001422.txt

cactus jobstore NC_001422.txt NC_001422.hal --binariesMode local
conda install networkx==1.11


```
# Cactus how to
```
source /opt/cactus-2.0.3/cactus_env-3.8/bin/activate
cactus ./jobstore /opt/cactus-2.0.3/examples/evolverMammals.txt ./evolverMammals.hal --realTimeLogging
hal2maf evolverMammals.hal evolverMammals.maf
mafFilter -needComp=simHuman_chr6.simHuman.chr6 evolverMammals.maf -reject=rejected.maf > evolverMammals.filtered.maf
maf_project evolverMammals.filtered.maf simHuman_chr6.simHuman.chr6 removed.tmp > projected.maf
sed "s/simHuman_chr6.simHuman.chr6/ref/" projected.maf > projected.clean.maf
```

# How to view .maf in igv
- start `igv`
- load the reference genome
- load the maf file
    - MAF file needs to be projected onto reference genome
    - first MAF sequence has to have exactly the same name as the FASTA record (avoid long names and names with . and _)
- zoom in sufficiently 

# How to produce gfa 
```
conda install -c bioconda seqwish
conda install -c bioconda smoothxg
conda install -c bioconda bandage
```

```
hal2fasta evolverMammals.hal $(halStats --root evolverMammals.hal) --subtree --upper > evolverMammals.fa
hal2paf evolverMammals.hal > evolverMammals.paf
seqwish -p evolverMammals.paf -s evolverMammals.fa -g evolverMammals.gfa
smoothxg -g evolverMammals.gfa -o evolverMammals.smooth.gfa
```