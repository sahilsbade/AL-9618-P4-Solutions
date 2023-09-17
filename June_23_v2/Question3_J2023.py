class Employee:
    # self.__HourlyPay single
    # self.__EmployeeNumber string
    # self.__JobTitle string
    def __init__(self, EmpNumP, PayP, JobP):
        self.__HourlyPay = PayP
        self.__EmployeeNumber = EmpNumP
        self.__JobTitle = JobP
        self.__PayYear2022 = []  # array 52 elements single
        for i in range(0, 52):
            self.__PayYear2022.append(0.00)

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self, WeekNumber, Hours):
        self.__PayYear2022[WeekNumber - 1] = Hours * self.__HourlyPay

    def GetTotalPay(self):
        TotalPay = 0
        for X in range(0, 52):
            TotalPay = TotalPay + self.__PayYear2022[X]
        return TotalPay


class Manager(Employee):
    # BonusValue single
    def __init__(self, EmpNumP, PayP, JobP, BonusP):
        super().__init__(EmpNumP, PayP, JobP)
        self.__BonusValue = BonusP

    def SetPay(self, WeekNumber, Hours):
        Hours = Hours * (1 + self.__BonusValue / 100)
        super().SetPay(WeekNumber, Hours)


def EnterHours():
    try:
        TextFile = "HoursWeek1.txt"
        File = open(TextFile, 'r')
        EmpID = ""

        for X in range(0, 8):
            EmpID = File.readline()
            for Y in range(0, 8):
                if EmployeeArray[Y].GetEmployeeNumber() == EmpID:
                    EmployeeArray[Y].SetPay(1, float(File.readline()))

        File.close()

    except IOError:
        print("Could not find file")


"""main"""

EmployeeArray = []
Pay = 0.00
ID = ""
Bonus = 0.00
Title = ""
Temp = ""
try:
    TextFile = "Employees.txt"
    File = open(TextFile, 'r')
    for x in range(0, 8):
        Pay = float(File.readline())
        ID = File.readline()
        Temp = File.readline()
        try:
            Bonus = float(Temp)
            Title = File.readline()
            EmployeeArray.append(Manager(ID, Pay, Title, Bonus))
        except ValueError:
            Title = Temp
            EmployeeArray.append(Employee(ID, Pay, Title))

    File.close()
except IOError:
    print("Could not find file")

EnterHours()
for y in range(0, 8):
    print(f"{EmployeeArray[y].GetEmployeeNumber()} {round(EmployeeArray[y].GetTotalPay(), 2)}")