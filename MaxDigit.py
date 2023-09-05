
def MaxDigit(No):
    Digit = 0
    Max = 0
    while No != 0:
        Digit = int(No % 10)
        if(Digit > Max):
            Max = Digit
        No = int(No / 10)
    return Max

def main():
    Num = int(input("Enter the number : "))

    Ret = MaxDigit(Num)

    print("The largest digit from the number is : ",Ret)

if __name__ == "__main__":
    main()