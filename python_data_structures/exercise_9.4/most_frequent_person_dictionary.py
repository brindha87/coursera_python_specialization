# Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = 'mbox-short.txt'
fh = open(fname)
person = dict()

# Build a histogram dictionary
for line in fh:
    if not line.startswith('From '): continue
    words = line.split()
    name = words[1]
    person[name] = person.get(name, 0) + 1

# Find the person who occured most
bigkey = None
bigval = None
for key, value in person.items():
    if bigval is None or value > bigval:
        bigkey = key
        bigval = value

# Prints the person occured most along with the frequency of occurence
print (bigkey, bigval)
