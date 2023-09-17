def InsertionSort(TheData):
	for x in range(0, len(TheData)):
		DataToInsert = TheData[x]

		Inserted = 0
		NextValue = x - 1
		while NextValue >= 0 and Inserted != 1:
			if DataToInsert < TheData[NextValue]:
				TheData[NextValue + 1] = TheData[NextValue]
				NextValue = NextValue - 1
				TheData[NextValue + 1] = DataToInsert
			else:
				Inserted = 1


def OutputArray(TheData):
	for x in range(0, len(TheData)):
		print(TheData[x], end=" → ")
	print("End")


def Search(TheData):
	NumberInput=int(input("Enter a whole number: "))
	for x in range(0, len(TheData)):
		if TheData[x] == NumberInput:
			print("Found")
			return True

	print("Not found")
	return False


"""main"""

TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]

print("Before Sorting: ")
OutputArray(TheData)

InsertionSort(TheData)

print("After Sorting: ")
OutputArray(TheData)

Search(TheData)
Search(TheData)
