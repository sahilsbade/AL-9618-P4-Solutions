import datetime


class Character:
    # self.__CharacterName : string
    # self.__DateOfBirth : date
    # self.__Intelligence : real
    # self.__Speed : int
    def __init__(self, CCharName, CCharDOB, CCharIntelligence, CCharSpeed):
        self.__CharacterName: str = CCharName
        self.__DateOfBirth: datetime.date = CCharDOB
        self.__Intelligence: float = CCharIntelligence
        self.__Speed: int = CCharSpeed

    def GetName(self) -> str:
        return self.__CharacterName

    def GetIntelligence(self) -> float:
        return self.__Intelligence

    def SetIntelligence(self, NewValue):
        self.__Intelligence = NewValue

    def Learn(self):
        self.__Intelligence += (self.__Intelligence * 0.10)

    def ReturnAge(self):
        return 2023 - self.__DateOfBirth.year


class MagicCharacter(Character):
    # self.__Element : string
    def __init__(self, CCharName, CCharDOB, CCharIntelligence, CCharSpeed, CCharElement):
        super().__init__(CCharName, CCharDOB, CCharIntelligence, CCharSpeed)
        self.__Element: str = CCharElement

    def Learn(self):
        if self.__Element == "fire" or self.__Element == "water":
            super().SetIntelligence(super().GetIntelligence() * 1.2)
        elif self.__Element == "earth":
            super().SetIntelligence(super().GetIntelligence() * 1.3)
        else:
            super().SetIntelligence(super().GetIntelligence() * 1.1)


"""main"""
FirstCharacter = Character("Royal", datetime.date(2019, 1, 1), 70, 30)
FirstCharacter.Learn()
print("{0} is {1} years old and has an intelligence value of {2}."
      .format(FirstCharacter.GetName(), FirstCharacter.ReturnAge(), FirstCharacter.GetIntelligence()))

FirstMagic = MagicCharacter("Light", datetime.date(2018, 3, 3), 75, 22, "fire")
FirstMagic.Learn()
print("{0} is {1} years old and has an intelligence value of {2}."
      .format(FirstMagic.GetName(), FirstMagic.ReturnAge(), FirstMagic.GetIntelligence()))
