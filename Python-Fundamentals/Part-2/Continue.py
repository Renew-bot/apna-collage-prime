i = 1
while(i<=10):
    if(i%6==0):
        i+=1
        continue # skip loop at 6 then continue to next
    print(i)
    i+=1

# Example
j = 0
print("\nPrint all odd no bw 1 to 10\n")
while(j<10):
    j+=1
    if(j%2==0):
        continue
    print(j)