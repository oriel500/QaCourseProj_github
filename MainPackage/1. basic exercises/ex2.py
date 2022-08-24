
d = int(input("Enter Day: "))
m = int(input("Enter Month: "))
y = int(input("Enter year: "))
y_right = y % 10
y_left = y // 10 % 10

print(f"{d}/{m}/{y_left}{y_right}")

