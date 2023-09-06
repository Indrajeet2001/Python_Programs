


def main():
    
    n = int(input())
    
    Arr = list()

    print("Enter the elements : ")
    for i in range(n):
        value = int(input())
        Arr.append(value)

    print("Elements of the List are : ")
    for i in range(n):
        print(Arr[i])

    Max1 = 0
    for i in range(n):
        if(Arr[i] > Max1):
            Max1 = Arr[i]
    
    Arr.remove(Max1)
    Max2 = Arr[0]
            
    for i in range(n-1):
        if((Arr[i] != Max1)):
            if(Arr[i] > Max2 & Arr[i] < Max1):
                Max2 = Arr[i]

    print("First Max is : ",Max1)
    print("Second Max is : ",Max2)

if __name__ == "__main__":
    main()