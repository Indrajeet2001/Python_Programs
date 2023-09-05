
def SumDigits(No):
    Digit = 0
    Add = 0
    while No != 0:
        Digit = int(No % 10)
        Add = Digit + Add
        No = int(No / 10)
    return Add 

def main():
    Num = int(input("Enter the number : "))

    Ret = SumDigits(Num)

    print("Number of digits in the : ",Ret)

if __name__ == "__main__":
    main()