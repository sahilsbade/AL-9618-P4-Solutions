def IterativeVowels(Value: str) -> int:
    Total = 0
    for x in range(0, len(Value)):
        FirstCharacter = Value[0]
        if (FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i'
                or FirstCharacter == 'o' or FirstCharacter == 'u'):
            Total = Total + 1
        Value = Value[1:len(Value)]
    return Total


def RecursiveVowels(Value: str) -> int:
    if len(Value) == 0:
        return 0
    else:
        FirstCharacter = Value[0]
        if (FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i'
                or FirstCharacter == 'o' or FirstCharacter == 'u'):
            return 1 + RecursiveVowels(Value[1:len(Value)])
        else:
            return RecursiveVowels(Value[1:len(Value)])


"""main"""
print(IterativeVowels("house"))
print(RecursiveVowels("imagine"))
