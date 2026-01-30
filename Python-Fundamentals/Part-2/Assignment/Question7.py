# Q7. Design a program to continuously input a number from user & print if it is positive or negative until the user enters “Quit”.
while True:
    print("\nCheck number is positive or negative")
    print('Enter "Quit" to stop ⛔')
    n = input("Enter a Number : ")

    if (n == "Quit"):
        break

    n = int(n)
    if(n>0):
        print("The number is Positive")
    elif(n<0):
        print("The number is Negative")
    else:
        print("Number is 0️⃣")