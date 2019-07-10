firstNumber = int(input("Enter the first number amongst the range"))
secondNumber = int(input("Enter the last number amongst the range"))

for i in range(firstNumber,secondNumber):
    if(i%2 == 0):
        print(i)