global Animals  # string array of 10 elements
Animals = []

Animals.append("horse")
Animals.append("lion")
Animals.append("rabbit")
Animals.append("mouse")
Animals.append("bird")
Animals.append("deer")
Animals.append("whale")
Animals.append("elephant")
Animals.append("kangaroo")
Animals.append("tiger")


def SortDescending():
	ArrayLength = 10
	for x in range(0, ArrayLength - 1):
		for y in range(0, ArrayLength - x - 1):
			if Animals[y][0] < Animals[y + 1][0]:
				Temp = Animals[y]
				Animals[y] = Animals[y + 1]
				Animals[y + 1] = Temp


SortDescending()
for x in range(0, len(Animals)):
	print(Animals[x])
