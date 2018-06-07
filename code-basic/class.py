class Car(object):
    wheels = 4 

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self): 
        print("..brroom", self.make, self.model, "started")

myCar = Car("Suzuki", "Swift")
yourCar = Car("Ford", "Mastang")
print (myCar.make, "Wheels", myCar.wheels)
myCar.start()
print (yourCar.make, "Wheels", myCar.wheels)
yourCar.start()


