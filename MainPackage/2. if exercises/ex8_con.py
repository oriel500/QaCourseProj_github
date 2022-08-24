d = int(input("enter day: "))
m = int(input("enter month: "))
y = int(input("enter year: "))

if 1 <= d <= 31:
    if 1 <= m <= 12:
        if 1950 <= y <= 2022:
            if d < 10:
                d = '0' + str(d)
            if m < 10:
                m = '0' + str(m)
            print(f"{d}/{m}/{y % 100 // 10}{y % 10}")
        else:
            print("year invalid")
    else:
        print("month invalid")
else:
    print("day invalid")



