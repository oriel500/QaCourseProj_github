# get from the user full name, age, city
first_name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print(f"Your full name is {first_name.capitalize()} {last_name.capitalize()}"
      f"\nYour age is {age}"
      f"\nYou are livnig in {city.capitalize()}")
