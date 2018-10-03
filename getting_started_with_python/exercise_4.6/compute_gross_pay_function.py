# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation.
# The function should return a value

hours = input("Enter the hours: ")
hours = float(hours)
rate = input("Enter the rate per hour: ")
rate = float(rate)

def computepay(hours, rate):
    if hours < 40:
        return hours * rate
    else:
        return (40 * rate) + ((hours - 40) * 1.5 * rate)

gross_pay = computepay(hours, rate)
print (gross_pay)
