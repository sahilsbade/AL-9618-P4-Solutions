class Picture:
    def __init__(self, PDescription, PWidth, PHeight, PFrameColour):
        self.__Description = PDescription  # string
        self.__Width = PWidth  # integer
        self.__Height = PHeight  # integer
        self.__FrameColour = PFrameColour  # string

    def getDescription(self):
        return self.__Description

    def getHeight(self):
        return self.__Height

    def getWidth(self):
        return self.__Width

    def getColour(self):
        return self.__FrameColour

    def setDescription(self, SDescription):
        self.__Description = SDescription


PictureArray = [Picture("", 0, 0, "") for i in range(0, 100)]


def ReadData(PictureArray):
    Filename = "Pictures.txt"
    count = 0

    try:
        File = open(Filename, "r")

        RDescription = File.readline().lower().strip()

        while RDescription != "":
            RWidth = int(File.readline().strip())
            RHeight = int(File.readline().strip())
            RFrameColour = File.readline().lower().strip()

            PictureArray[count] = Picture(RDescription, RWidth, RHeight, RFrameColour)

            RDescription = File.readline().lower()

            count += 1

        File.close()

    except IOError:
        print("No file found")

    return count


NumberOfPictures = ReadData(PictureArray)

ReadData(PictureArray)

GFrameColour = input("Enter the frame colour: ").lower().strip()
GWidth = int(input("Enter the maximum width: ").strip())
GHeight = int(input("Enter the maximum height: ").strip())

for i in range(NumberOfPictures):
    if PictureArray[i].getColour() == GFrameColour and PictureArray[i].getWidth() <= GWidth and PictureArray[i].getHeight() <= GHeight:
        print(PictureArray[i].getDescription(), end=' ')
        print(PictureArray[i].getWidth(), end=' ')
        print(PictureArray[i].getHeight())
