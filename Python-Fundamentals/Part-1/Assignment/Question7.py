# Q7. Ask the user for a temperature in Celsius (string input). Convert it to , then calculate and print temperature in Fahrenheit. 
# Conversion formula: Fahrenheit Temp = (CelsiusTemp ∗ (9/5)) + 32

c = float(input("Enter Temperature in Celcius :"))
f = c * (9/5) + 35

print(c ,"Celcius = " ,f , "Fahrenheit")