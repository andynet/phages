#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 15:01:00 2021

@author: andy
"""

# %% 
import pandas as pd
from Bio import SeqIO

# %%

df = pd.read_csv("data/NC_001416.blast", sep='\t', header=None)
df.columns = ["qseqid", "sseqid", "qlen", "slen", "length", "pident"]
df = df.head(n=29)

# %%
with open("data/unique.fasta") as f:
    records = list(SeqIO.parse(f, "fasta"))
    
# %%
related_records = []
for record in records:
    if record.id in list(df.sseqid):
        related_records.append(record)
        
# %%
with open("data/NC_001416_related.fasta", "w") as f:
    SeqIO.write(related_records, f, "fasta-2line")
