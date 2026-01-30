# Q4. Write a function to return the count the number of digits in a number n . 
#  228758

def Count_digit(n):
  n = abs(n) # handle negative
  count = 0
  if n == 0:
    return 1
  while n>0:
    count+=1
    n//=10
  return count

print(Count_digit(0))