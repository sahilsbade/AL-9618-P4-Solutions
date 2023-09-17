class HiddenBox:

	# self.__BoxName String
	# self.__Creator String
	# self.__DateHidden String
	# self.__GameLocation String
	# self.__LastFinds [10][2] String
	# self.__Active String

	def __init__(self, CName, CCreator, CDate, CLoc):
		self.__BoxName = CName
		self.__Creator = CCreator
		self.__DateHidden = CDate
		self.__GameLocation = CLoc

	def GetGameLocation(self):
		return self.__GameLocation

	def GetBoxName(self):
		return self.__BoxName


def NewBox(TheBoxes):
	global NumBoxes
	BoxName = input("Enter the name of the box: ")
	Creator = input("Enter the creator of the box: ")
	DateHidden = input("Enter the date when the box was hidden: ")
	GameLocation = input("Enter the location of the box: ")
	TheBoxes[NumBoxes] = HiddenBox(BoxName, Creator, DateHidden, GameLocation)
	NumBoxes += 1


class PuzzleBox(HiddenBox):
	# self.__PuzzleText String
	# self.__Solution String
	def __init__(self, CPuzzleText, CSolution, CName, CCreator, CDate, CLoc):
		super().__init__(CName, CCreator, CDate, CLoc)
		self.__PuzzleText = CPuzzleText
		self.__Solution = CSolution


"""main"""
NumBoxes = 0
TheBoxes = [HiddenBox("", "", "", "") for x in range(0, 10000)]

NewBox(TheBoxes)
