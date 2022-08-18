import os, sys, csv

f_save = open('His_combi_candidates_compiled.csv', 'wb')
output_writer = csv.writer(f_save)
value = ["ddG at pH 5.0", "ddG at pH 7.4", "pH5.0-7.4"]
condition = ["pH5.0>7.4", "pH7.4<10"] #pH7.4<10 is not considered
candidates = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th"]
header = ["MT"] + value + condition + candidates
output_writer.writerow(header)

for i in range(1, 7+1) :
    f_name = 'His_combi_candidates_%d.csv'%i
    f_file = open(f_name, 'r').readlines()[1:]
    for j in range(len(f_file)) :
        data = f_file[j].rstrip().split(',')
        print(data)
        output_writer.writerow(data)
