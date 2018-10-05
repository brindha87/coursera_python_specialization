# Write a program that prompts for a file name
# then opens that file and reads through the file
# and print the contents of the file in upper case

fname = input('Enter a file name: ')
fhand = open(fname)
file_content = fhand.read()
uppercase_content = file_content.upper()
print (uppercase_content.rstrip())
