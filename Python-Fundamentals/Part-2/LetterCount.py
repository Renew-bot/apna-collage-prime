count = 0
word = input("Enter a word or sentence : ")
alpha = input("Enter an alphabet to find : ")

for ch in word:
    if(ch==alpha):
        count+=1
print("In" , word , "'",alpha,"'" , "is has occured", count ,"times")