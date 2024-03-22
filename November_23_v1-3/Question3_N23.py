class Character:
    # self.__Name: str
    # self.__XPosition: int
    # self.__YPosition: int
    def __init__(self, CName: str, CXPosition: int, CYPosition: int):
        self.__Name: str = CName
        self.__XPosition: int = CXPosition
        self.__YPosition: int = CYPosition

    def GetXPosition(self) -> int:
        return self.__XPosition

    def GetYPosition(self) -> int:
        return self.__YPosition

    def SetXPosition(self, value: int):
        self.__XPosition += value
        if self.__XPosition > 10000:
            self.__XPosition = 10000
        elif self.__XPosition < 0:
            self.__XPosition = 0

    def SetYPosition(self, value: int):
        self.__YPosition += value
        if self.__YPosition > 10000:
            self.__YPosition = 10000
        elif self.__YPosition < 0:
            self.__YPosition = 0

    def Move(self, direction: str):
        if direction == "up":
            self.SetYPosition(10)
        elif direction == "down":
            self.SetYPosition(-10)
        elif direction == "right":
            self.SetXPosition(10)
        else:
            self.SetXPosition(-10)


class BikeCharacter(Character):
    def __init__(self, CName: str, CXPosition: int, CYPosition: int):
        super().__init__(CName, CXPosition, CYPosition)

    def Move(self, direction: str):
        if direction == "up":
            self.SetYPosition(20)
        elif direction == "down":
            self.SetYPosition(-20)
        elif direction == "right":
            self.SetXPosition(20)
        else:
            self.SetXPosition(-20)


"""main"""
Jack = Character("Jack", 50, 50)
Karla = BikeCharacter("Karla", 100, 50)

CharacterInput = input("Do you want to move Jack or Karla? ").strip().lower()
while CharacterInput != "jack" and CharacterInput != "karla":
    CharacterInput = input("Invalid choice, please choose either Jack or Karla. ").strip().lower()

DirectionInput = input(f"Do you want to move {CharacterInput[0].upper() + CharacterInput[1:]} "
                       f"up, down, left, or right? ").strip().lower()
while DirectionInput != "up" and DirectionInput != "down" and DirectionInput != "left" and DirectionInput != "right":
    DirectionInput = input("Invalid choice, please choose amongst up, down, left, and right. ").strip().lower()

if CharacterInput == "jack":
    Jack.Move(DirectionInput)
    print(f"Jack's new position is X = {Jack.GetXPosition()}, Y = {Jack.GetYPosition()}")
else:
    Karla.Move(DirectionInput)
    print(f"Karla's new position is X = {Karla.GetXPosition()}, Y = {Karla.GetYPosition()}")
