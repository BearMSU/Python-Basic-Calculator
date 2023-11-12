#Calculator
from replit import clear
from art import logo
#Add function
def add(n1, n2):
    return n1 + n2
#Subtract function
def subtract(n1, n2):
    return n1 - n2
#Multiply function
def multiply(n1, n2):
    return n1 * n2
#Divide function
def divide(n1, n2):
    return n1 / n2
#Dictionary of mathematical operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    # Get the numbers from the user
    num1 = float(input("What's the first number?: "))
    # Print the operator keys from the dictionary
    for operator in operations:
        print(operator)
    # Set Flag
    should_continue = True
    while should_continue == True:
        # Get the operator from the user
        operation = input("Choose an operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        # Get answer from operation
        calculation = operations[operation]
        answer = calculation(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
        num1 = answer
    else:
        should_continue = False
        clear()
        calculator()

calculator()
