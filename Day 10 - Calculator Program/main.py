import art

we_continue = True #main program function
final_answer = 0 #'global' variable
no_previous_op = True #if there is a previous number to save

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2

operations_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(art.logo)
while we_continue:
    operation = ""
    num1 = 0

    if no_previous_op:
        num1 = float(input("What is the first number?: "))
    else:
        print(f"First number is {final_answer}\n")

    op = input("Pick an operation: \n+\n-\n*\n/\n")

    if op in operations_dictionary:
        operation = operations_dictionary[op]
    else:
        print("Invalid operation")
        continue

    num2 = float(input("What is the second number?: "))

    final_answer = operation(num1, num2) 

    print(f"The answer is {num1} {op} {num2} = {final_answer}\n")

    next_operation = input("Would you like to continue with this number (y/n)?\n").lower()

    if next_operation == "y":
        num1 = final_answer
        no_previous_op = False
        continue
    elif next_operation == "n":
        final_answer = 0
        no_previous_op = True
        print("\n" * 10)
        print(art.logo + "\n")
        continue
    else:
        print("Invalid input. \nExit Program.")
        we_continue = False