import subprocess, os, sys
"""
protein = input("what's your protein.pdb? : ")
chain = input("which chain do you want to use? : ")
mutation = input("which mutation do you want to introduce? : ")
candidates = input("Please enter your candidates file name in txt : ")
"""
protein = '5uu5_origin.pdb'
chain = 'A'
mutation = 'H'
#candidates = 'candidates.txt'
chain_kind = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] # This means the kind of chains of protein you will use

"""
f_candidates = open(candidates, 'r')
for a in f_candidates.readlines() :
    residue_numbers = a.split() # read whole resdidue numbers
"""

#residue_number = (1, 3, 4, 7, 10)

seq = subprocess.Popen(['seq_extractor.py', protein, chain], stdout=subprocess.PIPE)
out, err = seq.communicate()

out_decode = out.decode().rstrip()
print('sequence of protein :', out_decode) # indicates the sequence of protein
print('length of protein :', len(out_decode)) # indicates the length of protein

for gap in range(1, 430+1, 30) :
    print(gap)
    f_mutant_file = open('individual_list%d.txt'%gap, 'w') # create text file of which name is 'mutant_list.txt'
    #for residue in residue_numbers :
    for residue in range(gap, gap + 30) :
        a = 0 # for counting
        for j in chain_kind :
            a = a + 1
            str_residue = str(residue)
            mutant = out_decode[residue-1] + j + str_residue + mutation
            print(mutant)
            if a < len(chain_kind) :
                f_mutant_file.write(mutant + ',')
            else :
                f_mutant_file.write(mutant + ';\n')

f_mutant_file.close()
#f_candidates.close()
