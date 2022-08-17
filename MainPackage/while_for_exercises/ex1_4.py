num = int(input("Enter number: "))
is_prime = True

for number in range(2, num):
    if num % number == 0:
        is_prime = False
        break

if is_prime:
    print("The number is prime")
else:
    print("The number is not prime")
