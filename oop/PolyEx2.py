class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        print("Driving around")


class Plane:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        print("flying around")


class Motorbike:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        print("Ride around")


#instance of our class
car = Car("Toyota", "MarkX")
plane = Plane("Boeing", "797")
bike =Motorbike("Kawasaki", "Ninja650")

for i in (car, plane, bike):
    i.move()