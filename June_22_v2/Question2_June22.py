import random


def printArray(arr):
    for x in range(0, 10):
        for y in range(0, 10):
            print(arr[x][y], " ", end="")
        print("\n")


def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        Mid = (Lower + (Upper - 1)) // 2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        elif SearchArray[0][Mid] > SearchValue:
            return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
        else:
            return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)

    return -1


ArrayData = [[0 for x in range(0, 10)] for y in range(0, 10)]

ArrayData = [[random.randint(1, 100) for x in range(0, 10)] for x in range(0, 10)]

print("Before")
printArray(ArrayData)

ArrayLength = 10
for X in range(0, ArrayLength):
    for Y in range(0, ArrayLength - 1):
        for Z in range(0, ArrayLength - Y - 1):
            if ArrayData[X][Z] > ArrayData[X][Z + 1]:
                TempNumber = ArrayData[X][Z]
                ArrayData[X][Z] = ArrayData[X][Z + 1]
                ArrayData[X][Z + 1] = TempNumber

print("After")
printArray(ArrayData)

print(BinarySearch(ArrayData, 0, 9, 99))