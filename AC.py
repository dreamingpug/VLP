import os, sys, subprocess # to use linux

cmd = "AnalyseComplex" # command which foldx can read
pdb = "5uu5_origin_1" # protein file in pdb

#mt_list = "individual_list1.txt " # mutation list in txt

for i in range(5) :
    protein = pdb + '_%d'%i
    protein_pdb = protein+'.pdb'
    print(protein)

    dir = "./%s"%protein
    if not os.path.isdir(dir) :
        os.mkdir(dir)

    for ph in [5.0, 7.4] :
        print(ph)
        s_ph = '%s'%ph # to work linux with for loop, linux does not seem to read int so change to str
        ph_10 = '%s'%(ph*10)
        subprocess.call("foldx --command=" + cmd + " --pdb=" + protein_pdb + " --pH=" + s_ph
        + " --output-dir=" + dir + " --output-file=" + protein + '_' + ph_10 , shell=True)

if not os.path.isdir('Summary') :
    os.mkdir('Summary')

for i in range(5) :
    protein = pdb + '_%d'%i
    subprocess.call("cp " + protein +"/Summary_*.* ./Summary", shell=True)


"""
#1/bin/bash

pdb=5uu5_origin_A2_$1.pdb
name=$( echo $pdb | cut -d "." -f1)


if [ ! -d "$name" ]; then mkdir $name; fi
for i in 5.0 7.4
do
    multi=$(echo $i*10|bc)
    foldx --command=AnalyseComplex --pdb=$pdb --pH=$i --output-dir="./$name" --output-file=""$name"_"$multi""
done

mkdir Summary
cp "$name"/Summary_*.* ./Summary
"""
