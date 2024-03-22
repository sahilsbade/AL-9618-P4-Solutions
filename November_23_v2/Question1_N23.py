def PushData(letter):
    global VowelTop
    global ConsonantTop

    if letter in ['a', 'e', 'i', 'o', 'u']:
        if VowelTop == 100:
            print("Vowel stack full")
        else:
            StackVowel.append(letter)
            VowelTop += 1
    else:
        if ConsonantTop == 100:
            print("Consonant stack full")
        else:
            StackConsonant.append(letter)
            ConsonantTop += 1


def ReadData():
    try:
        File = open("StackData.txt", "r")
        for Line in File:
            PushData(Line.strip())
        File.close()

    except IOError:
        print("File note found")


def PopVowel() -> str:
    global VowelTop

    if VowelTop == 0:
        return "No data"
    else:
        VowelTop -= 1
        return StackVowel[VowelTop]


def PopConsonant() -> str:
    global ConsonantTop

    if ConsonantTop == 0:
        return "No data"
    else:
        ConsonantTop -= 1
        return StackConsonant[ConsonantTop]

"""main"""

StackVowel = []  # string 100
StackConsonant = []  # string 100


global VowelTop  # integer
global ConsonantTop  # integer
VowelTop = 0
ConsonantTop = 0

ReadData()
Letters = ''
isEmpty = False

for i in range(5):
    while not isEmpty:
        choice = input("Vowel or consonant?").strip().lower()
        if choice == 'vowel':
            data_accessed = PopVowel()
            if data_accessed != 'No data':
                Letters += data_accessed
                break
            else:
                isEmpty = True

        elif choice == 'consonant':
            data_accessed = PopConsonant()
            if data_accessed != 'No data':
                Letters += data_accessed
                break
            else:
                isEmpty = True

print(Letters)