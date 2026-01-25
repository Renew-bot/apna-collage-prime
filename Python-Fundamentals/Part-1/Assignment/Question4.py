# Q4. The user enters a string containing a number (e.g. "45" ). Convert it to:
# • an integer
# • a float
# • a string again
# Print all three values with their types

a = input("Enter a Number : ")

i = int(a)
f = float(a)
s = str(a)

print(type(i) , i)
print(type(f) , f)
print(type(s) , s)