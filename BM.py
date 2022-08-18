import os, sys, subprocess, mutant_list # to use linux

cmd = "BuildModel " # command which foldx can read
pdb = mutant_list.protein # protein file in pdb
mt_list = "mutant_file.txt " # mutation list in txt
numberOfRuns = "5"

#for i in range(1, 5+1) :
#    number = '%d'%i # to work linux with for loop, linux does not seem to read int so change to str

subprocess.call("foldx --command=" + cmd + "--pdb=" + pdb + " --mutant-file="
+ mt_list + "--numberOfRuns=" + numberOfRuns, shell=True)
