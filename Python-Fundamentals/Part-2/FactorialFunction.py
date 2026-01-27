def factorial(n):
    mul=1
    for x in range(1,n+1):
        mul*=x
    return(mul)

f = int(input("Enter a number to calculate its factorial : "))
print(factorial(f))