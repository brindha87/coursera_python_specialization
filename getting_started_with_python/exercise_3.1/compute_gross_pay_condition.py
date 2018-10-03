# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours

hours = input("Enter the number of hours: ")
hours = float(hours)
rate = input("Enter hourly rate: ")
rate = float(rate)
if hours < 40:
    gross_pay = hours * rate
else:
    gross_pay = (40 * rate) + ((hours - 40) * 1.5 * rate)
print (gross_pay)
