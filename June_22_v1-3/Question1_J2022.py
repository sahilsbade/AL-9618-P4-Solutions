
def ReadHighScores():
	Filename = "HighScore.txt"
	File = open(Filename, "r")

	for x in range(0, 10):
		FileData[x][0] = File.readline().strip()
		FileData[x][1] = int(File.readline().strip())

	File.close()


def OutputHighScores():
	for x in range(0, 11):
		print(f"{FileData[x][0]} {FileData[x][1]}")


def Arrange(PlayerName, points):
	for x in range(0, 10):
		if points > FileData[x][1]:
			Temp1 = FileData[x][0]
			Temp2 = FileData[x][1]
			FileData[x][0] = PlayerName
			FileData[x][1] = points
			Count = x + 1

			while Count < 10:
				Second1 = FileData[Count][0]
				Second2 = FileData[Count][1]
				FileData[Count][0] = Temp1
				FileData[Count][1] = Temp2

				Temp1 = Second1
				Temp2 = Second2
				Count += 1
			break


def WriteTopTen():
	File = open("NewHighScore.txt", "w")
	for x in range(0, 10):
		File.write(str(FileData[x][0]) + "\n")
		File.write(str(FileData[x][1]) + "\n")
	File.close()


"""main"""

FileData = [["" for x in range(0, 2)] for y in range(0, 11)]

ReadHighScores()
OutputHighScores()

Username = "ABCD"
while len(Username) != 3:
	Username = input("Enter your Username: ")

score = -1
while score < 1 or score > 100000:
	score = int(input("Enter your score: "))

Arrange(Username, score)

OutputHighScores()
