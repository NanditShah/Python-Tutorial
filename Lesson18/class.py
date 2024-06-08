class Vehicle():
    def __init__(self,make,model):
        self.make = make
        self.model = model
    
    def moveForward(self):
        print(f'{self.model} is moving forward')
    
    def getInfo(self):
        print(f'I am a {self.make} {self.model}')

car1 = Vehicle('Tesla','S3')
car1.moveForward()
car1.getInfo()

car2 = Vehicle('Toyota','Innova')
car2.moveForward()
car2.getInfo()

####################################
# Inheritance

class Airplane(Vehicle):
    def __init__(self,make,model,modelNum):
        super().__init__(make,model)
        self.modelNum = modelNum

    def getModelNum(self):
        print(f'Model number is {self.modelNum}')

    def getInfo(self):
        print(f'I am a {self.make} {self.model}({self.modelNum})')


myAirplane = Airplane('Boeing','A1','N-12345')
myAirplane.moveForward()
myAirplane.getInfo()
myAirplane.getModelNum()


class GolfKart(Vehicle):
    pass

myGolfKart = GolfKart('Yamaha','Defender')
myGolfKart.moveForward()
myGolfKart.getInfo()

####################################