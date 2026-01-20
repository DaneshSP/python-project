def odd_num(n):
    for i in range(n+1):
        if i %2 !=0:
            print(i, end=" ")
            
n=int(input("enter a number: "))
odd_num(n)
