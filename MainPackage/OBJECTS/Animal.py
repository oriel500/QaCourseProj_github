class Animal:

    def __init__(self, _name: str):
        self.name = _name
        self.l_hunger = 5.0
        self.l_energy = 5.0

    def eat(self, amount_food: int):
        self.l_hunger -= (amount_food / 50)
        self.l_energy -= (amount_food / 100)

        # if level of hunger below to 0, take off the remaining grams/100 from energy
        if self.l_hunger < 0:
            print("#The animal don't finish the food")
            amount_food = (self.l_hunger * 50) * -1
            self.l_hunger = 0
            self.l_energy -= amount_food / 100
        if self.l_energy < 0:
            print("#The animal need to rest")
            self.l_energy = 0

    def play(self, min1):
        self.l_energy -= (min1 / 10) * 2
        self.l_hunger += (min1 / 10) * 2

        # if level of energy below to 0, take down to remaining time/10 from hunger
        if self.l_energy < 0:
            print("#The animal stop in the middle because he tiered")
            min1 = (self.l_energy * 5) * -1
            self.l_energy = 0
            self.l_hunger += (min1 / 10)
            if self.l_hunger > 10:
                self.l_hunger = 10

    def rest(self, min1: int):
        self.l_energy += (min1 / 20)
        self.l_hunger += (min1 / 30)

        if self.l_energy > 10 and self.l_hunger <= 10:
            print("#The animal done to rest and want to play")
            min1 = (self.l_energy - 10) * 20
            self.l_energy = 10
            self.l_hunger += (min1 / 30)
            if self.l_hunger > 10:
                self.l_hunger = 10

        elif self.l_hunger > 10 and self.l_energy <= 10:
            print("#The animal done to rest and want to eat")
            min1 = (self.l_hunger - 10) * 30
            self.l_hunger = 10
            self.l_energy += (min1 / 20)
            if self.l_energy > 10:
                self.l_energy = 10

        elif self.l_hunger > 10 and self.l_energy > 10:
            print("#The animal done to rest and want eat and play!")
            self.l_hunger = 10
            self.l_energy = 10

    def __str__(self):
        return f'Name of animal: {self.name}\n#level hunger: {round(self.l_hunger,2)}\n#level energy: {round(self.l_energy,2)}'


# ==main==
if __name__ == "__main__":
    # create animal
    name = input("Enter name of animal: ")
    animal = Animal(name)
    print("CREATE ANIMAL")
    print("=======================")
    print(animal)
    print("=======================")
    print("Choose action to do with animal:\n1- Eat\n2- Play\n3- Rest\n4- End")
    action = int(input("Enter action: "))

    # choose action. if choose 0 end the program
    while action != 0:
        if action == 1:
            action = int(input("Enter amount of food (gram unit): "))
            animal.eat(action)
            action = 1
        elif action == 2:
            action = int(input("Enter how much time he play (in a minuet): "))
            animal.play(action)
            action = 2
        elif action == 3:
            action = int(input("Enter how much time he rest (in a minuet): "))
            animal.rest(action)
            action = 3
        elif action == 0:
            pass
        else:
            print("Invalid action...")
            action = int(input("Enter action again: "))
        if 1 <= action <= 3:
            print("=======================")
            print(animal)
            print("=======================")
            print("Choose action to do with animal:\n1- Eat\n2- Play\n3- Rest\n4- End")
            action = int(input("Enter action: "))

