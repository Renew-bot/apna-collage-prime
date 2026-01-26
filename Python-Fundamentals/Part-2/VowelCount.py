count = 0
word = input("Enter a word or sentence : ")

for ch in word:
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        count+=1
print("Their are",count,"Vowels in",word)