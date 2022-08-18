import sys, os, subprocess
from itertools import combinations

#-----variables------------------------------------
protein = '5uu5_origin_combination_' # pdb file name
chain = 'A' # first chain for seq_extractor.py
mutation = 'H' # mutated amino acid
#candidates = 'candidates.txt' # candidates file with text, do not change this file
chain_kind = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] # the kind of chains of protein you will use
combination_range = 9

#-----open candidates file that should be conbinated-----
combination_candidates = 'candidates_combination.txt'
candidates = open(combination_candidates, 'r').readlines()[0].rstrip()

#-----define combination function which save combinations as a list-----
l_candidates = candidates.split(',')

def candi_combi(r) :
    return list(combinations(l_candidates, r))

#for i in range(1, 10) :
#    print(len(candi_combi(i)))

#-----open pdb file and extract the sequnece-----------

for order in range(1,  combination_range + 1) : # mutation order
    protein_candidates = protein + str(order) + '.pdb'
    print(protein_candidates)
    seq = subprocess.Popen(['seq_extractor.py', protein_candidates, chain], stdout=subprocess.PIPE)
    out, err = seq.communicate()

    out_decode = out.decode().rstrip()
    #print('sequence of protein :', out_decode) # indicates the sequence of protein
    #print('length of protein :', len(out_decode)) # indicates the length of protein

#-----make final individual_list using combination lists-------
    f_mutant_file = open('individual_list%d.txt'%order, 'w') # create text file of which name is 'mutant_list.txt'
    #f_candidates = open(candidates, 'r')
    print(candi_combi(order))
    for combi in candi_combi(order) :
        i = 0
        #print(len(combi))
        while i < len(combi) :
            end = 0
            for chain in chain_kind :
                end = end + 1
                i_combi = int(combi[i])
                mutant = out_decode[i_combi-1] + chain + combi[i] + mutation #NA146H, NB146H, NC146H...
                #print(mutant)
                if end < len(chain_kind) or i + 1 < len(combi) :
                    f_mutant_file.write(mutant + ',')
                else :
                    f_mutant_file.write(mutant + ';\n') #add ;\n at the end of the last one
            i = i + 1
    f_mutant_file.close()
