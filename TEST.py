class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.read = 50

    def get_d_mame(self):
        print(f"{self.make}, {self.model}, {self.year},пробіг {self.read}")


    def read_od(self):
        print(f"Пробіг авто {self.read} км.")

    def up_od(self, mil):
        if mil >= self.read :
            self.read = mil
        else:
            print ("fucke you")

    def plus_od(self, mil_plus):
        self.read += mil_plus


my_n_car = Car('BMW', "535", "2015")

my_n_car.get_d_mame()

my_n_car.read_od()
print(my_n_car.make)
my_n_car.up_od(60)
my_n_car.read_od()
my_n_car.plus_od(45)
my_n_car.read_od()
