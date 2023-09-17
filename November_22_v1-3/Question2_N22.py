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


class Hand:
	# self.__Cards[10] : Card
	# self.__FirstCard : INTEGER
	# self.__NumberCards : INTEGER
	def __init__(self, Card1, Card2, Card3, Card4, Card5):
		self.__Cards = []
		self.__Cards.append(Card1)
		self.__Cards.append(Card2)
		self.__Cards.append(Card3)
		self.__Cards.append(Card4)
		self.__Cards.append(Card5)
		self.__FirstCard = 0
		self.__NumberCards = 5

	def GetCard(self, index):
		return self.__Cards[index]


def CalculateValue(PlayerHand):
	points = 0

	for x in range(0, 5):
		PlayerCard = PlayerHand.GetCard(x)
		points = points + PlayerCard.GetNumber()
		CardColor = PlayerCard.GetColor()

		if CardColor == "red":
			points += 5
		elif CardColor == "blue":
			points += 10
		else:
			points += 15

	return points


"""main"""

Red1 = Card(1, "red")
Red2 = Card(2, "red")
Red3 = Card(3, "red")
Red4 = Card(4, "red")
Red5 = Card(5, "red")

Blue1 = Card(1, "blue")
Blue2 = Card(2, "blue")
Blue3 = Card(3, "blue")
Blue4 = Card(4, "blue")
Blue5 = Card(5, "blue")

Yellow1 = Card(1, "yellow")
Yellow2 = Card(2, "yellow")
Yellow3 = Card(3, "yellow")
Yellow4 = Card(4, "yellow")
Yellow5 = Card(5, "yellow")

Player1 = Hand(Red1, Red2, Red3, Red4, Yellow1)
Player2 = Hand(Yellow2, Yellow3, Yellow4, Yellow5, Blue1)

if CalculateValue(Player1) > CalculateValue(Player2):
	print("Player 1 wins!")
elif CalculateValue(Player1) < CalculateValue(Player2):
	print("Player 2 wins!")
else:
	print("There has been a draw.")