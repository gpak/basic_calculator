# Creating a simple calculator.
# x = first number
# y = second number
def add(x,y):
    addition = x + y
    return addition
#Check to see if function works.
#print(add(2, 3))
def subtract(x,y):
    subtraction = x - y
    return subtraction

def multiply(x,y):
    multiplication = x * y
    return multiplication

def divide(x,y):
    division = x / y
    return division

while True:
    choice = input("Enter Choice:  1, 2, 3, 4: ")

    if choice in ('1','2','3','4'):
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))

        if choice == '1':
            print(num1, "+", num2, '=', add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, '=', subtract(num1, num2))
        elif choice == '3':
            print(num1, '*', num2, '=', multiply(num1, num2))
        elif choice == '4':
            print(num1, '/', num2, '=', divide(num1, num2))
        break
    else:
            print('Invalid Number')
