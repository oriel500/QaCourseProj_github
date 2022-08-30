from random import randint


class Loto:

    def __init__(self):
        self.LOW = 1
        self.UP = 45
        # create list
        self.numbers = self.get_numbers()
        # create money
        self.max_money = self.set_money_win()

    def get_numbers(self):
        list1 = [randint(self.LOW, self.UP) for i in range(6)]
        return list1

    def set_money_win(self):
        money = 60
        return money

    def check_guss(self, num: int):
        return num in self.numbers

    def cal_money(self, count_guss_correct: int):
        if count_guss_correct <= 1:
            return 0
        elif 2 <= count_guss_correct <= 5:
            return (self.max_money * count_guss_correct)/6
        elif count_guss_correct == 6:
            return self.max_money

    def __str__(self):
        return f'{str(self.numbers)}, max money to get: {self.max_money}'


# ==main==
if __name__ == "__main__":
    loto = Loto()
    print(loto)
    count_guss = 0

    for i in range(6):
        guss = int(input(f"enter guss number {i+1}: "))
        if guss > 45 or guss < 1:
            print("The user write number OUT OF THE RANGE, he is invalid...")
            break

        if loto.check_guss(guss):
            count_guss += 1

    print(f"The user win in {loto.cal_money(count_guss)}")
