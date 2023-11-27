class Card:
	# self.__Number : INTEGER
	# self.__Color : STRING

	def __init__(self, CNum, CCol):
		self.__Number = CNum
		self.__Color = CCol

	def GetNumber(self):
		return self.__Number

	def GetColor(self):
		return self.__Color


def ChooseCard():
	global NumbersChosen

	Continue = True

	while Continue:
		CardSelected = int(input("Enter a card number from 1 to 30: ")) - 1
		if CardSelected < 0 or CardSelected > 29:
			print("Number must be between 1 and 30.")
		elif NumbersChosen[CardSelected]:
			print("Card selected already taken.")
		else:
			print("Valid choice.")
			NumbersChosen[CardSelected] = True
			Continue = False
			return CardSelected


"""main"""

CardArray = [Card(0, "") for x in range(0, 30)]

global NumbersChosen

NumbersChosen = [False for y in range(0, 30)]

try:
	File = open("CardValues.txt", "r")
	for x in range(0, 30):
		CardArray[x] = Card(int(File.readline().strip()), str(File.readline().strip()))

	File.close()
except IOError:
	print("File not found.")

Player1 = []
for x in range(0, 4):
	ReturnNumber = ChooseCard()
	Player1.append(CardArray[ReturnNumber])

for x in range(0, 4):
	print(f"{Player1[x].GetNumber()} {Player1[x].GetColor()}")