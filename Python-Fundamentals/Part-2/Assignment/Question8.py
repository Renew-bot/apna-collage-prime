# Q8. Letʼs create a Simple Calculator that performs arithmetic operations. Create a function calculator(a, b, operation) that performs addition, subtraction, 
# multiplication, or division based on the operation parameter. [ operation parameter can have values + , - , * , /  .

def calc(a, b, operation):
    match operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b != 0:
                return a / b
            return "Error: Division by zero"
        case _:
            return "Invalid operation"


print(calc(2,0,'/'))