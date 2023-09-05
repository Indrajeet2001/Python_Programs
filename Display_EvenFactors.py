
def DisplayFactors(value):
    Fact = 1
    for i in range(1,value,1):
        if((value % i == 0) & (i % 2 == 0)):
            print("Factors are : ",i)


def main():
    Num = int(input("Enter the number : "))

    DisplayFactors(Num)


if __name__ == "__main__":
    main()