# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# Average spam confidence: 0.750718518519
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

fname = input('Enter a file name: ')
fhand = open(fname)

count = 0
total = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        pos = line.find(':')
        strval = line[pos+1:]
        total += float(strval.strip())

print ('Average spam confidence:', total/count)
