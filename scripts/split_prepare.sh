#!/bin/bash

for file in $(ls); do
    tmp=$(head -n 1 ${file} | cut -f1 -d '.')
    mv ${file} ${tmp:1}.fna
done;

tree=""
phages=$(ls)
for id in ${phages}; do
    tree="${tree}(${id} ";
done;
for id in ${phages}; do
    tree="${tree})";
done;

