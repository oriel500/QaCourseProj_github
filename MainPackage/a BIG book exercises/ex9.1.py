from datetime import datetime

name = input("Enter name: ")
age = int(input("Enter age: "))

born_year = datetime.now().year - age
date100 = datetime(born_year+100, 8, 21)
print(date100.strftime("%Y"))
