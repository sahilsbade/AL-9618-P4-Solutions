class SaleData:
    def __init__(self, PSaleID, PQuantity):
        self.SaleID = PSaleID  # string
        self.Quantity = PQuantity  # integer


CircularQueue = []  # SaleData - 5 items
global Head
global Tail
global NumberOfItems

Head = 0
Tail = 0
NumberOfItems = 0
for x in range(0, 5):
    CircularQueue.append(SaleData("", -1))


def Enqueue(RecordToAdd):
    global Head
    global Tail
    global NumberOfItems

    if NumberOfItems == 5:
        return -1
    else:
        CircularQueue[Tail] = RecordToAdd
        if Tail == 4:
            Tail = 0
        else:
            Tail += 1

        NumberOfItems += 1
        return 1

def Dequeue():
    global Head
    global Tail
    global NumberOfItems

    if NumberOfItems == 0:
        return SaleData("", -1)
    else:
        RecordRemoved = CircularQueue[Head]
        NumberOfItems -= 1
        if Head == 4:
            Head = 0
        else:
            Head += 1

        return RecordRemoved

def EnterRecord():
    ID = input("Enter ID: ")
    Quantity = int(input("Enter Quantity: "))
    Record = SaleData(ID, Quantity)

    if Enqueue(Record) == -1:
        print("Full")
    else:
        print("Stored")


for x in range(0, 6):
    EnterRecord()

ReturnValue = Dequeue()

if ReturnValue == -1:
    print("Queue Empty")
else:
    print(ReturnValue.SaleID, " ", ReturnValue.Quantity)

EnterRecord()

for x in range(0, 5):
    print(CircularQueue[x].SaleID, " ", CircularQueue[x].Quantity)