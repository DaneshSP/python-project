def fact(n):
    if n<0:
        return "non negative numbers"
    elif n==0:
        return 1
    else:
        return n*fact(n-1)
            
num=int(input("enter a factorial number: "))
result=fact(num)
print(f"The factorial of {num} is {result}")
