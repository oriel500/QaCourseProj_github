class Car:
    """The car class holds information and methods about car"""

    def __init__(self, fcompany="shevrolet", fcolor="orange", fkind="mini", fkm=600):
        self.company = fcompany
        self.color = fcolor
        self.kind = fkind
        self.km = fkm

    def print_car(self):
        print(f'{self.company} {self.color} {self.kind} {self.km}')

    def __str__(self):
        return 'Amazing car'


# == main ==
if __name__ == "__main__":
    car_orange = Car()
    car_orange.print_car()
    print(car_orange.color)
    print(car_orange.__dir__()) # all the תכונות of object
    print(car_orange.__dict__)
    print(car_orange)
