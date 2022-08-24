computers = input("Enter how many computer you fix today?: ")

if computers == '':
    computers = 15
else:
    computers = int(computers)

print(f"Tomorrow you need to fix {computers*2}")