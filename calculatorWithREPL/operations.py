def calculateResult(num1, operator, num2):
    operations = {
        '+': lambda x,y : x + y,
        '-': lambda x,y : x - y,
        '*': lambda x,y : x * y,
        '/': lambda x,y : x / y
    }

    operation = operations.get(operator)
    return operation(num1, num2)
