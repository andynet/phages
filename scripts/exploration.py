#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 17:50:39 2021

@author: andy
"""

# %%
import pandas as pd
import seaborn as sns
from Bio import SeqIO
import nltk

# %%
tmp = pd.read_csv("./sequences.csv")

# %%
sns.distplot(tmp["Length"], bins=256)

# %%
with open("./sequences.fasta") as f:
    records = list(SeqIO.parse(f, "fasta"))
    


# %%
types = ['ssRNA(+)', 'dsRNA', 'ssDNA(+)', 'ssDNA', 'dsDNA', 'unknown']

for t in types:
    tmp2 = tmp.query(f"Molecule_type == '{t}'")
    print(t, tmp2["Length"].mean().round(), tmp2["Length"].count(), sep='\t')


# %%
sns.displot(tmp["Molecule_type"], )

# %%
tmp3 = tmp.query("10000 < Length < 20000")

selected = []
for record in records:
    if record.id in set(tmp3["Accession"]):
        selected.append(record)

with open("./sequences.selected.fasta", "w") as f:
    SeqIO.write(selected, f, "fasta")

# %%
g = sns.FacetGrid(tmp, col="Molecule_type", margin_titles=True)

# %%
records[tmp2.index[0]].seq

# %%
dist = nltk.edit_distance(records[tmp2.index[0]].seq, records[tmp2.index[1]].seq)
print(dist, len(records[tmp2.index[0]].seq), len(records[tmp2.index[1]].seq))

# %%
seq = str(records[0].seq)

# k can be from 1 to n
def get_set(seq, k):
    A = set()
    for i in range(len(seq) - k):
        A.add(seq[i:i+k])
    return A

def sim_Jaccard(A, B):
    return 1 - len(A.intersection(B))/len(A.union(B))

def dist_Jaccard(A, B):
    return 1 - len(A.intersection(B))/len(A.union(B))

to = 10
k = 19
for i in range(to):
    for j in range(i+1, to):
        A = get_set(records[i].seq, k)
        B = get_set(records[j].seq, k)
        J = dist_Jaccard(A, B)
        print(i, j, J, sep='\t')
           
    
    
    