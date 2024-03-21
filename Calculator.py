import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return x ** y

def modulo(x, y):
    return x % y

def square_root(x):
    if x < 0:
        return "Error! Square root of a negative number."
    else:
        return math.sqrt(x)

def factorial(x):
    if x < 0:
        return "Error! Factorial of a negative number."
    elif x == 0:
        return 1
    else:
        return x * factorial(x - 1)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Modulo")
print("7. Square Root")
print("8. Factorial")
print("9. Sine")
print("10. Cosine")
print("11. Tangent")

while True:
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10/11): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))
        elif choice == '6':
            print("Result:", modulo(num1, num2))
    elif choice in ('7', '8'):
        num1 = float(input("Enter a number: "))
        if choice == '7':
            print("Result:", square_root(num1))
        elif choice == '8':
            print("Result:", factorial(int(num1)))
    elif choice in ('9', '10', '11'):
        num1 = float(input("Enter an angle in radians: "))
        if choice == '9':
            print("Result:", sin(num1))
        elif choice == '10':
            print("Result:", cos(num1))
        elif choice == '11':
            print("Result:", tan(num1))
    else:
        print("Invalid input")
