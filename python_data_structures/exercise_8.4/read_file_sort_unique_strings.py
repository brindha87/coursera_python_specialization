# Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = 'romeo.txt'
fh = open(fname)

# Build a list of words
words = list()
for line in fh:
    words_in_current_line = line.split()
    for w in words_in_current_line:
        if w in words: continue
        words.append(w)

words.sort()
print (words)
