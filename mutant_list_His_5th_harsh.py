import subprocess, os, sys

"""
protein = input("what's your protein.pdb? : ")
chain = input("which chain do you want to use? : ")
mutation = input("which mutation do you want to introduce? : ")
candidates = input("Please enter your candidates file name in txt : ")
"""
#-----variables------------------------------------
protein = '5uu5_origin_' # pdb file name
chain = 'A' # first chain for seq_extractor.py
mutation = 'H' # mutated amino acid
candidates = 'candidates_harsh.txt' # candidates file with text, do not change this file
chain_kind = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] # the kind of chains of protein you will use

#-----open pdb file and extract the sequnece-----------

for order in range(1,  20 + 1) :
    protein_candidates = protein + str(order) + '.pdb'
    print(protein_candidates)
    seq = subprocess.Popen(['seq_extractor.py', protein_candidates, chain], stdout=subprocess.PIPE)
    out, err = seq.communicate()

    out_decode = out.decode().rstrip()
    #print('sequence of protein :', out_decode) # indicates the sequence of protein
    #print('length of protein :', len(out_decode)) # indicates the length of protein

#-----open candidates file and make final individual_list-------
    f_mutant_file = open('individual_list%d.txt'%order, 'w') # create text file of which name is 'mutant_list.txt'
    f_candidates = open(candidates, 'r')
    for residues in f_candidates :
        residue = residues.split(',')
        for res in residue :
            if len(res) == 0 : continue
            else :
                #print(type(res))

                a = 0 # for counting, to add ;\n at the last one
                for j in chain_kind :
                    a = a + 1
                    int_res = int(res)
                    mutant = out_decode[int(res)-1] + j + res + mutation #NA146H, NB146H, NC146H...
                    #print(mutant)
                    if a < len(chain_kind) :
                        f_mutant_file.write(mutant + ',')
                    else :
                        f_mutant_file.write(mutant + ';\n') #add ;\n at the end of the last one

    f_mutant_file.close()
    f_candidates.close()
