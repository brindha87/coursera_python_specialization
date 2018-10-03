# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.

largest = None
smallest = None

while True:
    input_val = input('Enter a Number: ')
    if input_val == 'done':
        break
    try:
        val = int(input_val)
    except:
        print ('Invalid input')
        continue

    if largest is None:
        largest = val
    elif val > largest:
        largest = val

    if smallest is None:
        smallest = val
    elif val < smallest:
        smallest = val

print ('Maximum is', largest)
print ('Minimum is', smallest)
