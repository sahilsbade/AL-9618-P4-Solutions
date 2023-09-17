class Vehicle:
    # self.__ID string
    # self.__MaxSpeed integer
    # self.__CurrentSpeed integer
    # self.__IncreaseAmount integer
    # self.__HorizontalPosition integer

    def __init__(self, PID, PMaxSpeed, PIncreaseAmount):
        self.__ID = PID
        self.__MaxSpeed = PMaxSpeed
        self.__IncreaseAmount = PIncreaseAmount
        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0

    def getCurrentSpeed(self):
        return self.__CurrentSpeed

    def getIncreaseAmount(self):
        return self.__IncreaseAmount

    def getMaxSpeed(self):
        return self.__MaxSpeed

    def getHorizontalPosition(self):
        return self.__HorizontalPosition

    def SetCurrentSpeed(self, CSP):
        self.__CurrentSpeed = CSP

    def SetHorizontalPosition(self, HPP):
        self.__HorizontalPosition = HPP

    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount

        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed

        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed

    def getCurrentPosition(self):
        print("Current position: {}".format(self.__HorizontalPosition))
        print("Current speed: {}".format(self.__CurrentSpeed))

class Helicopter (Vehicle):
    # VerticalPosition integer
    # VerticalChange integer
    # MaxHeight integer

    def __init__(self, PID, PMaxSpeed, PIncreaseAmount, PVertChange, PMaxHeight):
        Vehicle.__init__(self, PID, PMaxSpeed, PIncreaseAmount)

        self.__VerticalPosition = 0
        self.__VerticalChange = PVertChange
        self.__MaxHeight = PMaxHeight

    def IncreaseSpeed(self):
        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight

        Vehicle.SetCurrentSpeed(self, Vehicle.getCurrentSpeed(self) + Vehicle.getIncreaseAmount(self))

        if Vehicle.getCurrentSpeed(self) > Vehicle.getMaxSpeed(self):
            Vehicle.SetCurrentSpeed(self, Vehicle.getMaxSpeed(self))

        Vehicle.SetHorizontalPosition(self, Vehicle.getCurrentSpeed(self) + Vehicle.getHorizontalPosition(self))

    def getCurrentPosition(self):
        print(f"Current position: {Vehicle.getHorizontalPosition(self)}")
        print(f"Current speed: {Vehicle.getCurrentSpeed(self)}")


# main program
Car = Vehicle("Tiger", 100, 20)

Heli = Helicopter("Lion", 350, 40, 3, 100)

Car.IncreaseSpeed()
Car.IncreaseSpeed()
Car.getCurrentPosition()
print("")
Heli.IncreaseSpeed()
Heli.IncreaseSpeed()
Heli.getCurrentPosition()

