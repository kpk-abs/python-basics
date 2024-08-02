operations = {
        '+': lambda x,y : x + y,
        '-': lambda x,y : x - y,
        '*': lambda x,y : x * y,
        '/': lambda x,y : x / y
    }

def calculateResult(num1, operator, num2):
    return operations[operator](num1,num2)
