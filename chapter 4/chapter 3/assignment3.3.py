hrs = float(input("Enter hours: "))
rate = float(input("Enter the rate per hour: "))
if hrs <= 40:
    pay = rate * hrs
else:
    moreHours = hrs - 40
    pay = rate * 40 + rate*1.5 * moreHours
print(pay)
