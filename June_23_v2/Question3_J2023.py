class Employee:
    # self.__HourlyPay real
    # self.__EmployeeNumber string
    # self.__JobTitle string
    def __init__(self, CEmpNum, CPay, CJob):
        self.__HourlyPay = CPay
        self.__EmployeeNumber = CEmpNum
        self.__JobTitle = CJob
        self.__PayYear2022 = []  # array 52 elements single
        for i in range(0, 52):
            self.__PayYear2022.append(0.00)

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self, WeekNumber, Hours):
        self.__PayYear2022[WeekNumber - 1] = Hours * self.__HourlyPay

    def GetTotalPay(self):
        TotalPay = 0
        for i in range(0, 52):
            TotalPay += self.__PayYear2022[i]
        return TotalPay


class Manager(Employee):
    # BonusValue real
    def __init__(self, CEmpNum, CPay, CJob, CBonus):
        super().__init__(CEmpNum, CPay, CJob)
        self.__BonusValue = CBonus

    def SetPay(self, WeekNumber, Hours):
        Hours = Hours * (1 + self.__BonusValue / 100)
        super().SetPay(WeekNumber, Hours)


def EnterHours():
    try:
        Filename1 = "HoursWeek1.txt"
        File1 = open(Filename1, 'r')
        EmpID = ""

        for j in range(0, 8):
            EmpID = File1.readline().strip()
            for k in range(0, 8):
                if EmployeeArray[k].GetEmployeeNumber() == EmpID:
                    EmployeeArray[k].SetPay(1, float(File1.readline()))

        File1.close()

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
    Filename = "Employees.txt"
    File = open(Filename, 'r')
    for x in range(0, 8):
        Pay = float(File.readline())
        ID = File.readline().strip()
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
