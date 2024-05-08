Animal = []
Colour = []
AnimalTopPointer = 0
ColourTopPointer = 0


def PushAnimal(DataToPush):
    global AnimalTopPointer
    global ColourTopPointer
    if AnimalTopPointer == 20:
        return False

    else:
        Animal.append(DataToPush)
        AnimalTopPointer += 1

        return True


def PopAnimal():
    # ReturnData string
    global AnimalTopPointer
    global ColourTopPointer
    if AnimalTopPointer == 0:
        return ""

    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData


def ReadData():
    try:
        global AnimalTopPointer
        global ColourTopPointer
        AnimalFile = open("AnimalData.txt", 'r')

        for Line in AnimalFile:
            PushAnimal(Line.strip())

        AnimalFile.close()

        ColourFile = open("ColourData.txt", 'r')
        for Line in ColourFile:
            PushColour(Line.strip())

        ColourFile.close()

    except IOError:
        print("Could not find file")


def PushColour(DataToPush):
    global AnimalTopPointer
    global ColourTopPointer
    if ColourTopPointer == 20:
        return False

    else:
        Colour.append(DataToPush)
        ColourTopPointer += 1

        return True


def PopColour():
    # ReturnData string
    global AnimalTopPointer
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ""

    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return ReturnData


def OutputItem():
    global AnimalTopPointer
    global ColourTopPointer

    ColourReturned = PopColour()
    AnimalReturned = PopAnimal()

    if ColourReturned == "":
        print("No colour")
        PushColour(ColourReturned)

    elif AnimalReturned == "":
        print("No animal")
        PushColour(AnimalReturned)

    else:
        print(f"{ColourReturned} {AnimalReturned}")


# main program

ReadData()
for x in range(0, 4):
    OutputItem()
