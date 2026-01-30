# Q2. Write a function that takes two integers and and prints all even numbers between them (inclusive). 

def even(a,b):
    evens=[]
    for x in range(a,b):
        if x%2==0:
            evens.append(x)
    return evens

a = int(input("Enter a : "))
b = int(input("Enter b : "))
print(even(a,b))