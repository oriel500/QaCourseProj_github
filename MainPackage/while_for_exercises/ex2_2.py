password = int(input("Enter password: "))
check_password = int(input("Enter password again: "))

for i in range(4):
    if password != check_password:
        print("#The varification passward invalid#")
        check_password = int(input("Enter password again: "))

if password == check_password:
    print("The passward saved!")
else:
    print("#Too many tries#")