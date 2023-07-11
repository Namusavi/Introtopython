class Base:
    def __init__(self):
        self.a ="I have rights"
        self.c ="and priviledges"
        self.d = "more rights"
        self.e = "and power"

class Derived(Base):
    def __init__(self):
        print(self.a)
        print(self.c)
        print(self.d)
        print(self.e)



#create an instance of the parent class
obj1 =Base()
print(obj1.a)
print(obj1.c)
print(obj1.d)
print(obj1.e)