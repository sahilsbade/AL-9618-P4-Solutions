DataArray = []  # 25 cell integer array

Filename = "Data.txt"
File = open(Filename, "r")

try:
    for Line in File:
        DataArray.append(int(Line))

    File.close()

except IOError:
    print("No file found")


def PrintArray(arr):
    for i in range(0, len(arr)):
        print(arr[i], end= " ")


PrintArray(DataArray)


def LinearSearch(arr, data_to_found):
    Count = 0
    for x in range(0, len(arr)):
        if arr[x] == data_to_found:
            Count += 1

    return Count


DataToFind = int(input("\nEnter a number between 0 and 100 (inclusive): "))
if DataToFind < 0 or DataToFind > 100:
    DataToFind = int(input("Enter a number between 0 and 100 (inclusive)"))

print(f"The number {DataToFind} is found {LinearSearch(DataArray, DataToFind)} times.")
