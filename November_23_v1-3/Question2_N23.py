class RecordData:
    # self.__ID : string
    # self.__Total : integer
    def __init__(self, CID: str, CTotal: int):
        self.__ID = CID
        self.__Total = CTotal

    def getID(self) -> str: return self.__ID

    def getTotal(self) -> int: return self.__Total

    def setID(self, value): self.__ID = value

    def setTotal(self, value): self.__Total = value


def Enqueue(Data: str):
    global Queue
    global HeadPointer
    global TailPointer

    if TailPointer == 50:
        print("Queue is full.")
    else:
        Queue[TailPointer] = int(Data)
        TailPointer += 1
        if HeadPointer == -1:
            HeadPointer = 0


def Dequeue() -> str | int:
    global Queue
    global HeadPointer
    global TailPointer

    if HeadPointer == -1 or HeadPointer == TailPointer:
        print("Queue is empty.")
        return "Empty"
    else:
        HeadPointer += 1
        return Queue[HeadPointer - 1]


def ReadData():
    try:
        DataFile = open('QueueData.txt', 'r')
        for Line in DataFile:
            Enqueue(Line.strip())
        DataFile.close()
    except IOError:
        print("No file.")


def TotalData():
    global Records
    global NumberRecords
    DataAccessed = Dequeue()
    Flag = False
    if NumberRecords == 0:
        Records.append(RecordData(DataAccessed, 1))
        NumberRecords += 1
        Flag = True
    else:
        for x in range(0, NumberRecords):
            if Records[x].getID() == DataAccessed:
                Records[x].setTotal(Records[x].getTotal() + 1)
                Flag = True
    if not Flag:
        Records.append(RecordData(DataAccessed, 1))
        NumberRecords += 1


def OutputRecords():
    global Records
    global NumberRecords
    for x in range(0, NumberRecords):
        print(f"ID {Records[x].getID()} Total {Records[x].getTotal()}")


"""main"""
# global Queue
# global HeadPointer
# global TailPointer

Queue = [0 for x in range(0, 50)]  # string array of 50 elements
HeadPointer = -1
TailPointer = 0

Records = []  # RecordData array of 50 elements
NumberRecords = 0

ReadData()
while HeadPointer != TailPointer:
    TotalData()
OutputRecords()
