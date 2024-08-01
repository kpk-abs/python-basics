import sys
  
add = lambda x,y : x + y

subtract = lambda x,y : x - y

multiply = lambda x,y : x * y

divide = lambda x,y : x / y

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