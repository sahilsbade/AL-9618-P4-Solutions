def Enqueue(QueueArray, HeadPointer, TailPointer, NumberItems, DataToAdd):
	if NumberItems == 10:
		return False, QueueArray, HeadPointer, TailPointer, NumberItems

	QueueArray[TailPointer] = DataToAdd
	if TailPointer >= 9:
		TailPointer = 0
	else:
		TailPointer += 1

	NumberItems += 1

	return True, QueueArray, HeadPointer, TailPointer, NumberItems


def Dequeue(QueueArray, HeadPointer, NumberItems):
	if NumberItems == 0:
		return False, QueueArray, HeadPointer, NumberItems
	else:
		ReturnValue = QueueArray[HeadPointer]
		HeadPointer += 1

		if HeadPointer >= 9:
			HeadPointer = 0

		NumberItems -= 1
		return ReturnValue, QueueArray, HeadPointer, NumberItems


"""main"""

# HeadPointer : INTEGER
# TailPointer : INTEGER
# NumberItems : INTEGER

HeadPointer = 0
TailPointer = 0
NumberItems = 0
QueueArray = ["" for x in range(0, 10)]

for x in range(0, 11):
	InputString = input("Enter a string: ")
	Status1, QueueArray, HeadPointer, TailPointer, NumberItems = Enqueue(QueueArray, HeadPointer, TailPointer, NumberItems, InputString)
	if Status1:
		print("Enqueue Successful")
	else:
		print("Enqueue Unsuccessful")

Value, QueueArray, HeadPointer, NumberItems = Dequeue(QueueArray, HeadPointer, NumberItems)
print(Value)
Value, QueueArray, HeadPointer, NumberItems = Dequeue(QueueArray, HeadPointer, NumberItems)
print(Value)
