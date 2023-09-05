
def Palindrome(No):
    Rev = 0
    Digit = 0
    value = No
    while No != 0:
        Digit = int(No % 10)
        Rev = int(Rev * 10 + Digit)
        No = int(No / 10)
    if(Rev == value):
        return True
    else:
        return False
    
def main():
    Num = int(input("Enter the number : "))

    Ret = Palindrome(Num)

    if(Ret == True):
        print("Number is palindrome")
    else:
        print("Number is not palindrome")

if __name__ == "__main__":
    main()