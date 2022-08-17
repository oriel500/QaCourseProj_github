user_name = input("Enter your name: ")
salary = int(input("Enter your salary: "))
percent = int(input("Enter your precent: "))
salary = salary + (percent/100)*salary
print(salary)