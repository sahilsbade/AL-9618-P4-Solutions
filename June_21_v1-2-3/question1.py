class node:
	def __init__(self, CData, CnextNode):
		self.data = CData
		self.nextNode = CnextNode


def outputNodes(arr, Pointer):
	currentPointer = Pointer
	while currentPointer != -1:
		print(arr[currentPointer].data, end=" → ")
		currentPointer = arr[currentPointer].nextNode
	print("∅")


def addNode(arr, startPointer, emptyList):
	currentPointer = startPointer

	add_data = input("Enter the data to be added: ")

	if emptyList < 0 or emptyList > 9:
		return False

	else:
		newNode = node(int(add_data), -1)
		arr[emptyList] = newNode

		previousPointer = 0

		while currentPointer != -1:
			previousPointer = currentPointer
			currentPointer = arr[currentPointer].nextNode

		arr[previousPointer].nextNode = emptyList
		emptyList = arr[emptyList].nextNode

		return True


'''main'''

linkedList = [node(1, 1), node(5, 4), node(6, 7), node(7, -1),
			  node(2, 2), node(0, 6), node(0, 8), node(56, 3), node(0, 9), node(0, -1)]

startPointer = 0
emptyList = 5

outputNodes(linkedList, startPointer)
returnValue = addNode(linkedList, startPointer, emptyList)

if returnValue:
	print("Item successfully added")
else:
	print("Item not added, list full")
outputNodes(linkedList, startPointer)

