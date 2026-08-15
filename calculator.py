def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a,b):
    return a/b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter the operation |    + - / *   |: ")
if operation == "/" and num2 == 0:
    print("Cannot divide by zero")
    exit()


if operation == "+":
    result = add(num1,num2)
elif operation == "-":
    result = sub(num1,num2)
elif operation == "*":
    result = multiply(num1,num2)
elif operation == "/":
    result = divide(num1,num2)
else:
    result = "Invalid operation"

print(f"Answer: {result}")





