
def DisplayTable(value):
    for i in range(1,11,1):
        print(" ",value * i)


def main():
    Num = int(input("Enter the number : "))

    print("The table is : ")
  
    DisplayTable(Num)


if __name__ == "__main__":
    main()