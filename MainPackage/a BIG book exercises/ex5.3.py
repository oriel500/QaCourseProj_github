# get from user address
info = input("Enter your street, house number and city: ")
arr = info.split()
print(f"You are living in {arr[2]}\n"
      f"Your street is {arr[0]}\n"
      f"Your numer house is {arr[1]}")

