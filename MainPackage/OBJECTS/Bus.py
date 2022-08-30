class Bus:

    def __init__(self, num_seats: int):
        self.count_pass = 0  # number of how many passengers on the bus right now
        self.seats = []  # list of seats

        # create free bus
        for i in range(num_seats):
            self.seats.append("free")

    def get_on(self, name: str):
        """get name and add to bus in first free seat"""
        """if the bus full, print massage with name and return None"""

        # full bus
        if "free" not in self.seats:
            print(f"#The bus is full, the passanger {name} did not get on the bus")
        # have free seat
        else:
            for i in range(len(self.seats)):
                if self.seats[i] == "free":
                    self.seats[i] = name
                    self.count_pass += 1
                    break

    def get_off(self, name: str):
        """get first name and taking him off the bus"""

        if name not in self.seats:
            print("#The passanger not on the bus")
        else:
            for i in range(len(self.seats)):
                if self.seats[i] == name:
                    self.seats[i] = "free"
                    self.count_pass -= 1
                    break

    def __str__(self):
        return f"{str(self.seats)},\nnumber of passangers: {self.count_pass}"


# ==main==
if __name__ == "__main__":
    bus = Bus(5)
    print("The choise of actions is\n1- add passenger\n2- remove passenger\n0- end the program")
    action = int(input("enter number of action: "))

    while action != 0:
        name = input("enter name of passenger: ")
        if action == 1:
            bus.get_on(name)
        elif action == 2:
            bus.get_off(name)
        print("==========================================")
        print("The choise of actions is\n1- add passenger\n2- remove passenger\n0- end the program")
        action = int(input("enter number of action again: "))

    print("==========================================")
    print(bus)
