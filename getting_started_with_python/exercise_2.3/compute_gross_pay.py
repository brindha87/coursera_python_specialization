# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Use 35 hours and a rate of 2.75 per hour to test the program
# You should use input to read a string and float() to convert the string to a number.

hrs = input("Enter Hours:")
hourly_rate = input("Enter rate per hour: ")
gross_pay = float(hrs) * float(hourly_rate)
print ("Pay:", gross_pay)
