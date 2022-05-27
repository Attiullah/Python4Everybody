big = max("Hey there")
print(big )


def computepay(hrs, rate):
    if hrs <= 40:
        return rate * hrs
    else:
        return 40 * rate + (hrs - 40) *1.5 *rate
hrs = float(input("Enter number of hours: "))
rate = float(input("Enter the rate: "))
print("Pay", computepay(hrs, rate))