# FORMATTING = 

# format() :- py3 , placeholder{} , placement value , 

# f-strings :- py 3.6 , Literal String Interpolation , print(f"  ") , variable , expression

a=5
b=10
sum = a+b

print("1]format()")

#Normal Formatting
print("Sum is {}".format(sum))
print("Sum of {} + {} is {}".format(a,b,sum))
print("I love {}".format("Python"))

#Index Based Formating
print("Sum of {1} + {0} is {2}".format(a,b,sum))

# Value Based Formatting
print("Values of Variables {c} & {d}".format(c=2,d=4))

print("\n2]F-strings")
print(f"Sum Of {a} & {b} is {a+b}")
print(f"Average Of {a} & {b} is {(a+b)/2}")