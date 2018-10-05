# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour

fname = 'mbox-short.txt'
fh = open(fname)

# Build a dictionary of key:hour, value: frequency of occurence
hour_histogram = dict()
for line in fh:
    if not line.startswith('From '): continue
    words = line.split()
    hour = words[5].split(':')[0]
    hour_histogram[hour] = hour_histogram.get(hour, 0) + 1

# Build a list of tuple with the dictionary. Because list can only be sorted.
hourhistlist = sorted(hour_histogram.items())

for tup in hourhistlist:
    print (tup[0], tup[1])
