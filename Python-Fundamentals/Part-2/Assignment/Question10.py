# 10. Letʼs create a “Number Guessing Game”. Given a secret number (already decided by you), write a program that asks the user to guess it and prints: 
# "Too high"  if the guess is above the number 
# "Too low" if the guess is below 
# "Correct!" if the guess matches 
import random
print("Number Guessing Game🎮")
ans = random.randint(1,100)
while True :
    n = int(input("Guess an Number : "))
    if n==ans : 
        print("Your guess is correct ✅")
        break
    elif n>ans :
         print("Too High") 
    elif n<ans : 
        print("Too low")
    else: print('Invalid Input')