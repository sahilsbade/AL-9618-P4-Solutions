class TreasureChest:
    # __question : string
    # __answer : integer
    # __points : integer
    def __init__(self, CQuestion, CAnswer, CPoints):
        self.__question = CQuestion
        self.__answer = CAnswer
        self.__points = CPoints

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, UAnswer):
        if int(UAnswer) == self.__answer:
            return True
        else:
            return False

    def getPoints(self, UAttempts):
        if UAttempts == 1:
            return self.__points
        elif UAttempts == 2:
            return self.__points // 2
        elif UAttempts == 3 or UAttempts == 4:
            return self.__points // 4


arrayTreasure = []  # 5 of type TreasureChest


def readData():
    filename = "TreasureChestData.txt"
    try:
        File = open(filename, "r")
        read_data = (File.readline()).strip()

        while read_data != "":
            question = read_data
            ans = int((File.readline()).strip())
            points = int((File.readline()).strip())
            arrayTreasure.append(TreasureChest(question, ans, points))
            read_data = (File.readline()).strip()

        File.close()
    except IOError:
        print("File not found")


readData()
choice = int(input("Enter a number between 1 and 5: ")) - 1

if -1 < choice < 5:

    result = False
    attempts = 0

    while not result:
        print(arrayTreasure[choice].getQuestion())
        answer = int(input("Enter answer: "))
        result = arrayTreasure[choice].checkAnswer(answer)
        attempts += 1

    print(int(arrayTreasure[choice].getPoints(attempts)))
