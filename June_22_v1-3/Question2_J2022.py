class Balloon:
	# self.__Health : INTEGER
	# self.__Color : STRING
	# self.__DefenceItem : STRING
	def __init__(self, CColor, CDefenceItem):
		self.__Health = 100
		self.__Color = CColor
		self.__DefenceItem = CDefenceItem

	def GetDefenceItem(self):
		return self.__DefenceItem

	def ChangeHealth(self, change_in_health):
		self.__Health = self.__Health + change_in_health

	def CheckHealth(self):  # TRUE = balloon dead and FALSE = balloon alive
		if self.__Health <= 0:
			return True
		else:
			return False


def Defend(PBalloon):
	OpStrength = int(input("Enter the strength of the opponent: "))
	PBalloon.ChangeHealth(-OpStrength)
	print(f"You attempted to defend your opponent's attack with your {PBalloon.GetDefenceItem()}.")
	if PBalloon.CheckHealth():
		print("Defence unsuccessful. Your balloon has popped. RIP Balloon, You will be missed.")
	else:
		print("Defence successful! Your balloon is still floating!")
	return PBalloon


"""main"""

DefenceItem = input("Enter a new defence item: ")
Color = input("Enter a new color: ")

Balloon1 = Balloon(Color, DefenceItem)

Balloon1 = Defend(Balloon1)
