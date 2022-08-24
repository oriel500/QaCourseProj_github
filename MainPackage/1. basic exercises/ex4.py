name = input("Enter Name: ")
year = int(input("Enter This Year: "))
age = int(input("Enter Age: "))
nextYear = int(input("Enter other year in future: "))
diff = nextYear - year

print(f"{name} will be {age+diff} in year {nextYear}")
