
def Enqueue(Data):
    global Queue
    global TailPointer
    global HeadPointer
    if TailPointer < 100:
        if HeadPointer == -1:
            HeadPointer = 0
        Queue[TailPointer] = Data
        TailPointer += 1
        return True
    return False


def RecursiveOutput(Start):
    global Queue
    if Start == 0:
        return Queue[Start]
    else:
        return Queue[Start] + RecursiveOutput(Start - 1)


""""main"""
Queue = [-1 for x in range(0, 100)]
HeadPointer = -1
TailPointer = 0

Success = False
for count in range(1, 121):
    Success = Enqueue(count)
    if not Success:
        print("Unsuccessful Enqueue")
    else:
        print("Success")

print(RecursiveOutput(TailPointer - 1))