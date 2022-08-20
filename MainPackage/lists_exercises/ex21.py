# Bullsi Game
from random import randint

list1 = []
hits_count = 0
bools_count = 0
try_count = 0
won = False
invalid = False

for i in range(4):
    num = randint(0, 9)
    while num in list1:
        num = randint(1, 9)
    list1.append(num)
# print(list1)

while not won:
    guss = input("Guss the nuber: ")
    try_count += 1

    for number in guss:
        if int(number) in list1:
            if list1.index(int(number)) == guss.index(number):
                bools_count += 1
            else:
                hits_count += 1
    if bools_count == 4:
        won = True
    else:
        print(f"Bools: {bools_count}, Hits {hits_count}")
    bools_count = 0
    hits_count = 0

print(f"OMG you win!!!, tries {try_count}")
