```
mafft --retree 1 --maxiterate 0 --nofft --parttree --treeout <input> > <output>
```

## how to install CVTree
```
sudo pacman -Syu cmake gcc openmp netcdf netcdf-cxx

cd tools
mv /home/balaz/Downloads/CVTree-Version-3.0.0.tar.gz .
ex CVTree-Version-3.0.0.tar.gz

cd CVTree-Version-3.0.0
mkdir build

cd build
cmake ..
make

cd ../example
../build/bin/cvtree -G faa
```