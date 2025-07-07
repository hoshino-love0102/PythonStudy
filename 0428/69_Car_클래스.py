class Car:
    def __init__(self, displ, drv):
        self.displ = displ
        self.drv = drv

    def into(self):
        return f"{self.displ},{self.drv}"

car = Car(2.0, 'f')
print(car.into())
