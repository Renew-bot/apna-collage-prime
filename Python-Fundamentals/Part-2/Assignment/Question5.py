# Q5. Write a function to return the sum of digits of a number, n .

def digit_sum(n):
    n = abs(n)
    sum = 0
    rem = 0
    while n>0:
        rem = n%10
        sum += rem
        n = n//10
    return sum

print(digit_sum(2222))