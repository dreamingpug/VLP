import os, sys, csv

#-------please rename the raw with your original file---------
raw = "His_1st_IE.csv" # original file
fhand = open(raw, 'r')
lines = fhand.readlines()

#----WT values of ddG at pH 5.0 and 7.4--------
WT_ddG = "WT_ddG.csv"
WT_values = open(WT_ddG, 'r').readlines()
for WT_value in WT_values :
    WT_ddG_50 = float(WT_value.split(',')[1])
    WT_ddG_74 = float(WT_value.split(',')[2].rstrip())
#print(WT_ddG_50, WT_ddG_74)

#----open new files with header----------
output = "His_1st_candidates_harsh.csv" # new file
data = open(output, 'wb')
output_writer = csv.writer(data)
value = ["ddG at pH 5.0", "ddG at pH 7.4", "pH5.0-7.4"]
condition = ["pH5.0>7.4", "pH7.4<10"]
header = ["MT"] + value + condition
output_writer.writerow(header)

#-----conditions----------------------------
list_candidates = list()

for line in lines :
    values = line.rstrip()
    name = values.split(",")[0]
    #print(name)
    ddG_50 = float(values.split(",")[1]) - WT_ddG_50
    ddG_74 = float(values.split(",")[2]) - WT_ddG_74
    ddG_50_74 = ddG_50 - ddG_74

    if ddG_50 > ddG_74 : ddG_50_is_bigger = 1
    else : ddG_50_is_bigger = 0
    if ddG_74 < 10 : ddG_74_is_subten = 1
    else : ddG_74_is_subten = 0

    if not ddG_50_is_bigger + ddG_74_is_subten == 2 :
        continue
    else :
        row = [name] + [ddG_50, ddG_74, ddG_50_74, ddG_50_is_bigger, ddG_74_is_subten]
        list_candidates.append(row)

#print(list_candidates)

#---remove candidates with less than 3 models which meet the conditions----------------------
counts = dict()
residues = list()
junks = list()

for i in range(len(list_candidates)) :
    mutants = list_candidates[i][0]
    res = mutants.split('_')[1]
    residues.append(res)

for r in residues :
    counts[r] = counts.get(r, 0) + 1
keys = counts.keys()

for key in keys :
    if counts[key] < 3 : #conditions
        #print(key)
        for i in range(len(list_candidates)) :
            mutants = list_candidates[i][0]
            res = mutants.split('_')[1]
            if key == res :
                junks.append(list_candidates[i])

for j in junks :
    list_candidates.remove(j)

#print(junks)
#print(list_candidates)

#---select the model with the lowest ddG at pH 7.4 among same mutations-------------------

d_ddG_74 = list()
candidates = list()

for i in range(len(list_candidates)) :
    def mutants(i) :
        return list_candidates[i][0]
    def res(i) :
        return mutants(i).split('_')[1]
    def count(i) :
        return mutants(i).split('_')[2]
    def ddG_74(i) :
        return list_candidates[i][2]
    #print(mutants(i), res(i), count(i), ddG_74(i))

    try :
        if res(i) == res(i+1) :
            a = [mutants(i), res(i), count(i), ddG_74(i)]
            d_ddG_74.append(a)
            #print(d_ddG_74)
        else :
            a = [mutants(i), res(i), count(i), ddG_74(i)]
            d_ddG_74.append(a)
            #print(d_ddG_74)
            b = list()
            for j in range(len(d_ddG_74)) :
                b.append(d_ddG_74[j][3])
            #print(b, min(b))
            for j in range(len(d_ddG_74)) :
                if min(b) == d_ddG_74[j][3] :
                    print(d_ddG_74[j][0], min(b))
                    candidates.append(d_ddG_74[j][0])
                else : continue
            d_ddG_74 = list()
    except :
        a = [mutants(i), res(i), count(i), ddG_74(i)]
        d_ddG_74.append(a)
        #print(d_ddG_74)
        b = list()
        for j in range(len(d_ddG_74)) :
            b.append(d_ddG_74[j][3])
        #print(b, min(b))
        for j in range(len(d_ddG_74)) :
            if min(b) == d_ddG_74[j][3] :
                print(d_ddG_74[j][0], min(b))
                candidates.append(d_ddG_74[j][0])
            else : continue
        #print("-------", b.index(min(b)), min(b))
        d_ddG_74 = list()

print(candidates)
#----------finally make the csv file with candidates-----------
final_candidates = list()

for i in range(len(candidates)) :
    for j in range(len(list_candidates)) :
        if candidates[i] == list_candidates[j][0] :
            final_candidates.append(list_candidates[j])
        else : continue

print(final_candidates)
for i in range(len(final_candidates)) :
    data = final_candidates[i]
    output_writer.writerow(data)
