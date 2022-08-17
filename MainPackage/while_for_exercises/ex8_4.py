for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    is_prime = True

    # check if the number prime
    if num <= 1:
        is_prime = False
    for number in range(2, num):
        if num % number == 0:
            is_prime = False

    # check the smallest number if is prime
    if is_prime:
        if i == 0:
            min = num
        if num < min:
            min = num

if is_prime:
    print(min)
else:
    print("All the number not prime")
