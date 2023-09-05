
def DisplayNonFactors(value):

    for i in range(1,value,1):

        if(value % i != 0):

            print("NonFactors are : ",i)


def main():
    Num = int(input("Enter the number : "))

    DisplayNonFactors(Num)


if __name__ == "__main__":
    main()