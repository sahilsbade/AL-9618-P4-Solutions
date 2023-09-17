
def Enqueue(DataToAdd):
	global QueueData
	global StartPointer
	global EndPointer

	if EndPointer == 20:
		return False
	else:
		QueueData[EndPointer] = DataToAdd
		EndPointer += 1
		return True


def Remove():
	global QueueData
	global StartPointer
	global EndPointer

	if EndPointer - StartPointer < 2:
		return "No Items"
	else:
		return QueueData[StartPointer] + " " + QueueData[StartPointer + 1]


def ReadFile():
	global QueueData
	global StartPointer
	global EndPointer

	Filename = input("Enter the file name: ")
	try:
		File = open(Filename, "r")
		Flag = True
		DataToInsert = (File.readline()).strip()
		Count = 1
		while Flag and len(DataToInsert) > 1:
			Flag = Enqueue(DataToInsert)
			DataToInsert = (File.readline()).strip()
			Count += 1
			if Count == 20:
				break

		if Count <= 20 and EndPointer < 19:
			File.close()
			return 1

		elif Count <= 20 and EndPointer == 19:
			File.close()
			return 2

	except IOError:
		return -1


"""main"""

QueueData = ["" for x in range(0, 20)]
StartPointer = 0
EndPointer = 0

Value = ReadFile()

if Value == -1:
	print("File not found")
elif Value == 2:
	print("Insufficient space in queue")
else:
	print("Enqueue from file successful")