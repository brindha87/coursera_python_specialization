import re

fname = 'textandnumbers.txt'
fh = open(fname)

numlist = list()
for line in fh:
    match = re.findall('[0-9]+', line)
    if len(match) < 1: continue
    for i in match:
        num = int(i)
        numlist.append(num)

print ('Sum:', sum(numlist))
