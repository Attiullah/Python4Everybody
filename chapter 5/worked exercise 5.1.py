tot = 0
count = 0
while True:
    given = input("Enter a number: ")
    if given == 'Done':
        break
    try:
        gf = float(given)
        print(gf)
    except:
        print("Wrong input!! try Again")
        continue
    count  = count + 1
    tot = tot + gf
print(tot, count, tot/count)
