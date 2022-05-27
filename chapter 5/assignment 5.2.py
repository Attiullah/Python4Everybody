smallest = None
largest = None
while True:
    try:
        number = input("Enter a number: ")
        if number == "done":
            break
        fn = int(number)

        if smallest is None or fn < smallest:
            smallest = fn
        elif largest is None or fn > largest:
            largest = fn
    except:
        print("Invalid input")
        continue
print("Minimum is", smallest)
print("Maximum is", largest)