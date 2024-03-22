def IterativeCalculate(Number: int) -> int:
    # ToFind : INTEGER
    # Total : INTEGER
    ToFind = Number
    Total = 0

    while Number != 0:
        if ToFind % Number == 0:
            Total += Number

        Number -= 1

    return Total


def RecursiveValue(Number: int, ToFind: int) -> int:
    if Number == 0:
        return 0
    else:
        if ToFind % Number == 0:
            return Number + RecursiveValue(Number - 1, ToFind)
        else:
            return RecursiveValue(Number - 1, ToFind)


"""main"""

print(IterativeCalculate(10))
print(RecursiveValue(50, 50))