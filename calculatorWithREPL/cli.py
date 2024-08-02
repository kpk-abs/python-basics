import sys

from operations import calculateResult

def main():
    if len(sys.argv) != 4:
        print("Give valid input.")
        sys.exit(1)    
        
    result = calculateResult(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
    print(result)

main()