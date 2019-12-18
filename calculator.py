## Calculator
def add(num1, num2):
    return int(num1) + int(num2)


def subtract(num1, num2):
    return int(num1) - int(num2)


def multiply(num1, num2):
    return int(num1) * int(num2)


def division(num1, num2):
    return int(num1) / int(num2)

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
choice = input("Choose the operation (+, -, /, *): ")

if num1.isdigit() == False or num2.isdigit() ==False:
    print("the number is invalid")

elif choice == "+":
    print("The answer is", add(num1, num2))

elif choice == "-":
    print("The answer is ", subtract(num1, num2))
    
elif choice == "*":
    print("The answer is ", multiply(num1, num2))

elif choice == "/":
    print("The answer is ", division(num1, num2))

else:
    print("The operation is not valid")
