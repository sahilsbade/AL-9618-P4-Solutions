def ReadFile():
	global DataArray
	try:
		File = open("IntegerData.txt", "r")

		for x in range(0, 100):
			DataArray[x] = int(File.readline().strip())

		File.close()

	except IOError:
		print("File not found.")


def FindValues():
	global DataArray
	data_to_find = -1
	while data_to_find < 1 or data_to_find > 100:
		data_to_find = int(input("Enter the number (between 1 and 100) you wish to find: "))

	count = 0
	for x in range(0, 100):
		if DataArray[x] == data_to_find:
			count += 1

	return count


def BubbleSort():
	global DataArray

	swaps = True
	top = 100
	while swaps or top > 0:
		swaps = False

		for x in range(0, top - 1):
			if DataArray[x] > DataArray[x + 1]:
				Temp = DataArray[x]
				DataArray[x] = DataArray[x + 1]
				DataArray[x + 1] = Temp
			swaps = True
		top -= 1


"""main"""

DataArray = [0 for x in range(0, 100)]

ReadFile()

print(f"The number you entered was found {FindValues()} times.")

BubbleSort()
for x in range(0, len(DataArray)):
	print(DataArray[x], end=" → ")
print("End")
