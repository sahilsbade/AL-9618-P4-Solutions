def SearchValue(Root, ValueToFind):
	global ArrayNodes

	if Root == -1:
		return -1
	elif ArrayNodes[Root][1] == ValueToFind:
		return Root
	elif ArrayNodes[Root][1] == -1:
		return -1

	if ArrayNodes[Root][1] > ValueToFind:
		return SearchValue(ArrayNodes[Root][0], ValueToFind)
	if ArrayNodes[Root][1] < ValueToFind:
		return SearchValue(ArrayNodes[Root][2], ValueToFind)


def PostOrderTraversal(RootNode):
	if RootNode[0] != -1:
		PostOrderTraversal(ArrayNodes[RootNode[0]])

	if RootNode[2] != -1:
		PostOrderTraversal(ArrayNodes[RootNode[2]])

	print(str(RootNode[1]))


"""main"""

ArrayNodes = []
for x in range(0, 20):
	ArrayNodes.append([-1, -1, -1])

ArrayNodes = [[1, 20, 5], [2, 15, -1], [-1, 3, 3], [-1, 9, 4], [-1, 10, -1], [-1, 58, -1], [-1, -1, -1]]
FreeNode = 6
RootPointer = 0

ReturnValue = SearchValue(RootPointer, 15)

if ReturnValue == -1:
	print("Value not found.")
else:
	print(f"Value found at index {ReturnValue}")

PostOrderTraversal(ArrayNodes[RootPointer])