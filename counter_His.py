import sys

candidates_file = 'His_6th_candidates2_harsh.csv'
candidates = open(candidates_file, 'r').readlines()
range_limit = int(sys.argv[1])
top = 10

#----collect whole residues in a list----
residues = list()
for i in range(1, range_limit) :
    residue = candidates[i].rstrip().split(',')[6:]
    residues = residues + residue

#----count each residue----
counter = dict()
for r in residues :
    counter[r] = counter.get(r, 0) + 1

#----convert to a list----
counter_list = list()
for k, v in counter.items() :
    a = (v, k)
    counter_list.append(a)
counter_list.sort()
counter_list.reverse()

#----print!!----
print('Within %d samples, top %d candidates are'%(range_limit, top))
for i in range(top) :
    count, residue = counter_list[i]
    print('residue %s, %d times, %.1f percent'%(residue, count, count/float(range_limit)*100))
