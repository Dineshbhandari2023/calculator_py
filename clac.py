from art import logoo
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = int(input("Enter your first Number: "))

    for symbol in operations:
        print(symbol) 

    should_continue = True
    while should_continue:
        operation_symbol = input("pick an operation from the line above: ")
        num2 = int(input("Enter your second Number: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue and 'n' to stop calculating with the {answer} \n") == "y":
            num1 = answer
        else:
            should_continue = False
            clear_console()
 
calculator()        

        
        
        
# operation_symbol = input("Pick another operation: ")
# num3 = int(input("Enter another Number: "))
# calculation_function = operations[operation_symbol]
# second_answer = calculation_function(calculation_function(num1, num2), num3)

# print(f"{answer} {operation_symbol} {num3} = {second_answer}")




