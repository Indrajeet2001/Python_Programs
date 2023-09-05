
def CountDigits(No):
    Cnt = 0
    while No != 0:
        Cnt += 1
        No = int(No / 10)
    return Cnt

def main():
    Num = int(input("Enter the number : "))

    Ret = CountDigits(Num)

    print("Number of digits in the : ",Ret)

if __name__ == "__main__":
    main()