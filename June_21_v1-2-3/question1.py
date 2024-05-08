class Node:
	def __init__(self, CData, CnextNode):
		self.data = CData
		self.nextNode = CnextNode


def outputNodes(arr, Pointer):
	currentPointer = Pointer
	while currentPointer != -1:
		print(arr[currentPointer].data, end=" → ")
		currentPointer = arr[currentPointer].nextNode
	print("∅")


def addNode(arr, startP, emptyL):
	currentPointer = startP

	add_data = input("Enter the data to be added: ")

	if emptyL < 0 or emptyL > 9:
		return False

	else:
		newEmptyL = arr[emptyL].nextNode
		newNode = Node(int(add_data), -1)
		arr[emptyL] = newNode

		previousPointer = 0

		while currentPointer != -1:
			previousPointer = currentPointer
			currentPointer = arr[currentPointer].nextNode

		arr[previousPointer].nextNode = emptyL
		emptyL = newEmptyL

		return True, emptyL


'''main'''

linkedList = [Node(1, 1), Node(5, 4), Node(6, 7), Node(7, -1), Node(2, 2), Node(0, 6), Node(0, 8), Node(56, 3), Node(0, 9), Node(0, -1)]

startPointer = 0
emptyList = 5

outputNodes(linkedList, startPointer)
returnValue, emptyList = addNode(linkedList, startPointer, emptyList)

if returnValue:
	print("Item successfully added")
else:
	print("Item not added, list full")
outputNodes(linkedList, startPointer)
