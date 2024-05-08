# global StackPointer
# global StackData

StackPointer = 0  # integer
StackData = [0 for i in range(0, 10)]  # integer


def output_stack():
    global StackPointer
    global StackData

    for i in range(0, 10):
        print(StackData)


def Push(data):
    global StackPointer
    global StackData

    if StackPointer == 10:
        return False

    else:
        StackData[StackPointer] = data
        StackPointer += 1
        return True


def Pop():
    global StackPointer
    global StackData

    if StackPointer == 0:
        return -1

    else:
        ReturnData = StackData[StackPointer - 1]
        StackPointer -= 1
        return ReturnData


# StackPointer = 0  # integer
# StackData = [0 for i in range(0,10)]  # integer


for x in range(0, 11):
    num = int(input("Enter a number: "))

    if Push(num):
        print("Stored")

    else:
        print("Stack full")

for x in range(0, 10):
    print(StackData[x])

Pop()
Pop()

print("\n")

for x in range(0, StackPointer):
    print(StackData[x])
