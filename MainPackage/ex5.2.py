# get from the user full name, age, city
first_name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("Your full name is {0} {1}".format(first_name.capitalize(), last_name.capitalize()))
print("Your age is {0}".format(age))
print("You are living in {0}".format(city.capitalize()))
