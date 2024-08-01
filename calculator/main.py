import sys
  

def calculateResult(num1, operator, num2):
    operations = {
        '+': lambda x,y : x + y,
        '-': lambda x,y : x - y,
        '*': lambda x,y : x * y,
        '/': lambda x,y : x / y
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