import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculateResult(num1, operator, num2):
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    operation = operations.get(operator)
    return operation(num1, num2)

def main():
    if len(sys.argv) != 4:
        print("Give valid input.")
        sys.exit(1)    
        
    result = calculateResult(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
    print(result)

main()