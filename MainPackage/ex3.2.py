num = int(input("enter number: "))
flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

    if flag:
        print("not prime number")
    else:
        print("prime number")
else:
    print("not prime number")






