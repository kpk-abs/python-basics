from operations import calculateResult

def parseExpression(userInput):
    userInput = userInput.replace(' ', '')
    data = []
    temp = ''
    for char in userInput:
        if char.isdigit():
            temp += char
        else:
            if temp:
                data.append(int(temp))
                temp = ''
            data.append(char)
    
    if temp:
        data.append(int(temp))
    
    return data
  
def main():
  while True:
    userInput = input(">>> ")
    if userInput.lower() == 'exit':
      break

    inputArray = parseExpression(userInput)
    result = calculateResult(inputArray[0], inputArray[1], inputArray[2])
    print(result)
    
main()