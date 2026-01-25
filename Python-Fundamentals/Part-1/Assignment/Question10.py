# Q10. Take a decimal number as input (like 45.78 ) and output its:
# • integer part - 45
# • fractional part - .78

num = float(input("Enter a decimal number: "))

IntegerPart = int(num)
FractionPart = num - IntegerPart

print("Integer part:", IntegerPart)
print("Fractional part:", round(FractionPart, 2))