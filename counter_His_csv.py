import sys, csv

candidates_file = 'His_6th_candidates2_harsh.csv'
candidates = open(candidates_file, 'r').readlines()
range_limit = 238
#top = 10

#----open candidates and save residues in sorted way----
candidates_origin = open('candidates_harsh.txt', 'r').readlines()[0].split(',')
residues_origin = list()
for i in candidates_origin :
    if len(i) <1 : continue
    residues_origin.append(int(i))
residues_origin.sort()
#print(residues_origin)

#----open new files with header----------
output = "His_counting.csv" # new file
data = open(output, 'wb')
output_writer = csv.writer(data)
header = ["Top"] + residues_origin
output_writer.writerow(header)

#----collect whole residues in a list----

for i in range(10, range_limit + 1, 10) :
    print("Top %d"%i)
    residues = list()
    i_residues = list()
    for j in range(1, i) :
        residue = candidates[j].rstrip().split(',')[6:]
        residues = residues + residue
    for k in residues :
        i_residues.append(int(k))
    #print(residues)
    #print(i_residues)

#----count each residue----
    counter = dict()
    for r in i_residues :
        counter[r] = counter.get(r, 0) + 1
    #print(counter)

    #----convert to a list----
    counter_list = list()
    for l in residues_origin :
        #print(l)
        #print(counter.keys())
        if not l in counter.keys() :
            counter_list.append(0)
        else : counter_list.append(counter[l]/float(i))

    #print(counter_list)

    #----save counter_list to outout in csv---
    row = [i] + counter_list
    output_writer.writerow(row)

data.close()
