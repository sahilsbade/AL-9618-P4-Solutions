class Character:
    # self.__Name : STRING
    # self.__XCoordinate : INTEGER
    # self.__YCoordinate : INTEGER

    def __init__(self, CName, CXCoord, CYCoord):
        self.__Name = CName
        self.__XCoordinate = CXCoord
        self.__YCoordinate = CYCoord

    def GetName(self):
        return self.__Name

    def GetX(self):
        return self.__XCoordinate

    def GetY(self):
        return self.__YCoordinate

    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate = self.__XCoordinate + XChange
        self.__YCoordinate = self.__YCoordinate + YChange


cArr = [] * 10

try:
    File = open("Characters.txt", 'r')
    for X in range(10):
        Name = File.readline().strip()
        XCoord = int(File.readline().strip())
        YCoord = int(File.readline().strip())
        cArr.append(Character(Name, XCoord, YCoord))
    File.close()

except IOError:
    print("File not found")

pos = -1
cName = ""
while pos == -1:
    cName = str(input("Enter Character: ")).lower()
    for i in range(10):
        if cName == cArr[i].GetName().lower():
            pos = i

IsValid = False
while not IsValid:
    Move = input("Enter A for left, W for up, S for down, or D for right: ")

    if Move.upper() == "A":
        cArr[pos].ChangePosition(-1, 0)
        IsValid = True

    elif Move.upper() == "W":
        cArr[pos].ChangePosition(0, 1)
        IsValid = True

    elif Move.upper() == "S":
        cArr[pos].ChangePosition(0, -1)
        IsValid = True

    elif Move.upper() == "D":
        cArr[pos].ChangePosition(1, 0)
        IsValid = True

print(cName, " has changed coordinate to X = ",
      str(cArr[pos].GetX()), " Y = ", str(cArr[pos].GetY()))
