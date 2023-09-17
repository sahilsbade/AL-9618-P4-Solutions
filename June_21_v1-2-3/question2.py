
def linearSearch(data):
	for x in range(0, 10):
		if arrayData[x] == data:
			return True

	return False


def bubbleSort():
	for x in range(0, 9):
		for y in range(0, 8):
			if arrayData[y] > arrayData[y + 1]:
				temp = arrayData[y]
				arrayData[y] = arrayData[y + 1]
				arrayData[y + 1] = temp


"""main"""

arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

value_to_find = int(input("Enter the *integer* value to be found: "))
result = linearSearch(value_to_find)

if result:
	print(f"{value_to_find} found in array")
else:
	print(f"{value_to_find} not found in array")