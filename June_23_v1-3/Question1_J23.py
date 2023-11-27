DataArray = []  # 25 cell integer array

Filename = "Data.txt"
File = open(Filename, "r")

try:
    for Line in File:
        DataArray.append(int(Line))

    File.close()

except IOError:
    print("No file found")


def PrintArray(DataArray):
    for i in range(0, len(DataArray)):
        print(DataArray[i], end=" ")


PrintArray(DataArray)


def LinearSearch(DataArray, DataToFind):
    Count = 0
    for x in range(0, len(DataArray)):
        if DataArray[x] == DataToFind:
            Count += 1

    return Count


DataToFind = int(input("\nEnter a number between 0 and 100 (inclusive): "))
if DataToFind < 0 or DataToFind > 100:
    DataToFind = int(input("Enter a number between 0 and 100 (inclusive)"))

print(f"The number {DataToFind} is found {LinearSearch(DataArray, DataToFind)} times.")
