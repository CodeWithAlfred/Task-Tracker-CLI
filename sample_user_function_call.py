def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

user_input = input("Enter operation and two numbers (e.g., 'add 2 3'): ")
parts = user_input.split()
operation = parts[0]
num1 = float(parts[1])
num2 = float(parts[2])

if operation in operations:
    result = operations[operation](num1, num2)
    print(f"The result is: {result}")
else:
    print("Invalid operation")
